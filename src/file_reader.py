import os
import re
import struct
import time
import fcntl

PROC_DIR = "/proc"

def get_disk_usage(mount_point):
    stat = os.statvfs(mount_point)
    total = stat.f_frsize * stat.f_blocks
    free = stat.f_frsize * stat.f_bfree
    used = total - free
    return used

def read_disk_mount_point():
    mount_map = {}
    with open('/proc/mounts', 'r') as f:
        for line in f:
            parts = line.split()
            device = parts[0].removeprefix('/dev/')
            mount_point = parts[1]
            mount_map[device] = mount_point
        return mount_map

def read_proc_data(file):

    path = os.path.join(PROC_DIR, file)
    try:
        with open(path, 'r') as f:
            data = f.readlines()
            
    except IOError:
        # Skip if the file can't be read (e.g., process has exited)
        return
    return data

def get_numbers_list(text) -> list[float]:
    match = re.findall(r'\d+(?:\.\d+)?', text)
    if match:
        match = [float(i) if '.' in i else int(i) for i in match]
        return match

#Transform each line in a vector position
def read_proc_file(pid, file)->list[str]:
    path = os.path.join(PROC_DIR, pid, file)
    try:
        with open(path, 'r') as f:
            data = f.readlines()

    except IOError:
        return
    return data

EVENT_FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)
file = "/dev/input/event3"
device = open(file, 'rb')

# Set non-blocking mode
fd = device.fileno()
flags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

def get_mounted_fs_info():
    fs_info = []
    with open("/proc/mounts", "r") as f:
        for line in f:
            parts = line.split()
            dev = os.path.basename(parts[0])
            fstype = parts[0], parts[2]
            fs_info.append(fstype)
            #print(fstype)
    return fs_info

def read_binary_file(event_path):
    count = 0
    while True:
        try:
            data = device.read(EVENT_SIZE)
            if not data or len(data) < EVENT_SIZE:
                break

            tv_sec, tv_usec, ev_type, code, value = struct.unpack(EVENT_FORMAT, data)

            if ev_type == 1:# Event is a keypress (others include scroll, mouse, joystick)
                #print(f"Key event - Code: {code}, Value: {value}")
                count+=1

        except BlockingIOError:
            break  # No data left in the buffer

    return count
    
def read_file(path:str) -> list[str]:
    try:
        with open(path, 'r') as f:
            data = f.readlines()

    except IOError:
        return
    return data

def read_file(path)->list[str]:
    try:
        with open(path, 'r') as f:
            data = f.readlines()
    except IOError:
        return
    return data