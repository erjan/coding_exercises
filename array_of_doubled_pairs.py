'''
Given an integer array of even length arr, return true if 
it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 
0 <= i < len(arr) / 2, or false otherwise.
'''

from collections import Counter

class Solution:
    def checkPos(self, arr):
        ctr = Counter()
        for el in arr:
            if ctr[el * 2] > 0:
                ctr[2 * el] -= 1
            else:
                ctr[el] += 1
        return sum(ctr.values()) == 0
    
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n = len(arr)
        pos = []
        neg = []
        for el in arr:
            if el >= 0:
                pos.append(el)
            else:
                neg.append(-el)
        pos.sort(reverse = True)
        neg.sort(reverse = True)
        return self.checkPos(pos) and self.checkPos(neg)
      
------------------------------------------------------------------------------------
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n = len(arr)
        if n % 2 == 1 or n == 1:
            return []

        numbers = Counter(arr)
        
        for i in sorted(arr):
            
            double = i*2
            if numbers.get(i, 0) > 0 and numbers.get(double, 0) > 0:
                numbers[i] -= 1
                numbers[double] -= 1
        for i in numbers.values():
            if i > 0:
                return False
        return True
