import data_classes
import copy

class DataProcesser:

    def __init__(self, lock_gather_info, lock_final_data):
        self.lock_gather_info = lock_gather_info
        self.lock_final_data = lock_final_data

    def proc_processor(self):
        with self.lock_gather_info:
            proc_data = copy.deepcopy(data_classes.GATHERED_DATA)

        cpu_usage = 100 * proc_data.cpu_active_time / proc_data.cpu_runtime
        mem_total = proc_data.mem_total
        mem_unused = proc_data.mem_unused
        mem_available = proc_data.mem_available
        mem_used_percent = 100 * (mem_total - mem_unused) / mem_total
        mem_reserved = mem_unused - mem_available # Verificar se está negativo (significa que David troquei na minha cabeça)
        swap_total = proc_data.swap_total
        swap_free = proc_data.swap_free
        swap_used_percent = 100 * (swap_total - swap_free) / swap_total
        proc_count_total = proc_data.proc_count
        thread_count_total = proc_data.thread_count_total
        time = proc_data.time

        show_system_data = data_classes.ShowSystemData(cpu_usage, mem_total, mem_used_percent, swap_total, swap_used_percent, proc_count_total, thread_count_total, [data_classes.ShowProcessData], time)

        for i in proc_data.process:
            

            name = i.name        proc_data = data_classes.SystemData()

            thread_count_proc = i.thread_count_proc

            prio = i.prio
            prio_type = "rt"
            if prio >= 100:
                prio -= 120
                prio_type = "nice"

            cpu_usage = 100 * (i.system_cpu_time+i.user_cpu_time) / proc_data.cpu_active_time

            proc = data_classes.ShowProcessData(name, thread_count_proc, prio, prio_type, cpu_usage)

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