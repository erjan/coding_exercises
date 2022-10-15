'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
'''

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        d = [1] + [0] * K # range of key is 0 <= key < K because key always mod by K
        acc = 0
        for a in A:
            acc = (acc + a) % K # it's works because a % k % k % k .... n times is still same as a % k 
            if d[acc]:
                res += d[acc]
            d[acc] += 1            
        return res
      
----------------------------------------------------------------------------------

class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		d = {0: 1}
		prefix_sum, count = 0, 0

		for num in nums:
			prefix_sum = (prefix_sum + num) % k
			count += d.get(prefix_sum, 0)

			# make the new prefix_sum key be whatever the old value was + 1
			d[prefix_sum] = d.get(prefix_sum, 0) + 1

		return count
Someone may also ask, why modulo at all? Well that's because that's what it's meant for. It's way to map some value into memory in a clock like fashion if that value somehow leads to the same mapping against another value.
i.e in this case, 2 different subarrays with the same sum are both divisble by k so they end up pointing to the same key.
(try learn about consistent hashing - the algorithm behind load balancing - and how hashmaps are designed for more details).

just a note, a very simple hashmap can use soemthing like, some_number % some_prime_number to map to a key in a hashmap.
