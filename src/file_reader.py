import os
import re

PROC_DIR = "/proc"

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