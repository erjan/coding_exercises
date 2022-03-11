'''
Given an integer num, return three consecutive integers (as a sorted array) that sum to num. 
If num cannot be expressed as the sum of three consecutive integers, return an empty array
'''


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = num
        n = str(n)
        s_check = 0
        for i in range(len(n)):
            s_check += int(n[i])

        if s_check % 3 == 0:
            res = list()

            actual_num = int(n) // 3
            res = [actual_num-1, actual_num, actual_num+1]
            return res
