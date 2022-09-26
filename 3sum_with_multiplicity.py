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
class Solution:
    def threeSumMulti(self, A, T):
        nmap, third, ans = [0 for _ in range(101)], ceil(T / 3) - 1, 0
        for num in A: nmap[num] += 1
        for k in range(min(T,100), third, -1):
            rem = T - k
            half = ceil(rem / 2) - 1
            for j in range(min(rem, k), half, -1):
                i = rem - j
                x, y, z = nmap[i], nmap[j], nmap[k]
                if i == k: ans += x * (x-1) * (x-2) // 6
                elif i == j: ans += x * (x-1) // 2 * z
                elif j == k: ans += x * y * (y-1) // 2
                else: ans += x * y * z
        return ans % 1000000007
