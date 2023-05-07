'''
Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

Implement the FrequencyTracker class.

FrequencyTracker(): Initializes the FrequencyTracker object with an empty array initially.
void add(int number): Adds number to the data structure.
void deleteOne(int number): Deletes one occurence of number from the data structure. The data structure may not contain number, and in this case nothing is deleted.
bool hasFrequency(int frequency): Returns true if there is a number in the data structure that occurs frequency number of times, otherwise, it returns false.
'''

from collections import defaultdict

class FrequencyTracker:

    def __init__(self):

        self.ds = defaultdict(int)
        self.fs = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.fs[self.ds[number]] -=1
        self.ds[number]+=1
        self.fs[self.ds[number]]+=1

        

    def deleteOne(self, number: int) -> None:
        self.fs[self.ds[number]]-=1
        self.ds[number] = max(0, self.ds[number]-1)
        self.fs[self.ds[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        if self.fs[frequency]>0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
