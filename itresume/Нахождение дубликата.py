
'''
Дан массив nums, в котором 
содержится n+1 чисел в промежутке [1, n]. В массиве nums есть только 
одно число, которое повторяется несколько раз. Выведите это число.
'''

class Answer:
    def findDuplicate(self, nums):
        
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
