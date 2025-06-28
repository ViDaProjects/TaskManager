import os
import file_reader
import data_classes

def get_partition_size_bytes(disk, part):
    path = f"/sys/block/{disk}/{part}/size"
    try:
        with open(path, 'r') as f:
            sectors = int(f.read().strip())
            return sectors * 512  # bytes
    except FileNotFoundError:
        return None

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
        
        # Some files with some info
        dev_path = f"/sys/block/{disk}"
        device_path = os.path.join(dev_path, "device")
        model_path = os.path.join(device_path, "model")
        vendor_path = os.path.join(device_path, "vendor")

        model = vendor = None

        # Getting partition data, mountpoint, names, etc
        partitions = [
            entry for entry in os.listdir(dev_path)
            if entry.startswith(disk) and os.path.exists(os.path.join(dev_path, entry))
        ]
        for i in range(len(partitions)):
            partitions[i] = partitions[i], get_partition_size_bytes(disk, partitions[i])
        
        # Gets partition filetype info and mound location for all file shenanigans
        partition_types = file_reader.get_mounted_fs_info()

        # INNER JOIN THE PARTITION NAME, SIZE AND FILETYPE, THIS IS NOT READABLE CODE
        partition_types_dict = {
            dev.removeprefix('/dev/'): fstype
            for dev, fstype in partition_types
            if dev.startswith('/dev/')
        }

        partitions_dict = dict(partitions)

        partitions = [
            (dev, partition_types_dict[dev], partitions_dict[dev])
            for dev in partition_types_dict
            if dev in partitions_dict
        ]

        mount_points = file_reader.read_disk_mount_point()
        
        # Shennagigans to allow adding the mounting points to the tuple
        old_partitions = partitions.copy()
        partitions = []
        for partition in old_partitions:
            partitions.append(partition + (mount_points[partition[0]],))

        used = 0
        for partition in partitions:
            used += file_reader.get_disk_usage(partition[3])

        # Try to get model name for sda and usb devices, does not work for nvme
        try:
            with open(model_path) as f:
                model = f.read().strip()
        except FileNotFoundError:
            pass  # model may not exist (e.g., for loopback or some NVMe)

        # Try vendor
        try:
            with open(vendor_path) as f:
                vendor = f.read().strip()
        except FileNotFoundError:
            pass  # vendor may not exist

        # Try nvme info if missing
        if model is None and disk.startswith("nvme"):
            # This is the common NVMe path: /sys/block/nvme0n1/device/...
            nvme_base = os.path.join(device_path, "../")  # Go one level up to nvme0
            nvme_base = os.path.realpath(nvme_base)
            try:
                with open(os.path.join(nvme_base, "model")) as f:
                    model = f.read().strip()
            except FileNotFoundError:
                pass

            try:
                with open(os.path.join(nvme_base, "vendor")) as f:
                    vendor = f.read().strip()
            except FileNotFoundError:
                pass

        # Add disk info to return USE DATACLASS
        if model or vendor:
            data.append((model or "unknown", vendor or "unknown", "/dev/" + disk, dev_path, partitions))

    return data

if __name__ == "__main__":
    data = get_disk_list()
    
    for disk in data:
        print(disk)
        data = disk_total_read(disk[3])
        print(data)