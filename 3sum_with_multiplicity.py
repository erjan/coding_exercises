'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.
'''



#TLE
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        count = 0
        for i in range(0, len(arr)-2):
            rem_sum = target - arr[i]
            hash_map = {}
            for j in range(i+1, len(arr)):
                if arr[j] > rem_sum:
                    break
                if rem_sum - arr[j] in hash_map:
                    count = count + hash_map[rem_sum-arr[j]]
                # update the hash_map
                hash_map[arr[j]] = hash_map.get(arr[j], 0) + 1
        return count % 1000000007
      
-----------------------------------------------------------------------
class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

                    j += 1
                    k -= 1

        return ans % MOD
