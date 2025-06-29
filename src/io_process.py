import data_classes
import copy
import time

def process_disk(data: data_classes.DiskInfo, old_data: data_classes.DiskInfo):
    
    data = data[0]
    old_data = old_data[0]

    processed_disk = data_classes.ShowDiscInfo(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    processed_disk.model = data.model
    processed_disk.vendor = data.vendor

    processed_disk.partitions = []

    for partition in data.partitions:
        processed_disk.partitions.append(data_classes.ShowPartitionInfo(partition.name, partition.mount_point, partition.used, partition.size, partition.used / partition.size))

    processed_disk.read_speed = (data.total_read - old_data.total_read) / 2
    processed_disk.sectors_read_speed = (data.sectors_read - old_data.sectors_read) / 2
    processed_disk.time_waiting_read = (data.duration_not_read - old_data.duration_not_read) / 2
    
    processed_disk.write_speed = (data.total_write - old_data.total_write) / 2
    processed_disk.sectors_write_speed = (data.sectors_write - old_data.sectors_write) / 2
    processed_disk.time_waiting_write = (data.duration_not_write - old_data.duration_not_write) / 2

    processed_disk.uncompleted_requests = data.in_flight

    #print(processed_disk)
    return processed_disk

class ProcessIOData:

    def __init__(self, sub_info_lock, pub_info_lock):
        self.sub_info_lock = sub_info_lock
        self.pub_info_lock = pub_info_lock

    def process_io_data(self):

        with self.sub_info_lock:
            io_old = copy.deepcopy(data_classes.get_io_raw())
        
        if not io_old:
            time.sleep(0.1)
            return
        #print(io_old)
        #io_old = io_old[0]
        

        time.sleep(0.5)

        with self.sub_info_lock:
            io_raw = copy.deepcopy(data_classes.get_io_raw())
            # AQUI LÊ OS DADOS
        
        processed_disk = process_disk(io_raw.disk_info, io_old.disk_info)

        processed_io = data_classes.ShowIOData(processed_disk)

        with self.pub_info_lock:
            data_classes.set_show_io_data(copy.deepcopy(processed_io))

