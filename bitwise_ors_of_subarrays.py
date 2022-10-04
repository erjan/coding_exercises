'''
We have an array arr of non-negative integers.

For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].

Return the number of possible results. Results that occur more than once are only counted once in the final answer
'''

    def subarrayBitwiseORs(self, A):
        res, cur = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)
      
-------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def subarrayBitwiseORs(self, A):
        # Tabulation is a list of sets, one for each number in A. 
        # Each set, at position i, is initialised to containing the element at A[i]
        tabulation = [set([A[i]]) for i in range(len(A))]
        
        # And now we need to go through, updating the sets based on the previous set.
        for i in range(1, len(A)):
            for previous_result in tabulation[i - 1]: 
                tabulation[i].add(A[i] | previous_result)  
        
        # Return the number of unique numbers in the tabulation list.
        return len(set.union(*tabulation)) if len(A) > 0 else 0
      
--------------------------------------------------------------------------------------------------------------

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        my_set = set(A)
        curr = 0
        prev = set()
        prev.add(A[0])
        for num in A[1:]:
            temp = set()
            for p in prev:
                temp.add(num | p)
                my_set.add(num | p)
            prev = temp
            prev.add(num)

        return len(my_set)
