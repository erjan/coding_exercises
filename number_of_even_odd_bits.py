'''
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].
'''



class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n_bi = bin(n)
        even = odd = 0
        for i,c in enumerate(str(n_bi[2:][::-1])):
            if c=='1':
                if i%2 == 0:
                    even+=1
                else:
                    odd+=1
        result = [even,odd]
        return result
            
        
