import data_classes
import copy
import time

def process_disk(data: list[data_classes.DiskInfo], old_data: list[data_classes.DiskInfo]):
    if len(data) != len(old_data):
        return
    pub_data = []

    loop_data = data
    old_loop_data = old_data

    for i in range(len(loop_data)):
        data = loop_data[i]
        old_data = old_loop_data[i]

        processed_disk = data_classes.ShowDiscInfo(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        processed_disk.model = data.model
        processed_disk.vendor = data.vendor

        processed_disk.partitions = []

        for partition in data.partitions:
            processed_disk.partitions.append(data_classes.ShowPartitionInfo(partition.name, partition.mount_point, partition.used, partition.size, 100 * partition.used / partition.size))

        processed_disk.read_speed = (data.total_read - old_data.total_read) / 2
        processed_disk.sectors_read_speed = (data.sectors_read - old_data.sectors_read) / 2
        processed_disk.time_waiting_read = (data.duration_not_read - old_data.duration_not_read) / 2
        
        processed_disk.write_speed = (data.total_write - old_data.total_write) / 2
        processed_disk.sectors_write_speed = (data.sectors_write - old_data.sectors_write) / 2
        processed_disk.time_waiting_write = (data.duration_not_write - old_data.duration_not_write) / 2

        processed_disk.uncompleted_requests = data.in_flight
        
        pub_data.append(processed_disk)

    #print(processed_disk)
    #print(pub_data)
    return pub_data

def process_net(data: list[data_classes.InternetInfo], old_data: list[data_classes.InternetInfo]):
    if len(data) != len(old_data):
        return
    
    pub_data = []

    for i in range(len(data)):
        processed_device = data_classes.ShowInternetInfo(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        
        processed_device.name = data[i].name

        processed_device.in_speed = (data[i].in_bytes - old_data[i].in_bytes) / 2
        processed_device.in_packet_speed = (data[i].in_packets - old_data[i].in_packets) / 2
        processed_device.in_avg_packet_size = processed_device.in_speed - processed_device.in_packet_speed
        processed_device.in_err_rate = (data[i].in_errs - old_data[i].in_errs) / 2
        processed_device.in_drop_rate = (data[i].in_drop - old_data[i].in_drop) / 2

        processed_device.out_speed = (data[i].out_bytes - old_data[i].out_bytes) / 2
        processed_device.out_packet_speed = (data[i].out_packets - old_data[i].out_packets) / 2
        processed_device.out_avg_packet_size = processed_device.out_speed - processed_device.out_packet_speed
        processed_device.out_err_rate = (data[i].out_errs - old_data[i].out_errs) / 2
        processed_device.out_drop_rate = (data[i].out_drop - old_data[i].out_drop) / 2
        
        pub_data.append(processed_device)

    #print(pub_data)
    return pub_data

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

        time.sleep(0.5)

        with self.sub_info_lock:
            io_raw = copy.deepcopy(data_classes.get_io_raw())
            # AQUI LÊ OS DADOS
        
        processed_disk = process_disk(io_raw.disk_info, io_old.disk_info)
        processed_net = process_net(io_raw.internet_info, io_old.internet_info)

        processed_io = data_classes.ShowIOData(processed_disk, processed_net)
        
        #print(processed_io)
        with self.pub_info_lock:
            data_classes.set_show_io_data(copy.deepcopy(processed_io))

