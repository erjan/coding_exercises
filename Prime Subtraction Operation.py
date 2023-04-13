'''
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.
'''




'''
Constraints are low, primes upto 1000 can be stored in array and binary searched.
Go from back and if current item is not smaller then next after
try to find smallest prime that can make current smaller then one after it.
This can be done in greedy way, until beggining is reached or current problematic item can not be paired with any smaller prime.
In problems with larger P and V (value of A[i]), they can precomputed too, this saves a lot of time if there are many calls to primeSubOperation function.

Complexity
Time complexity:
O(nlogp)O(n log p)O(nlogp) --> where N is length of array and p is the number of primes upto 1000

Space complexity:
O(P)O(P)O(P), where p is number of primes upto 1000
'''

class Solution:
    def primeSubOperation(self, A: List[int]) -> bool:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        for i in range(len(A) - 2, -1, -1):
            if A[i] < A[i + 1]: continue
            index = bisect_right(primes, A[i] - A[i + 1])
            if index == len(primes) or A[i] - primes[index] < 1: return False
            A[i] -= primes[index]
        return True
      
-------------------------------------------------

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # find primes within the range
        comp = [1, 1] + [0]*999
        for i in range(2, int(math.sqrt(1000)+1)):
            j = 2*i
            while j <= 1000:
                comp[j] = 1
                j += i
        primes = [i for i, a in enumerate(comp) if a == 0]
        
        # check True or False
        nums = [0] + nums
        for i, n in enumerate(nums[1:], start=1):
            if n <= nums[i-1]:
                return False
            idx = bisect_left(primes, n - nums[i-1])
            p = primes[idx-1] if idx > 0 else 0
            nums[i] -= p
        return True
