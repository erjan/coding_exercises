'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''

class Solution(object):
    def isPowerOfThree(self, n):
        # power_list: 3^0, 3^1, ..., 3^19
        power_list = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
        return n in power_list
      
      
public boolean isPowerOfThree(int n) {
    if(n>1)
        while(n%3==0) n /= 3;
    return n==1;
}      


#my solution

class Solution:
    def isPowerOfThree(self, n: int) -> bool:                
        if n < 1: return False
        
        if n !=1:
            while n %3 ==0:
                n = n/3

        return n== 1
