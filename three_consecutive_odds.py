'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = arr
        found = False
        for i in range(len(n)-2):
            n1 = n[i]
            n2 = n[i+1]
            n3 = n[i+2]

            if n1 %2 == 1 and n2 % 2 == 1 and n3%2 ==1:
                found = True
        print(found)
        return found
