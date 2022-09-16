'''
Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 
 '''

class Solution(object):
    def negabinary_to_dec(self,arr):
        s = 0
        d = 1
        i = len(arr)-1
        while i>=0:
            s += arr[i]*d
            i -= 1
            d *= -2
        return s
    
    def dec_to_negabinary(self,n):
        if n==0: return [0]
        ret = []
        while n != 0:
            a = abs(n%(-2))
            ret.append(a)
            n = (n-a)//(-2)
        return ret[::-1]
    
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        a = self.negabinary_to_dec(arr1)
        b = self.negabinary_to_dec(arr2)
        return self.dec_to_negabinary(a+b)
-----------------------------------------------------

class Solution:
    def addNegabinary(self, arr1: [int], arr2: [int]) -> [int]:
        result_len = max(len(arr1), len(arr2)) + 2
		# reverse both array
        arr1 = arr1[::-1] + [0] * (result_len - len(arr1))
        arr2 = arr2[::-1] + [0] * (result_len - len(arr2))
		# simply sum, then deal with 2s
        result = [arr1[i] + arr2[i] for i in range(result_len)]

		# note [2, 1] becomes [0, 0]
		#  and [2, 0] becomes [0, 1, 1]
        for i in range(result_len-2):
            if result[i] >= 2:
                if result[i + 1]:
                    result[i] -= 2
                    result[i + 1] -= 1
                else:
                    result[i] -= 2
                    result[i + 1] += 1
                    result[i + 2] += 1
		
		# remove extra 0s
        while result != [0] and result[-1] == 0:
            result = result[:-1]

		# reverse again
        return result[::-1]
    
-------------------------------------------------------------------------------
from collections import deque


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        output = deque()
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            val = carry
            if i >= 0:
                val += arr1[i]
            if j >= 0:
                val += arr2[j]
                
            # Only need a carry if val is -1, 2, or 3 (with reversed sign)
            carry = -(val // 2)
            # Note that -1 % 2 = 1 (carry will also be 1)
            output.appendleft(val % 2)
            i -= 1
            j -= 1
           
        while len(output) > 1 and output[0] == 0:
            output.popleft()
        return output
      
