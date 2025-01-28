from concurrent.futures import ProcessPoolExecutor
import time

def squareNumber(number):
    time.sleep(1)
    return number * number
number = [1,2,3,4,5]

if __name__ == "__main__":

    t = time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(squareNumber, number)
        for result in results:
            print(result)

    totalTime = time.time() - t
    print(totalTime)