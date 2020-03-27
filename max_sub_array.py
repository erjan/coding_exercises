#gives TLE error

import math
def f(nums):
    local_sum = 0
    global_sum = float('-inf')
    print(nums)

    res = []
    for r in range(len(nums)):
        print('-------------------------------------')
        before = 0
        #print(nums[r:i])
        for i in range(r,len(nums)):
            #print('-------------------------------------------')
            print(nums[r:i])
            
            local_sum = nums[i] + before
            #print('local sum: %d = nums[i]: %d + %d' %( local_sum, nums[i], before))
            before = local_sum
            if local_sum > global_sum:
                global_sum = local_sum
        print('global sum %d ' % global_sum)
        res.append(global_sum)
        

a = [-2,1,-3,4,-1,2,1,-5,4]

f(a)
        
