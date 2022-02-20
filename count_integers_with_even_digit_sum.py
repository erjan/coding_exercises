'''
Given a positive integer num, return the number of positive integers 
less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.
'''

#my own template-solution


def f(n):
    s = 0
    print()
    for i in range(len(n)):
        i = int(n[i])
        s += i
        print(i, end = ' ')

    print()
    print('sum is %d' % s)
            
    if s %2 == 0:
        print('good sum of digits is even')
        return True
    return False

n = 4
count = 0
for i in range(1,n+1):
    cur_num = str(i)
    print('cur number to check his digits sum: %s' % str(cur_num))
    res = f(cur_num)
    if res:
        count+=1
    
print('total real is %d' % count)

#my actual solution


class Solution:
    def countEven(self, num: int) -> int:
        def is_sum_digits_even(n):
            s = 0
            for i in range(len(n)):                
                i = int(n[i])
                s += i
            
            if s %2 == 0:
                return True
            return False
                                                            
        count = 0
        for i in range(1,num+1):
            cur_num = str(i)
            res = is_sum_digits_even(cur_num)
            if res:
                count+=1
        return count
