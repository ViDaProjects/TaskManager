import ctypes
import os
import data_classes

libc = ctypes.CDLL("libc.so.6")
readlink = libc.readlink
readlink.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
readlink.restype = ctypes.c_ssize_t




def syscall_readlink(path):
    bufsize = 4096
    buf = ctypes.create_string_buffer(bufsize)
    n = readlink(path.encode(), buf, bufsize)
    if n == -1:
        raise OSError(ctypes.get_errno(), f"Failed to readlink for {path}")
    return buf.value[:n].decode()

def split_info(text):
    socket = None
    file = None

    if "socket" in text:
        socket = text[8:-1]
    elif "/" in text:
        file = text
    elif "anon" in text:
        file = "Fake file"
    
    return socket, file

def list_fd_targets(pid):

    sockets = []
    files = []

    fd_dir = f"/proc/{pid}/fd"
    try:
        for fd in os.listdir(fd_dir):
            fd_path = os.path.join(fd_dir, fd)
            try:
                target = syscall_readlink(fd_path)
                socket, file = split_info(target)

                if socket:
                    sockets.append(socket)
                elif file:
                    files.append(file)

            except Exception as e:
                print(f"FD {fd}: Erro ao ler link - {e}")
    except PermissionError:
        print(f"Sem permissão para acessar /proc/{pid}/fd")

    return data_classes.PIDInfo(sockets, files)

class PIDInfo:

    def __init__(self, pid_info_lock, pid_number_lock):
        self.pid_info_lock = pid_info_lock
        self.pid_number_lock = pid_number_lock

    def get_pid_info(self):
        with self.pid_number_lock:
            pid = data_classes.get_pid_num()
        pid_info = list_fd_targets(pid)

        with self.pid_info_lock:
            data_classes.set_pid_info(pid_info)


# Exemplo: listar FDs do processo atual
if __name__ == "__main__":
    pid = os.getpid()  # Hehe, legal né?
    print(list_fd_targets(1))
