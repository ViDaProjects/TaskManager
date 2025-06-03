import os
import re

import file_reader

IO_DIR = "ioports"

class IOMiner:

    def __init__(self):
        self.lock_gather_io = None


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

if __name__ == "__main__":
    test = IOMiner()
    test.read_io_ports()