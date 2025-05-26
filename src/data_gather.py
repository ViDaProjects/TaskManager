import os
import re
import time
import threading
from src.data_classes import ProcessData, SystemData, ProcRam
from src.data_classes import GATHERED_DATA, PID
import copy

PROC_DIR = "/proc"
COMM_FILE = "comm"
SCHED_FILE = "sched"
STAT_FILE = "stat"
SMAPS_FILE = "smaps"



class DataMiner:

    def __init__(self, lock_gather_info, lock_pid):
        self.lock_gather_info = lock_gather_info
        self.lock_pid = lock_pid

    def is_numeric(self, s):
        return s.isdigit()


    # Gets numbers from text and returns as int
    def get_numbers_list(self, text) -> list[float]:
        match = re.findall(r'\d+(?:\.\d+)?', text)
        if match:
            match = [float(i) if '.' in i else int(i) for i in match]
            return match

    def read_proc_file(self, pid, file)->list[str]:
        path = os.path.join(PROC_DIR, pid, file)
        try:
            with open(path, 'r') as f:
                data = f.readlines()
                
        except IOError:
            # Skip if the file can't be read (e.g., process has exited)
            return
        return data

    def read_proc_mem(self):
        print("Ram data not gathered, process killed or permission denied")
        with self.lock_pid:
            smaps = self.read_proc_file(str(PID), SMAPS_FILE)
            

        if not smaps:
            with self.lock_gather_info:
                RAM_INFO = None
            print("Ram data not gathered, process killed or permission denied")
            return

        virtual_size = real_mem_share = real_mem_not_share = clean_shared_size = clean_private_size = in_swap = 0
        for i in range(len(smaps)):
            
            found = re.search(r'([0-9a-f]{12}-[0-9a-f]{12})', smaps[i])
            if found:
                virtual_size += self.get_numbers_list(smaps[i+1])[0]
                real_mem_share += self.get_numbers_list(smaps[i+4])[0]
                real_mem_not_share += self.get_numbers_list(smaps[i+5])[0]
                clean_shared_size += self.get_numbers_list(smaps[i+7])[0]
                clean_private_size += self.get_numbers_list(smaps[i+9])[0]
                in_swap += self.get_numbers_list(smaps[i+20])[0]
                
        t = time.time()
        with self.lock_gather_info:
            if found:
                RAM_INFO = ProcRam(virtual_size, real_mem_share, real_mem_not_share, clean_shared_size, clean_private_size, in_swap, t)
        print("ram data published")

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


    def get_proc_data(self):

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

            sys_data = SystemData(cpu_runtime, cpu_active_time, mem_total, mem_unused, mem_available, swap_total, swap_free, 0, 0, [], t)

            proc_count = thread_count = 0
            for file in os.listdir(PROC_DIR):
                if self.is_numeric(file):
                    proc_count+=1

                    path = os.path.join(PROC_DIR, file, "task")

                    thread_count_proc = 1
                    try:
                        threads = os.listdir(path)
                        thread_count += len(threads)
                        thread_count_proc = len(threads)
                    except (FileNotFoundError, PermissionError):
                        thread_count_proc = 0
                        continue
                    name = self.read_proc_file(file, "comm")# This dir has only proc name
                    
                    if not name:
                        continue
                    name = name[0]
                    #print(f"PID: {file}\tName: {name}")

                    sched = self.read_proc_file(file, SCHED_FILE)

                    if not sched:
                        continue
                    
                    # Static priority data
                    prio = self.get_numbers_list(sched[23])[0] # Retorna lista de int
                    
                    #print("PRIO: " + prio_type + "\t" + str(prio))

                    # Task cpu runtime data
                    cpu_runtime = self.get_numbers_list(sched[4])[0] # Probably wrong data
                    #print(cpu_runtime)

                    stat = self.read_proc_file(file, STAT_FILE)
                    
                    if not stat:
                        continue


                    stat = stat[0].split() # stat is a single line with values concatenated

                    user_cpu_time = int(stat[13])
                    system_cpu_time = int(stat[14]) # syscalls and admin runningg

                    proc_data = ProcessData(name, file, thread_count_proc, prio, user_cpu_time, system_cpu_time)

                    sys_data.process.append(proc_data)
            
            sys_data.proc_count = proc_count
            sys_data.thread_count_total = thread_count
            with self.lock_gather_info:
                GATHERED_DATA = copy.deepcopy(sys_data)
            print("proc data published")

            return 0

def gather_proc_data(lock_gather_info, lock_pid):
    var = DataMiner(lock_gather_info, lock_pid)
    
    var.get_proc_data()

def gather_mem_data(lock_gather_info, lock_pid):
    var = DataMiner(lock_gather_info, lock_pid)
    
    var.read_proc_mem()

if __name__ == "__main__":
    lock_gather_info = threading.Lock()
    lock_pid = threading.Lock()
    #gather_proc_data(lock_gather_info, lock_pid)
    gather_mem_data(lock_gather_info, lock_pid)
