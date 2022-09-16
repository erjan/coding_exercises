'''
You are given an even integer n​​​​​​. You initially have a permutation perm of size n​​ where perm[i] == i​ (0-indexed)​​​​.

In one operation, you will create a new array arr, and for each i:

If i % 2 == 0, then arr[i] = perm[i / 2].
If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
You will then assign arr​​​​ to perm.

Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.
'''

class Solution:
    def reinitializePermutation(self, n):
        
        count = [0]
        original = list(range(n))
        
        def recursion(perm):
            count[0] += 1
            arr = [] 
            for i in range(0, n, 2):
                arr.append(perm[i])
            for i in range(1, n, 2):
                arr.append(perm[i])
            
            equals = 0
            for i in range(n):
                if arr[i] != original[i]:
                    break
                else:
                    equals += 1
            if equals == n:
                return
            recursion(arr[:])
                    
        recursion(original)
        
        return count[0]  
