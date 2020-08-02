'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
'''


from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        
        c = list(c.values())
        
        made_set = set(c)
        
        if len(made_set) == len(c):
            return True
        return False
