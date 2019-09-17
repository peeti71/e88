import threading
import multiprocessing.dummy
#from queue import Queue
import time
# for multi threading
from threading import *
from time import sleep
from multiprocessing import Process, Queue


q = Queue()
# function for finonacci

def optimized_fibonacci(f):
    time.sleep(1)
    if f >= 0 and f <= 1:
        return f
    else:
        fib = [0, 1]
        for i in range(2, f + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        print(fib[f])


# function to run Thread
def threader():
    while True:
        f = q.get()
        optimized_fibonacci(numFibonacci)
        q.task_done()




numThreads = 2
numFibonacci = 10000
worker = 100
numRun = 1000

for x in range(numThreads):
    t = threading.Thread(target=threader)
    for runtime in range(worker):
        q.put(runtime)

    t.daemon = True
    t.start()
    sleep(1)

start = time.time()

join()

print('Entire job took:', time.time() - start)