
'''

Implement a thread-safe bounded blocking queue that has the following methods:

BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
int size() Returns the number of elements currently in the queue.
Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. The size method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.
'''


from threading import Semaphore
from collections import deque
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = deque()
        self.p1 = Semaphore(capacity)
        self.p2 = Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.p1.acquire()
        self.queue.append(element)
        self.p2.release()
        
    def dequeue(self) -> int:
        self.p2.acquire()
        ret = self.queue.popleft()
        self.p1.release()
        return ret

    def size(self) -> int:
        return len(self.queue)
