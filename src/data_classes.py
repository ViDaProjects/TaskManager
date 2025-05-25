
from dataclasses import dataclass

'''Both gathered_data and ram_info use the same lock because simplicity'''
global GATHERED_DATA
GATHERED_DATA = None

global RAM_INFO
RAM_INFO = None

global PID
PID = 0


@dataclass
class ProcessData:
    name: str
    thread_count_proc: float
    prio: float
    cpu_runtime: float
    cpu_active_time: float

@dataclass
class SystemData:
    cpu_runtime: float
    cpu_active_time: float 
    mem_total: float
    mem_unused: float
    mem_available: float
    swap_total: float
    swap_free: float
    proc_count: float
    thread_count_total: float
    process: list[ProcessData]

@dataclass
class ProcRam:
    virtal_size: float
    real_mem_share: float
    real_mem_not_share: float
    clean_shared_size: float
    clean_private_size: float
    in_swap: float