from PySide6.QtCore import QThread
import data_gather
import process_data
import time
from threading import Lock

class ShowProcDataThread(QThread):
    def __init__(self, lock_gather_info, lock_final_data, lock_pub_info):
        super().__init__()
        self.lock_gather_info = lock_gather_info
        self.lock_final_data = lock_final_data
        self.lock_pub_info = lock_pub_info
        self._running = True

    def run(self):
        while self._running:
            time.sleep(1)
            process_data.run_proc_processor(self.lock_gather_info, self.lock_final_data, self.lock_pub_info)

    def stop(self):
        self._running = False

class ShowMemDataThread(QThread):
    def __init__(self, lock_gather_info, lock_final_data, lock_pub_info):
        super().__init__()
        self.lock_gather_info = lock_gather_info
        self.lock_final_data = lock_final_data
        self.lock_pub_info = lock_pub_info
        self._running = True

    def run(self):
        
        while self._running:
            time.sleep(0.1)
            process_data.run_mem_processor(self.lock_gather_info, self.lock_final_data, self.lock_pub_info)

    def stop(self):
        self._running = False


class ProcDataThread(QThread):
    def __init__(self, lock_gather_info, lock_pid):
        super().__init__()
        self.lock_gather_info = lock_gather_info
        self.lock_pid = lock_pid
        self._running = True

    def run(self):
        while self._running:
            #print("here")
            time.sleep(0.1)
            data_gather.gather_proc_data(self.lock_gather_info, self.lock_pid)
            
            

    def stop(self):
        self._running = False


class MemDataThread(QThread):
    def __init__(self, lock_gather_info, lock_pid):
        super().__init__()
        self.lock_gather_info = lock_gather_info
        self.lock_pid = lock_pid
        self._running = True

    def run(self):
        
        while self._running:
            time.sleep(0.1)
            data_gather.gather_mem_data(self.lock_gather_info, self.lock_pid)

    def stop(self):
        self._running = False

if __name__ == "__main__":

    lock_gather_info = Lock()
    lock_PID = Lock()
    lock_final_data = Lock()
    lock_pub_info = Lock()

    proc_thread = ProcDataThread(lock_gather_info, lock_PID)
    ram_thread = MemDataThread(lock_gather_info, lock_PID)
    proc_processor_thread = ShowProcDataThread(lock_gather_info, lock_final_data, lock_pub_info)
    ram_processor_thread = ShowMemDataThread(lock_gather_info, lock_final_data, lock_pub_info)

    proc_thread.start()
    ram_thread.start()
    proc_processor_thread.start()
    ram_processor_thread.start()

    time.sleep(5)

    proc_thread.stop()
    ram_thread.stop()
    proc_processor_thread.stop()
    ram_processor_thread.stop()

    proc_thread.wait()
    ram_thread.wait()
    proc_processor_thread.wait()
    ram_processor_thread.wait()

    print("Threads stopped.")
