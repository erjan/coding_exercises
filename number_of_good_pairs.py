'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''

def f(n):
    counter= 0
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] == n[j] and i < j:
                print('good pair: (%d, %d)' %(i,j))
                counter+=1
    print('total %d' % counter)

nums = [1,2,3,1,1,3]

f(nums)
