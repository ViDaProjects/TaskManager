import threading

import list_names



def run_gatherer(lock_gather_info, lock_pid):
    
    proc_thread = threading.Thread(target=list_names.gather_proc_data, args=(lock_gather_info, lock_pid))
    proc_thread.start()

    ram_thread = threading.Thread(target=list_names.gather_mem_data, args=(lock_gather_info, lock_pid))
    ram_thread.start()

if __name__ == "__main__":

    lock_gather_info = threading.Lock()
    lock_PID = threading.Lock()

    run_gatherer(lock_gather_info, lock_PID)