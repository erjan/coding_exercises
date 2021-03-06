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
    
    #just using del 
    
    #beats 99.2 of all submissions lol
    
    class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        real_n = len(nums)//2
        result = list()
        
        
        x = nums[:real_n]
        y = nums[real_n:]

        for i in range(len(x)):
            result.append(x[i])
            result.append(y[i])
        del x,y
        return result
    
    
    #another solution - iterating thru n not nums array:
    class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
