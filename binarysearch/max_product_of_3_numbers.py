'''

Given a list of integers nums, find the largest product of three distinct elements.

'''


class Solution:
    def solve(self, n):

            n = list(n)
            n.sort(reverse=True)
            print(n)

            case1 = n[0] * n[1] * n[2]

            case2 = n[-2:]
            print(case2)

            case2 = n[0] * case2[0] * case2[1]
            print(case2, case1)

            return max(case1,case2)
          
        
        
#another
#The max product is either two smallest negatives x biggest positve or product of three biggest positives. Try all

class Solution:
    def solve(self, nums):
        nums.sort()
        one = nums[0] * nums[1]

        return max(one * nums[-1], nums[-1] * nums[-2] * nums[-3])
