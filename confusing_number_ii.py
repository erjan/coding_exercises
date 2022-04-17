'''
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return the number of confusing numbers in the inclusive range [1, n]
'''


class Solution:
    def confusingNumberII(self, N: int) -> int:
        rotatables = [1, 0, 6, 8, 9]
        rotation_map = {1:1, 0:0, 6:9, 8:8, 9:6}        
        confusing_number_count = 0
        
        def count_rotatables(cur_num=0):
            nonlocal confusing_number_count
            if cur_num * 10 > N:
                return
            for num in rotatables:
                next_num = cur_num*10 + num
                if next_num == 0:
                    continue
                confusing_number_count += next_num <= N and is_valid_rotation(next_num)
                count_rotatables(next_num)
        
        def is_valid_rotation(num):
            rotated = 0
            cur_num = num
            while cur_num:
                rotated = rotated * 10 + rotation_map[cur_num%10]
                cur_num //= 10
            return rotated != num
        
        count_rotatables()
        
        return confusing_number_count
      
------------------------------------------------------------------------------------------
class Solution:
    def confusingNumberII(self, N: int) -> int:
        rotations = {1:1, 6:9, 8:8, 9:6, 0:0}
        valid = [0, 1, 6, 8, 9]
        
        def backtrack(num, rotation, position):
            if num > N:
                return
            
            if num != rotation:
                count[0] += 1
            
            for digit in valid:
                backtrack(num * 10 + digit, rotations[digit] * position + rotation, position * 10)
        
        count = [0]
        for digit in valid[1:]:
            backtrack(digit, rotations[digit], 10)
        return count[0]
      
------------------------------------------------------------------------
Main idea: Call numbers that are the same as themselves after rotating 180 degrees "cyclic numbers". Call all numbers that are still valid after rotating 180 degrees "valid numbers". The number of confusing numbers is the number of valid numbers minus the number of cyclic numbers.

There are lots of edge cases in this problem so the code is not very clean.

class Solution(object):
    def confusingNumberII(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = max(len(str(n)), 3)
        g = [-1] * N # g(n) = num of exact n digit cyclic numbers
        f = [-1] * N # n digit cyclic where two ends can be 0's
        g[0] = 1
        g[1] = 2
        f[0] = 1
        f[1] = 3
        for i in range(2,N):
            g[i] = 4 * f[i-2]
            f[i] = sum(g[j] for j in range(i, -1, -2))
            
            if i%2 != 0:
                # we missed all zeros situation for odd i's
                f[i] += 1

        cds = [0, 1, 6, 8, 9] # confusing digits
        A = list(str(n))
        A = [int(a) for a in A]
        
        # count the number of valid numbers <= n
        valid_count = 0
        for i in range(len(A)):
            smaller_num = len([j for j in cds if j<A[i]])
            valid_count += smaller_num * 5**(len(A)-i-1) # definetly within range
            
            if A[i] not in cds:
                break
            else:
                if i==len(A)-1:
                    valid_count+=1
        print("valid_count", valid_count)
        
        flip = {0:0,1:1,6:9,8:8,9:6}
        
        # count the number of cyclic numbers
        ptr = 0
        cyclic_count = 0
        lastptr = len(A) - 1
        backdigits = [] # list of set back digits, start from the last reverse order
        while ptr < lastptr:
            smaller_num = len([i for i in cds if i<A[ptr]]) #
            if smaller_num >= 1: # if 0 < A[ptr]
                if len(backdigits) > 0:
                    cyclic_count += smaller_num * f[(lastptr-ptr-1)]
                else:
                    cyclic_count += (smaller_num-1) * f[(lastptr-ptr-1)] # if not 0
                    cyclic_count += sum(g[0:(lastptr-ptr)+1]) # if we choose 0
            
            if A[ptr] in cds:
                backdigits.insert(0, flip[A[ptr]])
                ptr += 1
                lastptr -= 1
            else:
                break
                
        print("cyclic", cyclic_count)
        
        # check if we reached the middle
        if ptr > lastptr:
            # strart from the ptr, if everything fixed so far is fine, add 1
            adder = 1
            j = 0
            for i in range(ptr, len(A)):
                if A[i] > backdigits[j]:
                    adder = 1
                    break
                elif A[i] < backdigits[j]:
                    adder = 0
                    break
                j += 1
            cyclic_count += adder
        elif ptr == lastptr:
            # strart from the ptr, if everything fixed so far is fine, add 1
            single_cyclic_set = [0,1,8]
            cyclic_count += len([i for i in single_cyclic_set if i<A[ptr]])
            # count ways for the center digit. These will be smaller than A
            if A[ptr] in single_cyclic_set:
                adder = 1
                j = 0
                for i in range(ptr+1, len(A)):
                    if A[i] < backdigits[j]:
                        adder = 0
                        break
                    elif A[i] > backdigits[j]:
                        adder = 1
                        break
                    j += 1
                cyclic_count += adder
        
        result = valid_count - cyclic_count
        return result
