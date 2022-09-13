'''
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
'''


class ProductOfNumbers:

    def __init__(self):
        self.main = []
        self.pref = []
        self.pref.append(1)
        

    def add(self, num: int) -> None:
        if num == 0:
            self.pref = [1]
        else:
            self.pref.append(num* self.pref[-1])

        self.main.append(num)
        
        

    def getProduct(self, k: int) -> int:
        if k >= len(self.pref):
            return 0
        return self.pref[-1]// self.pref[len(self.pref)-1-k]
        



--------------------------------------------------------------------
class ProductOfNumbers:

    def __init__(self):
        self.preprod = [1]

    def add(self, num: int) -> None:
        if not num:
            self.preprod = [1]
        else:
            self.preprod.append(self.preprod[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.preprod):
            return 0
        return self.preprod[-1] // self.preprod[-k-1]
---------------------------------------------------------------------------------
def __init__(self): #adding one dummy element at the begining 
    self.l = [1]

def add(self, num: int) -> None: # if num is equal to zero, all the product starting from num will also be zero
    if num == 0: # no need to record the previous zero
        self.l = [1]
    else:
        self.l.append(num*self.l[-1])
    return 
def getProduct(self, k: int) -> int:
    length = len(self.l) 
    if k<length: #if means no zero is included
        return self.l[length-1]//self.l[length-1-k]
    return 0 # at least one zero is included
