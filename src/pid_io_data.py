import os

def open_files(pid):
    fd_path = f"/proc/{pid}/fd"

    for fd in os.listdir(fd_path):
        try:
            file = os.readlink(os.path.join(fd_path, fd))
            print(f"{fd}: {file}")
        except PermissionError:
            print(f"{fd}: [Permission Denied]")
