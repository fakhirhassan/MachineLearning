from concurrent.futures import ThreadPoolExecutor

import time

def printNumbers(number):
    time.sleep(1)
    return number
number = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20]

t = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(printNumbers, number)
    for result in results:
        print(result)
totalTime = time.time() - t
print(f"Total time taken: {totalTime} seconds")