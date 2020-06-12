'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]
'''



#trivial solution

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        real_n = len(nums)//2
        result = list()
        
        
        x = nums[:real_n]
        y = nums[real_n:]

        for i in range(len(x)):
            result.append(x[i])
            result.append(y[i])
        print(result)
        return result
