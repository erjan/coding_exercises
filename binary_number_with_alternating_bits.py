'''
Given a positive integer, check whether it 
has alternating bits: namely, if two adjacent bits will always have different values.
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
            n = bin(n)
            n = n[2:]


            res = not '00' in n and not '11' in n
            print(res)
            return res
        
        
#another my own solution        
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
            n = bin(n)
            for i in range(len(n)-1):
                if n[i] == n[i+1]:
                    return False
            return True
