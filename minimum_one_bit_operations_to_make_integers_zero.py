'''
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.
'''

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n
        def leftmostbit(x):
            x |= x >> 1
            x |= x >> 2
            x |= x >> 4
            x |= x >> 8
            x |= x >> 16
            x += 1
            x >>= 1
            return x
        x = leftmostbit(n)
        return ((x << 1) - 1) - self.minimumOneBitOperations(n - x)
      
---------------------------------------------------------------------------
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        to flip the bits to turn the number to zero
        
        Interpretation of Rules:
        - recursive:
            to turn a leading one of i bits to zero, the only way is to turn the i-1 bits to a leading one pattern
            and to turn the i-1 bits leading zero to zero, the only way is to turn the i-2 bits to a leading one pattern
            and so on, which is a recursive process
            
            (10000.. -> 11000.. -> 01000..), (01000.. -> 01100.. -> 00100), ..., (..010 -> ..011 -> ..001 -> ..000)
            
        - reversable:
        
            Let's make some observations to check if there's any pattern:

            - 2: 10 -> 11 -> 01 -> 00
            - 4: 100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000
            - 8: 1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> (reversing 100 to 000) -> 0000
            ...
            
            based on the observation, turning every i bits leading one to zero, is turning the i-1 bits from 00.. to 10..
            and then back to 00.., which is a reverable process, and with the recursive process we can conclude that
            turning any length of 00..M-> 10.. is a reversable process
        
        - all unique states:
            since it is recursive and reversable, and we are flipping every bit between 1 and 0 programtically 10.. <-> 00..
            we can conclude that every intermediate state in a process is unique (2**i unique states, so we need 2**i - 1 steps)
        
                for i bits 10.. <-> 00.. - numer of operations f(i) = 2**i - 1
            
            this also aligns with the observation above that f(i) = 2*f(i-1) - 1 (-1 for no operation needed to achieve the initial 000)
        
        Process:
        to turn any binary to 0, we can turning the 1s to 0s one by one from lower bit to higher bit
        and because turning a higher bit 1 to 0, would passing the unique state including the lower bit 1s
        we can reverse those operations needed for the higher bit 100.. to the unique state including the lower bit 1s
        
        e.g. turning 1010100 to 0
        - 1010(100) -> 1010(000), we will need 2**3 - 1 operations
        - 10(10000) -> 10(00000), we will need (2**5 - 1) - (2**3 - 1) operations
        we will be passing the state 10(10100), which is ready available from the last state
        so we can save/reverse/deduct the operations needed for 1010(000) <-> 1010(100)
        - ...
        
            so for any binary, f(binary) would tell us how many operations we need for binary <-> 000..
            and for any more 1s, 100{binary} we can regard it as a process of 100.. <-> 100{binary} <-> 000{000..}
            which is 100.. <-> 000.. (2**i - 1) saving the operations 100{000..} <-> 100{binary} (f(binary))
            = (2**i - 1) - f(last_binary)
            
        """
        binary = format(n, "b")

        N, res = len(binary), 0
        
        for i in range(1, N+1):
            if binary[-i] == "1": res = 2**i-1 - res
                
        return res
