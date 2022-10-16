'''
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.
'''
'''
Intuition
Do this first:
Given pref, find arr that
pref[i] = arr[0] + arr[1] + ... + arr[i]
pref is prefix sum of arr

The solution is simple:

for(int i = A.size() - 1; i > 0; --i)
    A[i] -= A[i - 1];
return A;
Now we are doing something similar for this problem.


Explanation
Since pref is the prefix array,
it's calculated from arr one by one,
we can doing this process reverssely to recover the original array.

Since
pref[i] = pref[i-1] ^ A[i]
so we have
pref[i] ^ pref[i-1] = A[i]

So we simply change - to ^ in the intuition solution

The reverse operation of + is -
The reverse operation of ^ is still ^
More general, we can apply this solution to prefix of any operation.
'''

def findArray(self, A):
        for i in range(len(A) - 1, 0, -1):
            A[i] ^= A[i - 1]
        return A
      
----------------------------------------------------------------------------
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in range(len(pref)-1,0,-1):
            pref[i] = pref[i]^pref[i-1]
        
        return pref
          
