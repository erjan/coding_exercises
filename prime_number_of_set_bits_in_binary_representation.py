
'''
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
'''

#my own solution

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
          
        def check_prime(s):
            return s in [2, 3, 5, 7, 11, 13, 17, 19]
    
        count = 0
        l = left
        r = right
        for i in range(l, r+1):

            s = str(bin(i))

            num_ones = s.count('1')

            if check_prime(num_ones):
                count += 1
        print(count)
        return count

      
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for i in range(L,R+1):
            bits= bin(i).count('1')
            if bits!=1 and math.factorial(bits - 1)  % bits == bits - 1:
                res+=1
        return res
      
#another solution

class Solution:
    def isPrime(self,x):
        flag=0
        if x==1:
            return False
        for i in range(2,x):
            if x%i==0:
                flag=1
                break
        if flag==1:
            return False
        return True
        
    def countPrimeSetBits(self, left: int, right: int) -> int:
        arr_dict={}
        lst=list(range(left,right+1))
        for i in lst:
            if i not in arr_dict:
                arr_dict[i]=bin(i).replace("0b","")
        arr=list(arr_dict.values())
        count=0
        for i in arr:
            if self.isPrime(i.count('1')):
                # print(i)
                count+=1
        return count
