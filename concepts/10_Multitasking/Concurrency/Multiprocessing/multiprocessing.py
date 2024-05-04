import multiprocessing
import time

# Function to be executed by each process
def print_numbers():
    for i in range(5):
        print("Process {}: {}".format(multiprocessing.current_process().name, i))
        time.sleep(1)

# Create and start multiple processes
processes = []
for i in range(3):
    process = multiprocessing.Process(target=print_numbers)
    processes.append(process)
    process.start()

# Wait for all processes to complete
for process in processes:
    process.join()

print("All processes have completed.")
