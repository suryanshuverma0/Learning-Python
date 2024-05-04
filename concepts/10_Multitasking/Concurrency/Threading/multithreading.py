import threading
import time

# Function to be executed by each thread
def print_numbers():
    for i in range(5):
        print("Thread {}: {}".format(threading.current_thread().name, i))
        time.sleep(1)

# Create multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed.")
