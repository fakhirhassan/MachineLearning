import multiprocessing
import time
import sys
import math


sys.set_int_max_str_digits(1000000)

def factorial(number):
    result = math.factorial(number)
    return result
if __name__ == "__main__":
    number = [5000, 6000, 7000, 8000, 9000, 10000]
    startTime = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(factorial, number)
        
    endTime = time.time()
    print(result)
    print(f"Total time taken: {endTime - startTime} seconds")
    