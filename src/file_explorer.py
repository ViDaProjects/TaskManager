# Listar os arquivos contidos em um diretório, juntamente com os atributos de cada arquivo (p.ex. nome, tamanho, permissões, etc.)

import os
import ctypes
import ctypes.util
import time
import stat

import src.data_classes as data_classes

# Load libc
libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Define stat structure (for 64-bit Linux)
class StatStruct(ctypes.Structure):
    _fields_ = [
        ("st_dev", ctypes.c_ulong),
        ("st_ino", ctypes.c_ulong),
        ("st_nlink", ctypes.c_ulong),
        ("st_mode", ctypes.c_uint),
        ("st_uid", ctypes.c_uint),
        ("st_gid", ctypes.c_uint),
        ("__pad0", ctypes.c_int),
        ("st_rdev", ctypes.c_ulong),
        ("st_size", ctypes.c_long),
        ("st_blksize", ctypes.c_long),
        ("st_blocks", ctypes.c_long),
        ("st_atime", ctypes.c_ulong),
        ("st_atime_nsec", ctypes.c_ulong),
        ("st_mtime", ctypes.c_ulong),
        ("st_mtime_nsec", ctypes.c_ulong),
        ("st_ctime", ctypes.c_ulong),
        ("st_ctime_nsec", ctypes.c_ulong),
        ("__unused", ctypes.c_long * 3),
    ]

def interpret_mode(mode):

    # Ensure mode is just the permission bits (lowest 9 bits)
    mode = mode & 0o777

    # Permission characters
    perms = ''
    for shift in [6, 3, 0]:  # owner, group, others
        perms += 'r' if mode & (0o4 << shift) else '-'
        perms += 'w' if mode & (0o2 << shift) else '-'
        perms += 'x' if mode & (0o1 << shift) else '-'
    return perms

def get_username_from_uid(uid):
    with open("/etc/passwd", "r") as passwd_file:
        for line in passwd_file:
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.strip().split(":")
            if len(parts) >= 3 and parts[2].isdigit() and int(parts[2]) == uid:
                return parts[0]
    return "Unknown"

def get_dir_info(path):

    files = []
    folders = []

    try:
        dirs = os.listdir(path)
    except:
        return
    for dir in dirs:
        full_path = os.path.join(path, dir)

        statbuf = StatStruct()
        ret = libc.stat(full_path.encode('utf-8'), ctypes.byref(statbuf))

        if ret == 0:
            name = dir
            permissions = interpret_mode(statbuf.st_mode)
            size = statbuf.st_size
            block_count = statbuf.st_blocks
            time_since_access = int(time.time()) - statbuf.st_atime
            time_since_modified = int(time.time()) - statbuf.st_mtime
            owner = get_username_from_uid(statbuf.st_uid)
            pub_data = data_classes.File(name, permissions, size, block_count, time_since_access, time_since_modified, owner)
            try:
                os.listdir(full_path)
                files.append(pub_data)
            except:
                folders.append(pub_data)
        
    return data_classes.FileInfo(folders, files)

if __name__ == "__main__":
    print(get_dir_info("/home/laser/Documents/TaskManager/src/"))
