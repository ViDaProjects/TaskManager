import os
import re
import time
import src.file_reader as file_reader
import src.data_classes as data_classes
import copy
from src.disk_info import DiskGather
from src.internet_info import NetGather

IO_DIR = "ioports"
SYS_CLASS_INPUT_DIR = "/sys/class/input"
DEV_INPUT_DIR = "/dev/input"

class IOMiner:

    def __init__(self):
        self.lock_gather_io = None

    def read_io_names(self):
        '''Returns a tuple for each device with the name of the device and the id number that represents it'''
        devices = []
        for file in os.listdir(SYS_CLASS_INPUT_DIR):
            if "input" in file:
                name = file_reader.read_file(SYS_CLASS_INPUT_DIR + "/" + file + "/name")[0]
                devices.append((name, file[-1]))
                #print(file)
                #print(name, end = "\n\n")
        #data = file_reader.read_proc_data(SYS_CLASS_INPUT_DIR)
        return devices
    
    def read_keyboard_press(self, id):
        '''Returns key_press count since last count'''
        dir = DEV_INPUT_DIR + "/event" + str(id)
        count = file_reader.read_binary_file(dir)
        print(count)

    def read_io_ports(self) -> tuple[list[str], list[str]]:
        io_data = file_reader.read_proc_data(IO_DIR)

        ports = []
        names = []

        for line in io_data:
            line = line.strip()
            ports.append(line[0:9])
            names.append(line[12:])
            #print(line[0:9], end=" ")
            #print(line[12:])

        return ports, names
    
def keyboard_kinda_broken():
    test = IOMiner()
    #test.read_io_ports()

    devices = test.read_io_names()
    
    keyboard_devices = [item for item in devices if 'keyboard' in item[0].lower()]

    keyboards_ids = []
    for i in keyboard_devices:
        keyboard_name, keyboard_id = i
        keyboards_ids.append(keyboard_id)
    
    
    
    # Loop that should be called periodically to extract all data and update the buffer
    while True:
        
        key_count = 0
        for i in keyboard_devices:
            key_count = test.read_keyboard_press(i)
        time.sleep(2)

disk_gatherer = DiskGather()
net_gatherer = NetGather()

class PublisherIOData:

    def __init__(self, pub_info_lock):
        self.pub_info_lock = pub_info_lock

    def gather_io_data(self):
        
        disk_info = disk_gatherer.get_disk_info()
        net_info = net_gatherer.get_net_info()

        pub_data = data_classes.GatherDataPub(net_info, disk_info)

        with self.pub_info_lock:
            data_classes.set_io_raw(copy.deepcopy(pub_data))

if __name__ == "__main__":
    a = PublisherIOData(1)
    a.gather_io_data()
