import queue
import threading
import time


def producer(q, count) -> None:
    for n in range(count):
        print('Producing', n)
        q.put(n)
        time.sleep(1)
    print('Producer Done')
    q.put(None)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('Consuming', item)
    print('Counsumer done')


q = queue.Queue()
threading.Thread(target=producer, args=(q, 10)).start()
threading.Thread(target=consumer, args=(q,)).start()


# Challenge: How to implement the same funcunality, but no threads.
#   - q.get waiting ...