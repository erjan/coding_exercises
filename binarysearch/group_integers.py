'''
Given a list of integers nums, return whether you can split the list into 1 or more groups where:

The size of each group is larger than or equal to 2.
The sizes of all groups are equal.
All the integers in each group are the same.
'''

#my own terrible solution

class Solution:
    def solve(self, nums):
        if len(nums)< 2:
            return False
        nums = sorted(nums)
        group_size = 1
        print('sorted')
        print(nums)
        c = Counter(nums)
        c = c.most_common()
        print('most common')
        print(c)
        temp = list()
        for el in c:
            temp.append( el[1])
            
        print(temp)
        #c = sorted(c.values())
        c = sorted(temp)
                
        if len(c) == 1:
            print('good')
            return True
        for i in range(len(c)):
            if c[i] == 1 or c[i] % c[0]!=0 and c[i] % 2 != 0:
                print('bad!')
                return False
        print('all good')
        return True
