'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        res = []
        n = num
        up_limit = 2**31-1
        low_limit = -2**31

        for i in range(25):
            temp = 4**i
            if temp < up_limit:
                res.append(temp)

        if n in res:
            print('true')
            return True
        print('false')
        return False
    
# non loop, non-for solution


def f(num):
    num_bin = bin(num)
    num_str = str(num_bin) #0b10000
    num_str = num_str.split('b')[1] #remove and take after 'b' part
    # all numbers which are power of 4 must be > 0 and have 1 bit '1' and have even number of zeros.
    if num > 0:        
        if num_str.count("1") == 1 and num_str.count("0")%2 ==0:
            print('true')
            return True
    print('false')
    return False
   
fours = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
f(fours[5]-1)
