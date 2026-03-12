import time
from concurrent.futures import ThreadPoolExecutor
#function to print numbers
def print_numbers(n):
        time.sleep(2)
        return n
n=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
#create thread pool
with ThreadPoolExecutor(max_workers=4) as executor:
    result=executor.map(print_numbers, n)
t=time.time()
for result in result:
    print(result)
print(f"Time taken: {time.time() - t} seconds")

