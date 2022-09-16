'''
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
'''

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        end=len(A)
        res=[]
        while end>1:
            maxInd=A.index(max(A[:end])) #step 1 get max
            if maxInd==end-1: #if Max already at the end then its in the right place decrement end and continue
                end-=1
                continue

            #making the max element at Index 0, unless if it already was at index 0
            if maxInd!=0:
                A[:maxInd+1]=reversed(A[:maxInd+1])
                res.append(maxInd+1) #append flipping size which is maxInd+1
                
                
            #Now max is at ind=0, flip whole array to make it at the "end"
            A[:end]=reversed(A[:end])
            res.append(end)
            
            end-=1 #decrement end
        return res    
      
--------------------------------------------------------------------------------------------

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        x = len(A)
        k = []
        
        for indx in range(x):
            max_ = max(A[:x - indx])
            max_indx = A.index(max_) + 1
            A[:max_indx] = reversed(A[:max_indx])
            k.append(max_indx)
            
            A[:x - indx] = reversed(A[:x - indx])
            k.append(x - indx)
        return k
