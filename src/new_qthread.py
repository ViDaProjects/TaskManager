from PySide6.QtCore import QThread
from io_gatherer import PublisherIOData
from io_process import ProcessIOData
import time
from threading import Lock
from file_gather import PublisherFileData
from pid_info import PIDInfo
import data_classes

class GatherIOThread(QThread):
    def __init__(self, lock_gather_info):
        super().__init__()
        self.lock_gather_info = lock_gather_info
        self._running = True

        self.io_gatherer = PublisherIOData(lock_gather_info)

    def run(self):
        while self._running:
            time.sleep(0.1)
            disk_info = self.io_gatherer.gather_io_data()
            
            # Guarantees it publishes everything
            #with self.lock_gather_info:
            #    print(data_classes.get_io_raw())

    def stop(self):
        self._running = False

class ProcessIOThread(QThread):
    def __init__(self, lock_sub_info, lock_pub_info):
        super().__init__()
        self.lock_sub_info = lock_sub_info
        self.lock_pub_info = lock_pub_info
        self._running = True

        self.file_processor = PublisherFileData(lock_sub_info, lock_pub_info)

    def run(self):
        while self._running:
            self.sleep(0.1)
            self.file_processor.gather_file_data()
            
            # Guarantees it publishes everything
            #with self.lock_pub_info:
            #    print(data_classes.get_file_data())

    def stop(self):
        self._running = False

class FileInfoThread(QThread):
    def __init__(self, lock_sub_info, lock_pub_info):
        super().__init__()
        self.lock_sub_info = lock_sub_info
        self.lock_pub_info = lock_pub_info
        self._running = True

        self.io_processor = ProcessIOData(lock_sub_info, lock_pub_info)

    def run(self):
        while self._running:
            self.io_processor.process_io_data()

    def stop(self):
        self._running = False

class PIDInfoThread(QThread):
    def __init__(self, lock_pid_num, lock_pid_info):
        super().__init__()
        self.lock_pid_num = lock_pid_num
        self.lock_pid_info = lock_pid_info
        self._running = True

        self.pid_processor = PIDInfo(self.lock_pid_info, self.lock_pid_num)

    def run(self):
        while self._running:
            self.pid_processor.get_pid_info()
            #with self.lock_pid_info:
            #    print(data_classes.get_pid_info())

    def stop(self):
        self._running = False


if __name__ == "__main__":
    lock_gather_info = Lock()
    lock_PID = Lock()
    lock_PID_info = Lock()
    lock_pub_info = Lock()

    lock_gather_io = Lock()
    lock_pub_io = Lock()
    lock_file_path = Lock()
    lock_file_info = Lock()

    gather_io_thread = GatherIOThread(lock_gather_info)
    process_io_thread = ProcessIOThread(lock_gather_info, lock_pub_info)

    file_info_thread = FileInfoThread(lock_sub_info=lock_file_path, lock_pub_info=lock_file_info)

    pid_info_thread = PIDInfoThread(lock_PID, lock_PID_info)

    gather_io_thread.start()
    process_io_thread.start()
    file_info_thread.start()

    pid_info_thread.start()

    time.sleep(5)

    gather_io_thread.stop()
    process_io_thread.stop()
    file_info_thread.stop()

    pid_info_thread.stop()

    gather_io_thread.wait()
    process_io_thread.wait()
    file_info_thread.wait()

    pid_info_thread.wait()