import multiprocessing
import time

def squareNumber():
    for i in range(1, 6):
        time.sleep(1)
        print(i * i)

def cubeNumber():
    for i in range(1, 6):
        time.sleep(1)
        print(i * i * i)

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=squareNumber)
    p2 = multiprocessing.Process(target=cubeNumber)
    t = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    currentTime = time.time() - t
    print(f"Total time taken: {currentTime} seconds")