import os
import re
import time
import file_reader

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
            print(line[0:9], end=" ")
            print(line[12:])

        return ports, names

if __name__ == "__main__":
    test = IOMiner()
    #test.read_io_ports()

    devices = test.read_io_names()
    
    keyboard_devices = [item for item in devices if 'keyboard' in item[0].lower()]

    print(keyboard_devices)
    keyboard_name, keyboard_id = keyboard_devices[0]
    
    
    
    
    # Loop that should be called periodically to extract all data and update the buffer
    while True:
        
        key_count = test.read_keyboard_press(keyboard_id)
        time.sleep(2)
        
