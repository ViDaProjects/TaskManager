
from dataclasses import dataclass

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