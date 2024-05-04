import threading
import time

def print_seconds(seconds):
         print(f"It took {seconds} seconds ")
         time.sleep(seconds)
# using normal code
# t1 = time.perf_counter()
# print_seconds(3)
# print_seconds(7)
# print_seconds(2)
# t2= time.perf_counter()
# t = t2-t1
# print(t) #12 seconds

#using threading
t3= time.perf_counter()
thread1 = threading.Thread(target=print_seconds , args=[3])
thread2 = threading.Thread(target=print_seconds , args=[7])
thread3 = threading.Thread(target=print_seconds , args=[2])

thread1.start()
thread2.start()
thread3.start()

#Waits fo all to be completed 
thread1.join()
thread2.join()
thread3.join()
t4 = time.perf_counter()

t_thread = t4-t3
print(t_thread)