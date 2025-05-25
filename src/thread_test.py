import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):  # Smaller number but with forced switches
        with lock:
            temp = counter
            time.sleep(0.0001)  # Force thread switch
            counter = temp + 1

threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Expected: 10000, Got: {counter}")  # Will likely be less