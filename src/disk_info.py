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

class DiskGather:

    def get_disk_info(self):
        data = []
        for disk in os.listdir("/sys/block"):

            disk_data = data_classes.DiskInfo(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

            # Some files with some info
            dev_path = f"/sys/block/{disk}"

            #disk_total_read(dev_path)
            stat = file_reader.read_file(dev_path + "/stat")
            stat = file_reader.get_numbers_list(stat[0])

            disk_data.total_read = stat[0] # Amount of data read (how many requests)
            disk_data.sectors_read = stat[2]# Number of 512b segments read
            disk_data.duration_not_read = stat[3]# Time where it didn't read because disk was busy
            disk_data.total_write = stat[4]
            disk_data.sectors_write = stat[6]
            disk_data.duration_not_write = stat[7]
            disk_data.in_flight = stat[8] # Number of active read/write operations, When copying multiple files it can act weird and not register


            device_path = os.path.join(dev_path, "device")
            model_path = os.path.join(device_path, "model")
            vendor_path = os.path.join(device_path, "vendor")

            model = vendor = None

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
            
            disk_data.model = model
            disk_data.vendor = vendor

            # Getting partition data, mountpoint, names, etc
            partitions = [
                [entry] for entry in os.listdir(dev_path)
                if entry.startswith(disk) and os.path.exists(os.path.join(dev_path, entry))
            ]
            if not partitions:
                continue
            for i in range(len(partitions)):
                partitions[i].append(get_partition_size_bytes(disk, partitions[i][0]))

            
            mount_points = file_reader.read_disk_mount_point()
            
            # Shennagigans to allow adding the mounting points to the tuple

            partition_data = []

            for partition in partitions:
                part_name = partition[0]
                if part_name in mount_points:
                    partition_usage = file_reader.get_disk_usage(mount_points[part_name])
                    partition.append(mount_points[partition[0]])
                    partition_data.append(data_classes.PartitionInfo(partition[0], partition[2], partition_usage / 1000 / 1000 / 1000, partition[1] / 1000 / 1000 / 1000))
                else:
                    # A partição não está montada — pode registrar como "não montada", ignorar, etc.
                    continue

            disk_data.partitions = partition_data.copy()
            data.append(disk_data)
        
        # Trocar esse return para colocar em um buffer de thread
        return data

if __name__ == "__main__":
    a = DiskGather()
    data = a.get_disk_info()
    print(data)
    