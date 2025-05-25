from PySide6.QtCore import QThread
import data_gather
import time

class ProcDataThread(QThread):
    def __init__(self, lock_gather_info, lock_pid):
        super().__init__()
        self.lock_gather_info = lock_gather_info
        self.lock_pid = lock_pid
        self._running = True

    def run(self):
        while self._running:
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
            data_gather.gather_mem_data(self.lock_gather_info, self.lock_pid)

    def stop(self):
        self._running = False


if __name__ == "__main__":
    from threading import Lock

    lock_gather_info = Lock()
    lock_PID = Lock()

    proc_thread = ProcDataThread(lock_gather_info, lock_PID)
    ram_thread = MemDataThread(lock_gather_info, lock_PID)

    proc_thread.start()
    ram_thread.start()

    time.sleep(5)

    proc_thread.stop()
    ram_thread.stop()

    proc_thread.wait()
    ram_thread.wait()

    print("Threads stopped.")
