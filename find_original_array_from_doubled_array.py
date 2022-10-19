'''
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
'''

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        original = []
        numbers = collections.Counter(changed)
        
        for n in sorted(changed):
            v = n*2
            if numbers.get(n, 0) > 0 and numbers.get(v, 0) > 0:
                original.append(n)
                numbers[n] -= 1
                numbers[v] -= 1
            elif n // 2 not in numbers or n % 2 == 1:
                return []

        return original
