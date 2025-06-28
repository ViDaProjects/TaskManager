import os
import file_reader
import data_classes


def disk_total_read(disk_path):
    #print(disk_path + "/stat")
    stat = file_reader.read_file(disk_path + "/stat")
    stat = file_reader.get_numbers_list(stat[0])
    
    data = data_classes.DiskInfo(0, 0, 0, 0, 0, 0)

    data.total_read = stat[0] # Amount of data read (how many requests)
    data.sectors_read = stat[2]# Number of 512b segments read
    data.duration_not_read = stat[3]# Time where it didn't read because disk was busy
    data.total_write = stat[4]
    data.total_write = stat[6]
    data.duration_not_write = stat[7]
    data.in_flight = stat[8] # Number of active read/write operations, When copying multiple files it can act weird and not register

    return data

def get_disk_list():
    data = []
    for disk in os.listdir("/sys/block"):
        device_path = f"/sys/block/{disk}/device"
        model_path = os.path.join(device_path, "model")
        vendor_path = os.path.join(device_path, "vendor")
        device_path = f"/sys/block/{disk}"
        try:
            with open(model_path) as m, open(vendor_path) as v:
                data.append((m.read().strip(), v.read().strip(), "/dev/"+disk, device_path))
        except FileNotFoundError:
            # Some devices like loopback or ram might not have model/vendor
            pass
    return data

if __name__ == "__main__":
    data = get_disk_list()
    #print(data[0][3])
    data = disk_total_read(data[0][3])
    print(data)