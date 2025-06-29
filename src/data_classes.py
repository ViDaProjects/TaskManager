
from dataclasses import dataclass

class DataBuffers:

    def __init__(self):
        self.GATHERED_DATA = None

        self.RAM_INFO = None

        self.PID = str("20403")

        self.SHOW_SYSTEM_DATA = None

        self.SHOW_RAM_DATA = None

    def GATHERED_set(self, data):
        self.GATHERED_DATA = data
    
    def GATHERED_get(self):
        return self.GATHERED_DATA
    
    def RAM_INFO_set(self, data):
        self.RAM_INFO = data
    
    def RAM_INFO_get(self):
        return self.RAM_INFO

    def PID_set(self, data):
        self.PID = data
    
    def PID_get(self):
        return self.PID
    
    def SHOW_SYSTEM_DATA_set(self, data):
        self.SHOW_SYSTEM_DATA = data
    
    def SHOW_SYSTEM_DATA_get(self):
        return self.SHOW_SYSTEM_DATA
    
    def SHOW_RAM_DATA_set(self, data):
        self.SHOW_RAM_DATA = data

    def SHOW_RAM_DATA_get(self):
        return self.SHOW_RAM_DATA


def set_GATHERED_DATA(data):
    buffer.GATHERED_set(data)

def get_GATHERED_DATA():
    return buffer.GATHERED_get()

def set_RAM_INFO(data):
    buffer.RAM_INFO_set(data)

def get_RAM_INFO():
    return buffer.RAM_INFO_get()

def set_PID(data):
    buffer.PID_set(data)

def get_PID():
    return buffer.PID_get()

def set_SHOW_SYSTEM_DATA(data):
    buffer.SHOW_SYSTEM_DATA_set(data)

def get_SHOW_SYSTEM_DATA():
    return buffer.SHOW_SYSTEM_DATA_get()

def set_SHOW_RAM_DATA(data):
    buffer.SHOW_RAM_DATA_set(data)

def get_SHOW_RAM_DATA():
    return buffer.SHOW_RAM_DATA_get()

@dataclass
class ProcessData:
    name: str
    pid: str
    thread_count_proc: float
    prio: float
    user_cpu_time: float
    system_cpu_time: float

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
    time: float

@dataclass
class ProcRam:
    virtual_pages: float
    real_pages_share: float
    shared_pages: float
    text_pages: float
    data_stack_pages: float
    dirty_pages: float
    in_swap_kb: float
    time:float

@dataclass
class ShowProcessData:
    name: str
    pid: str
    thread_count_proc: float
    prio: float
    prio_type: str
    cpu_usage: float

@dataclass
class ShowSystemData:
    cpu_usage: float 
    mem_total: float
    mem_used: float
    mem_used_percent: float
    swap_used: float
    swap_total: float
    swap_used_percent: float
    proc_count_total: float
    thread_count_total: float
    process: list[ShowProcessData]

@dataclass
class ShowRamData:
    virtual_size_kb: float
    data_stack_size_kb: float
    real_size_share_kb: float
    real_size_not_share_kb: float
    dirty_percentage: float
    swap_percentage: float

@dataclass
class PartitionInfo:
    name: str
    mount_point: str
    used: float
    size: float

@dataclass
class DiskInfo:
    model: str
    vendor: str

    partitions: list[PartitionInfo] # List contains (partition_name, filetype, partition_size, mount_location)

    total_read: float
    sectors_read: float
    duration_not_read: float
    total_write: float
    total_write: float
    duration_not_write: float
    in_flight: float

    used: float
    total_size: float

@dataclass 
class InternetInfo:
    name: str
    # Blocks for in and out info
    in_bytes: float
    in_packets: float
    in_errs: float
    in_drop: float

    out_bytes: float
    out_packets: float
    out_errs: float
    out_drop: float

buffer = DataBuffers()
