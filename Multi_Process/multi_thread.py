import threading
import time
#function to print numbers
def print_numbers():
    for i in range(10):
        print(f"Thread 1: {i}")
        time.sleep(2)

#function to print letters
def print_letters():
    for i in range(10):
        print(f"Thread 2: {i}")
        time.sleep(2)

#create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
start_time = time.time()
#start threads
thread1.start()
thread2.start()
#join threads
thread1.join()
thread2.join()
end_time = time.time()
#print time taken
print(f"Time taken: {end_time - start_time} seconds")