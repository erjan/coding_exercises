'''
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
'''


class ListNode():
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = None
        self.mid = None
        self.end = None
        self.size = 0

    def pushFront(self, val: int) -> None:
        newNode = ListNode(val, self.head)
        if self.size==0:
            self.head = self.mid = self.end = newNode
        elif self.size==1:
            self.head = self.mid = newNode
            newNode.next = self.end
            self.end.prev = newNode
        elif self.size==2:
            self.head = newNode
            self.head.next = self.mid
            self.mid.prev = newNode
        elif self.size%2==1:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.mid = self.mid.prev
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1
        #print('pushfront',self.head.val if self.head else None,self.mid.val if self.mid else None,self.end.val if self.end else None,self.size)

    def pushMiddle(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size==0:
            self.head = self.mid = self.end = newNode
        elif self.size==1:
            self.head = self.mid = newNode
            self.head.next = self.end
            self.end.prev = self.head
        elif self.size==2:
            self.mid = newNode
            self.mid.next = self.end
            self.mid.prev = self.head
            self.head.next = self.mid
            self.end.prev = self.mid
        elif self.size%2==1:
            prev = self.mid.prev
            next = self.mid
            self.mid = newNode
            self.mid.next = next
            self.mid.prev = prev
            prev.next = self.mid
            next.prev = self.mid
        else:
            p = self.mid
            n = self.mid.next
            self.mid = newNode
            self.mid.next = n
            self.mid.prev = p
            p.next = self.mid
            n.prev = self.mid
        self.size += 1
        #print('pushmiddle',self.head.val if self.head else None,self.mid.val if self.mid else None,self.end.val if self.end else None,self.size)

    def pushBack(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size==0:
            self.head = self.mid = self.end = newNode
        elif self.size==1:
            self.end = newNode
            self.end.prev = self.head
            self.head.next = self.end
        elif self.size==2:
            self.end = newNode
            self.mid = self.head.next
            self.mid.next = self.end
            self.end.prev = self.mid
        elif self.size%2==1:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
        else:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
            self.mid = self.mid.next
        self.size += 1
        #print('pushback',self.head.val if self.head else None,self.mid.val if self.mid else None,self.end.val if self.end else None,self.size)

    def popFront(self) -> int:
        if self.size==0:
            return -1
        ret = self.head.val
        if self.size==1:
            self.head = self.mid = self.end = None
        elif self.size==2:
            self.head = self.mid = self.end
            self.head.prev = None
        elif self.size%2==1:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.head.next
            self.head.prev = None
            self.mid = self.mid.next
        self.size -=1
        #print('popfront',self.head.val if self.head else None,self.mid.val if self.mid else None,self.end.val if self.end else None,self.size)
        return ret

    def popMiddle(self) -> int:
        if self.size==0:
            return -1
        ret = self.mid.val
        if self.size==1:
            self.head = self.mid = self.end = None
        elif self.size==2:
            self.head = self.mid = self.end
            self.head.prev = None
        elif self.size%2==1:
            n = self.mid.next
            self.mid = self.mid.prev
            self.mid.next = n
            n.prev = self.mid
        else:
            p = self.mid.prev
            n = self.mid.next
            p.next = n
            n.prev = p
            self.mid = n
        self.size-=1
        #print('popmiddle',self.head.val if self.head else None,self.mid.val if self.mid else None,self.end.val if self.end else None,self.size)
        return ret

    def popBack(self) -> int:
        if self.size==0:
            return -1
        ret = self.end.val
        if self.size==1:
            self.head = self.mid = self.end = None
        elif self.size==2:
            self.end = self.head
            self.head.next = None
        elif self.size%2==1:
            self.mid = self.mid.prev
            self.end = self.end.prev
            self.end.next = None
        else:
            self.end = self.end.prev
            self.end.next = None
        self.size -= 1
        #print('popback',self.head.val if self.head else None,self.mid.val if self.mid else None,self.end.val if self.end else None,self.size)
        return ret
