'''
Given a characters array letters that is sorted in non-decreasing order and a character target, return 
the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
'''


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        l = 0
        r = len(letters)-1
        mid = 0

        while l <= r:

            mid = (l+r)//2

            if letters[mid] <= target:
                l = mid+1
            elif letters[mid] > target:
                r = mid - 1
            else:
                return mid
        res = letters[l]
        return res
       
