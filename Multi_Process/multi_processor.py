import multiprocessing
import time
#function to print numbers(process 1)
def print_numbers():
    for i in range(10):
        print(f"Process 1: {i}")
        time.sleep(2)
#function to print letters(process 2)
def print_letters():
    for i in range(10):
        print(f"Process 2: {i}")
        time.sleep(2)
#main function(not required in single processor or thread)
if __name__ == "__main__":
    #create processes       
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)
    start_time = time.time()
    #start processes
    process1.start()
    process2.start()
    #join processes
    process1.join()
    process2.join()
    end_time = time.time()
    #print time taken
    print(f"Time taken: {end_time - start_time} seconds")