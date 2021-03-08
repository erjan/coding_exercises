'''
You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
'''

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        nums = [0] * (n+1)
        nums[0] = 0
        nums[1] = 1

        i = 1
        t = len(nums)

        while (2*i+1) <= (t-1):

          # here is the problem: из за описания задачи я пытался генерить числа по четным нечетным -  а надо было просто все числа по правилам сразу генерить!
          #быть внимательнее....
          # if( i %2 == 0):....
          # elif (i %2 != 0):.....
            nums[2*i] = nums[i]
            nums[2*i+1] = nums[i] + nums[i+1]

            i+=1

        return max(nums)
