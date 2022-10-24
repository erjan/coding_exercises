'''
You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

The number of global inversions is the number of the different pairs (i, j) where:

0 <= i < j < n
nums[i] > nums[j]
The number of local inversions is the number of indices i where:

0 <= i < n - 1
nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.
'''


'''
w: it is trivial to get the number of local inversion,
    since we only need to compare two neighbours, the 
    key is to find the number of global inversion.
	AGAIN, for probelm like number in a array of length N is 0,...,N-1
	a natural idea is to think about adding more meaningful things to the index, 
	which help to reduce the space
h: note that the number in the arr of length n is 0,1,...,n-1
    A key observation is:
    At current index,
      1) if num > num's index: 
          currnet global inversion = num - num's index
          this is how many numbers after current index is smaller
          than the number at current index
      2) if num < num's index
          current global inversion = num's index - num -1
          this is how many numbers before current index is larger
          than the number at current index, the reason we subtract 1
          is that we have one duplicated count in 1)
          e.g. : [2, 1, 0] when we at index 0, we include the 
          instance 2>0, so when at at index 2, we should not include 0<2.
    then everything is trivial now
	
O(N) in time and O(1) in space
'''

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        numLoc = 0
        numGlo = 0

        for idx, num in enumerate(A):
            if num > idx:
                numGlo += (num-idx)
            elif num < idx:
                numGlo += (idx-num-1)
            
            if idx < len(A)-1 and num > A[idx+1]:
                numLoc += 1
        
        print(numLoc, numGlo)
        return numLoc == numGlo
--------------------------------------------------------------------------------------------------------------------------
'''
Every local inversion is also a Global inversion
So we only have to check whether there are any other global inversions i.e.The inversion separated by more than one index
So we track the maximum value seen before the previous value of the current element i.e.max_before_prev=max(max_before_prev,A[i-1])
If this max_before_prev is greater than the current element then it means that we have a global inversion separated by more than one index and hence return False
'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        max_before_prev=-1
        for i in range(1,len(A)):
            if A[i]<max_before_prev:
                return False
            max_before_prev=max(max_before_prev,A[i-1])
        return True
