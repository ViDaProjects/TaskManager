from PySide6.QtCore import QThread
from io_gatherer import PublisherIOData
from io_process import ProcessIOData
import time
from threading import Lock
from file_gather import PublisherFileData
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
            self.file_processor.gather_file_data()
            
            # Guarantees it publishes everything
            with self.lock_pub_info:
                print(data_classes.get_file_data())

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


if __name__ == "__main__":
    lock_gather_info = Lock()
    lock_pub_info = Lock()

    lock_file_path = Lock()
    lock_file_info = Lock()

    gather_io_thread = GatherIOThread(lock_gather_info)
    process_io_thread = ProcessIOThread(lock_gather_info, lock_pub_info)

    file_info_thread = FileInfoThread(lock_sub_info=lock_file_path, lock_pub_info=lock_file_info)

    gather_io_thread.start()
    process_io_thread.start()
    file_info_thread.start()

    time.sleep(5)

    gather_io_thread.stop()
    process_io_thread.stop()
    file_info_thread.stop()

    gather_io_thread.wait()
    process_io_thread.wait()
    file_info_thread.wait()