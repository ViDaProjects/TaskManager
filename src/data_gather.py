import os
import re
import time
import threading
from src.data_classes import ProcessData, SystemData, ProcRam
#from data_classes import GATHERED_DATA, PID
import src.data_classes as data_classes
import copy

PROC_DIR = "/proc"
COMM_FILE = "comm"
SCHED_FILE = "sched"
STAT_FILE = "stat"
SMAPS_FILE = "smaps"
STATM_FILE = "statm"
TASK_DIR = "task"



class DataMiner:

    def __init__(self):
        self.lock_gather_info = None
        self.lock_pid = None

    def is_numeric(self, s):
        return s.isdigit()


    # Gets numbers from text and returns as int
    def get_numbers_list(self, text) -> list[float]:
        match = re.findall(r'\d+(?:\.\d+)?', text)
        if match:
            match = [float(i) if '.' in i else int(i) for i in match]
            return match

    #Transform each line in a vector position
    def read_proc_file(self, pid, file)->list[str]:
        path = os.path.join(PROC_DIR, pid, file)
        try:
            with open(path, 'r') as f:
                data = f.readlines()

        except IOError:
            
            return
        return data

    def read_proc_mem(self):
        t = time.time()

        with self.lock_pid:
            pid = copy.deepcopy(data_classes.get_PID())

        statm = self.read_proc_file(pid, STATM_FILE)

        if not statm:
            with self.lock_gather_info:
                data_classes.set_RAM_INFO(None)
            #print("Ram data not gathered, process killed or permission denied")
            return
        
        ram_granular_data = self.get_numbers_list(statm[0])

        virtual_pages = ram_granular_data[0]

        real_pages_share = ram_granular_data[1]

        shared_pages = ram_granular_data[2]

        text_pages = ram_granular_data[3]

        data_stack_pages = ram_granular_data[5]

        dirty_pages = ram_granular_data[6]

        smaps = self.read_proc_file(str(pid), SMAPS_FILE)            

        if not smaps:
            with self.lock_gather_info:
                data_classes.set_RAM_INFO(ProcRam(virtual_pages, real_pages_share, shared_pages, text_pages, data_stack_pages, dirty_pages, -1, t))
            print("Ram data incomplete, permission denied")
            return

        in_swap_kb = 0
        for i in range(len(smaps)):
            
            found = re.search(r'([0-9a-f]{12}-[0-9a-f]{12})', smaps[i])
            if found:
                in_swap_kb += self.get_numbers_list(smaps[i+20])[0]

        with self.lock_gather_info:
            data_classes.set_RAM_INFO(ProcRam(virtual_pages, real_pages_share, shared_pages, text_pages, data_stack_pages, dirty_pages, in_swap_kb, t))

    # Reading proc file outside of pid
    def read_proc_data(self, file):

        path = os.path.join(PROC_DIR, file)
        try:
            with open(path, 'r') as f:
                data = f.readlines()
                
        except IOError:
            # Skip if the file can't be read (e.g., process has exited)
            return
        return data
    
    def get_proc_available_data(self, pid):

        thread_path = os.path.join(PROC_DIR, pid, TASK_DIR)

        try:
            lst = os.listdir(thread_path) # your directory path
            thread_count_proc = len(lst)
        except:
            thread_count_proc = 0

        name = self.read_proc_file(pid, "comm")# This dir has only proc name
        
        if not name:
            return
        name = name[0]

        sched = self.read_proc_file(pid, SCHED_FILE)

        if not sched:
            return
        
        # Static priority data
        prio = self.get_numbers_list(sched[23])[0] # Retorna lista de int

        # Task cpu runtime data WRONG
        cpu_runtime = self.get_numbers_list(sched[4])[0] # Probably wrong data

        stat = self.read_proc_file(pid, STAT_FILE)
        
        if not stat:
            return

        stat = stat[0].split() # stat is a single line with values concatenated
        
        user_cpu_time = int(stat[13])
        system_cpu_time = int(stat[14]) # syscalls and admin runningg

        proc_data = ProcessData(name, pid, thread_count_proc, prio, user_cpu_time, system_cpu_time)

        return proc_data

    def get_system_available_data(self):
        cpu_info = self.read_proc_data("stat")[0]
        cpu_info = self.get_numbers_list(cpu_info)

        cpu_runtime = sum(cpu_info)
        cpu_active_time = cpu_runtime - cpu_info[3] - cpu_info[4] # Positions for cpu idle and iowait
        
        ram_info = self.read_proc_data("meminfo")

        mem_total = self.get_numbers_list(ram_info[0])[0]
        mem_unused = self.get_numbers_list(ram_info[1])[0]
        mem_available = self.get_numbers_list(ram_info[2])[0]


        swap_total = self.get_numbers_list(ram_info[14])[0]
        swap_free = self.get_numbers_list(ram_info[15])[0]

        t = time.time()

        return cpu_runtime, cpu_active_time, mem_total, mem_unused, mem_available, swap_total, swap_free, t

    def get_proc_data(self):

            cpu_runtime, cpu_active_time, mem_total, mem_unused, mem_available, swap_total, swap_free, t = self.get_system_available_data()

            sys_data = SystemData(cpu_runtime, cpu_active_time, mem_total, mem_unused, mem_available, swap_total, swap_free, 0, 0, [], t)
            
            proc_count = thread_count = 0

            for file in os.listdir(PROC_DIR):
                if self.is_numeric(file):

                    proc = self.get_proc_available_data(file)

                    if not proc:
                        continue

                    proc_count += 1

                    thread_count += proc.thread_count_proc

                    sys_data.process.append(proc)
            
            sys_data.proc_count = proc_count
            sys_data.thread_count_total = thread_count
            
            if not self.lock_gather_info:
                return
            with self.lock_gather_info:
                
                data_classes.set_GATHERED_DATA(copy.deepcopy(sys_data))


            return 0
    
    def set_locks(self, lock_gather_info, lock_pid):
        self.lock_gather_info = lock_gather_info
        self.lock_pid = lock_pid

var = DataMiner()


def gather_proc_data(lock_gather_info, lock_pid):

    var.set_locks(lock_gather_info, lock_pid) # Lock_pid is not used for systemwide gather info, here cause removing is a hassle
    var.get_proc_data()

def gather_mem_data(lock_gather_info, lock_pid):

    var.set_locks(lock_gather_info, lock_pid)

    var.read_proc_mem()

if __name__ == "__main__":
    lock_gather_info = threading.Lock()
    lock_pid = threading.Lock()
    gather_proc_data(lock_gather_info, lock_pid)
    #gather_mem_data(lock_gather_info, lock_pid)
