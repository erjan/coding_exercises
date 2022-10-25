'''
You are given a 0-indexed binary string target of length n. You have another binary string s of length n that is initially set to all zeros. You want to make s equal to target.

In one operation, you can pick an index i where 0 <= i < n and flip all bits in the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.

Return the minimum number of operations needed to make s equal to target.
'''

    def minFlips(self, target: str) -> int:
        flips = 0
        i0 = target.find('1')
        if i0 ==-1:
            return flips
        flips = 1
        for i in range(i0 + 1, len(target)):
            if target[i] != target[i-1]:
                flips += 1
            
        return flips
      
      
