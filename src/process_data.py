import src.data_classes as data_classes
import copy
import time

class DataProcesser:

    def __init__(self, lock_gather_info, lock_final_data):
        self.lock_gather_info = lock_gather_info
        self.lock_final_data = lock_final_data

    def proc_processor(self):

        with self.lock_gather_info:
            for_percent = copy.deepcopy(data_classes.GATHERED_DATA)

        time.sleep(1)

        with self.lock_gather_info:
            proc_data = copy.deepcopy(data_classes.GATHERED_DATA)
        proc_data = for_percent = data_classes.SystemData()

        
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

        names = len(for_percent.process)*[]
        for i in range(len(for_percent.process)):
            names[i] = for_percent.process[i]


        for i in proc_data.process:
            
            if i.name not in names:
                continue

            name = i.name

            thread_count_proc = i.thread_count_proc

            prio = i.prio
            prio_type = "rt"
            if prio >= 100:
                prio -= 120
                prio_type = "nice"

            proc_cpu_time = i.system_cpu_time+i.user_cpu_time
            old_cpu_time = 0
            for j in for_percent.process:
                if i.name == j.name:
                    old_cpu_time = j.system_cpu_time + j.user_cpu_time

            if old_cpu_time == 0:
                print("old_cpu_time not working")

            proc_cpu_usage = 100 * (proc_cpu_time - old_cpu_time) / cpu_usage

            cpu_usage_proc = 100 * (i.system_cpu_time+i.user_cpu_time) / proc_data.cpu_active_time

            proc = data_classes.ShowProcessData(name, thread_count_proc, prio, prio_type, cpu_usage_proc)

            proc_data.process.append(proc)

        # Lock com deepcopy dentro

    def ram_processor(self):
        with self.lock_gather_info:
            ram_data = copy.deepcopy(data_classes.RAM_INFO)

        ram_data = data_classes.ProcRam()

        virtual_size = ram_data.virtual_size
        used = ram_data.real_mem_share
        shared_from_others = ram_data.real_mem_share - ram_data.real_mem_not_share
        clean_percent = 100 * (used - ram_data.clean_shared_size) / used
        in_swap_percent = 100 * ram_data.in_swap / used
