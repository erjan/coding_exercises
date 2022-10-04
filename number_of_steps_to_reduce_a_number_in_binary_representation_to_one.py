'''
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.
'''


class Solution:
    def numSteps(self, s: str) -> int:                        
        steps = 0
        
        cur = int(s,2)
        
        while cur!= 1:
            
            for i in range(len(s)-1,-1,-1):            
                if s[i] == '0': #num is even
                    
                    cur = cur//2
                    steps+=1
                    s = bin(cur)[2:]
                    break
                else:
                    cur = cur+1
                    steps+=1
                    s = bin(cur)[2:]

                    break
        return steps
                
--------------------------------------------------------------------------------------------------------------------
def numSteps(self, s):
        # Assignment
        num = int(s, 2)  # Turn binary str into its decimal counterpart
        moves = 0
    
        if num == 1:  # Threshold
            return moves

        # Reducing num into 1 while incrementing moves
        while num != 1:
            # If odd, make it even by addition
            if num % 2 == 1: 
                num += 1
                moves += 1
            # Inloop Threshold
            if num == 1:  
                return moves
            # Use division by 2 as much as possible
            num //= 2
            moves += 1

        return moves
                
                
              
