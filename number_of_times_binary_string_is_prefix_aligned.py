'''
You have a 1-indexed binary string of length n where all the bits are 0 initially. We will flip all the bits of this binary string (i.e., change them from 0 to 1) one by one. You are given a 1-indexed integer array flips where flips[i] indicates that the bit at index i will be flipped in the ith step.

A binary string is prefix-aligned if, after the ith step, all the bits in the inclusive range [1, i] are ones and all the other bits are zeros.

Return the number of times the binary string is prefix-aligned during the flipping process.
'''


Let right be the index of the rightmost bulb we have lit so far.

def numTimesAllBlue(light):
    cnt = right = 0
    for i, x in enumerate(light, 1):
        right = max(right, x)
        cnt += (right == i)
    return cnt
If total number of bulbs we have lit (indicated by i) equals to right, then we have all lit bulbs being blue and we add cnt
------------------------------------------------------------------------------------------------------------------------------------

The key point is updating the current max value while traversing, once we meet i + 1 == cur_max, then it means all the lights are blue.

class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        rst = 0
        cur_max = 0
        for i, l in enumerate(light):
            cur_max = max(cur_max, l)
            # everytime meet max, increase rst
            if i + 1 == cur_max:
                rst += 1
        return rst
