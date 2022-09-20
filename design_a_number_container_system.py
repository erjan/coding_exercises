'''
Design a number container system that can do the following:

Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:

NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
'''


from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.d1 = defaultdict(SortedSet)
        self.d2 = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.d2:
            self.d1[self.d2[index]].discard(index)
            self.d2[index]=number
            self.d1[number].add(index)
            
        else:
            self.d2[index]=number
            self.d1[number].add(index)

    def find(self, number: int) -> int:
        #print(self.d1)
        if number in self.d1 and len(self.d1[number])>0:
            return self.d1[number][0]
        else:
            return -1
          
----------------------------------------------------------------------------------------------
from sortedcontainers import SortedList
class NumberContainers:
    def __init__(self):
        self.numberIndices = defaultdict(SortedList)
        self.indexNumber = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indexNumber:
            num  = self.indexNumber[index]
            self.numberIndices[num].discard(index)
        self.indexNumber[index] = number
        self.numberIndices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numberIndices or not self.numberIndices[number]:
            return -1
        return self.numberIndices[number][0]
            
