'''
RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also removing a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of same values the multiset contains.
'''


class RandomizedCollection:

    def __init__(self):
        self.items = []

    def insert(self, val: int) -> bool:
        self.items.append(val)
        if self.items.count(val) > 1:
            return False
        else:
            return True

    def remove(self, val: int) -> bool:
        if val in self.items:
            flag = True
            self.items.remove(val)
        else:
            flag = False
        
        return flag

    def getRandom(self) -> int:
        return choice(self.items)
---------------------------------------------------------------------------------------------
from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        self.items, self.idxs = [], defaultdict(set) 

    def insert(self, val: int) -> bool:
        self.items.append(val)
        self.idxs[val].add(len(self.items)-1)
        return len(self.idxs[val]) == 1
        

    def remove(self, val: int) -> bool:
        if not self.idxs[val]:
            return False
        #we also need to cosider the case when the removed element is the last element of self.items
        out_idx, in_item = self.idxs[val].pop(), self.items[-1]
        self.items[out_idx] = in_item
        self.idxs[in_item].add(out_idx)
        self.idxs[in_item].discard(len(self.items)-1)
        self.items.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.items)
      
