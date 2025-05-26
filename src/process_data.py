import src.data_classes as data_classes
import copy
import time
import os
import ctypes
import threading

#from data_classes import SHOW_SYSTEM_DATA

class DataProcesser:

    def __init__(self):
        self.lock_gather_info = None
        self.lock_pub_info = None


    def proc_processor(self):

        if not self.lock_gather_info:
            return
        
        with self.lock_gather_info:
            for_percent = copy.deepcopy(data_classes.get_GATHERED_DATA())
        
        if for_percent is None:
            
            return
        
        time.sleep(0.4)

        with self.lock_gather_info:
            proc_data = copy.deepcopy(data_classes.get_GATHERED_DATA())

        
        cpu_active_delta = proc_data.cpu_active_time - for_percent.cpu_active_time

        cpu_runtime_delta = proc_data.cpu_runtime - for_percent.cpu_runtime

        cpu_usage = 100 * cpu_active_delta / cpu_runtime_delta
        mem_total = proc_data.mem_total
        mem_unused = proc_data.mem_unused
        mem_available = proc_data.mem_available
        mem_used = mem_total - mem_unused
        mem_used_percent = 100 * mem_used / mem_total
        mem_reserved = mem_unused - mem_available # Verificar se está negativo (significa que David troquei na minha cabeça)
        swap_total = proc_data.swap_total
        swap_free = proc_data.swap_free
        swap_used = swap_total - swap_free
        swap_used_percent = 100 * swap_used / swap_total
        proc_count_total = proc_data.proc_count
        thread_count_total = proc_data.thread_count_total

        show_system_data = data_classes.ShowSystemData(cpu_usage, mem_total// 1024, mem_used // 1024, mem_used_percent, swap_total// 1024, swap_used // 1024, swap_used_percent, proc_count_total, thread_count_total, [data_classes.ShowProcessData])

        names = []
        for i in range(len(for_percent.process)):
            names.append(for_percent.process[i].name)

        pub_info = data_classes.ShowSystemData(cpu_usage, mem_total, mem_used, mem_used_percent, swap_used, swap_total, swap_used_percent, proc_count_total, thread_count_total, [])

        proc_processed_list = []

        for i in proc_data.process:
            if i.name not in names:
                continue

            name = i.name
            pid = i.pid

            thread_count_proc = i.thread_count_proc

            prio = i.prio
            prio_type = "rt"
            if prio >= 100:
                prio -= 120
                prio_type = "nice"

            proc_cpu_time = i.system_cpu_time+i.user_cpu_time
            old_cpu_time = proc_cpu_time
            for j in for_percent.process:
                if i.name == j.name:
                    old_cpu_time = j.system_cpu_time + j.user_cpu_time

            proc_cpu_usage = 100 * (proc_cpu_time - old_cpu_time) / cpu_usage

            data = data_classes.ShowProcessData(name, pid, thread_count_proc, prio, prio_type, cpu_usage)

            pub_info.process.append(data)
        
        with self.lock_pub_info:
            data_classes.set_SHOW_SYSTEM_DATA(copy.deepcopy(pub_info))
        


    def ram_processor(self):
        if not self.lock_gather_info:
            return

        with self.lock_gather_info:
            ram_data = copy.deepcopy(data_classes.get_RAM_INFO())

        if ram_data is None:
            return

        libc = ctypes.CDLL("libc.so.6")
        getpagesize = libc.getpagesize
        getpagesize.restype = ctypes.c_int

        page_size = getpagesize()

        virtual_size_kb = (ram_data.virtual_pages * page_size) // 1024

        real_size_share_kb = (ram_data.shared_pages * page_size) // 1024
        
        shared_size_kb = (ram_data.shared_pages * page_size) // 1024

        text_size_kb = (ram_data.text_pages * page_size) // 1024

        data_stack_size_kb = (ram_data.data_stack_pages * page_size) // 1024
        
        dirty_size_kb = (ram_data.dirty_pages * page_size) // 1024

        in_swap_kb = ram_data.in_swap_kb

        real_size_not_share_kb = real_size_share_kb - shared_size_kb

        dirty_percentage = 100 * dirty_size_kb / real_size_share_kb
        swap_percentage = 100 * in_swap_kb / real_size_share_kb


        pub = data_classes.ShowRamData(virtual_size_kb, data_stack_size_kb, real_size_share_kb, real_size_not_share_kb, dirty_percentage, swap_percentage)

        with self.lock_pub_info:
            data_classes.set_SHOW_RAM_DATA(copy.deepcopy(pub))

    def set_locks(self, lock_gather_info, lock_pub_info):
        self.lock_pub_info = lock_pub_info
        self.lock_gather_info = lock_gather_info

var = DataProcesser()

def run_proc_processor(lock_gather_info, lock_pub_info):

    var.set_locks(lock_gather_info, lock_pub_info)
    
    var.proc_processor()

def run_mem_processor(lock_gather_info, lock_pub_info):
    var.set_locks(lock_gather_info, lock_pub_info)

    var.ram_processor()
