import threading
import time

def printNumbers():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

def printAlphabets():
    for i in range(65, 75):
        time.sleep(1)
        print(chr(i))

t1 = threading.Thread(target=printNumbers)
t2 = threading.Thread(target=printAlphabets)
t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

finishedTime = time.time() - t
print(f"Total time taken: {finishedTime} seconds")