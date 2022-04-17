You are given two 0-indexed integer arrays nums1 and nums2 of length n.

A range [l, r] (inclusive) where 0 <= l <= r < n is balanced if:

For every i in the range [l, r], you pick either nums1[i] or nums2[i].
The sum of the numbers you pick from nums1 equals to the sum of the numbers you pick from nums2 (the sum is considered to be 0 if you pick no numbers from an array).
Two balanced ranges from [l1, r1] and [l2, r2] are considered to be different if at least one of the following is true:

l1 != l2
r1 != r2
nums1[i] is picked in the first range, and nums2[i] is picked in the second range or vice versa for at least one i.
Return the number of different ranges that are balanced. Since the answer may be very large, return it modulo 109 + 7.



class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        # for (l, r), you can have sum1 how much and sum2 how much
        n = len(nums1)
        prefixSum1 = []
        prefixSum2 = []
        
        curSum1 = 0
        curSum2 = 0
        
        for i in range(n):
            curSum1 += nums1[i]
            curSum2 += nums2[i]
            prefixSum1.append(curSum1)
            prefixSum2.append(curSum2)
            
        total = 0
        sumTable = {}
        sumTable[0] = 1 # the number of combinations that sum1 can be a certain key
        for r in range(n):
            newSumTable = {}
            for diff in sumTable.keys():
                restSum1 = prefixSum1[-1] - prefixSum1[r]
                restSum2 = prefixSum2[-1] - prefixSum2[r]

                newDiff = diff + nums1[r]
                if restSum2 >= newDiff:
                    if newDiff in newSumTable:
                        newSumTable[newDiff] += sumTable[diff]
                    else:
                        newSumTable[newDiff] = sumTable[diff]

                newDiff = diff - nums2[r]
                if restSum1 >= -newDiff:
                    if newDiff in newSumTable:
                        newSumTable[newDiff] += sumTable[diff]
                    else:
                        newSumTable[newDiff] = sumTable[diff]

            sumTable = newSumTable
            if 0 in sumTable:
                total += sumTable[0]
                sumTable[0] += 1 # Suppose the new l starts from here
            else:
                sumTable[0] = 1 # Suppose the new l starts from here
        return total%1000000007
      
--------------------------------------------------------------------------------
First of all, we can see numbers from nums1 are positive and numbers from nums2 are negative, and then, we need to choose some numbers from nums1 and nums2 (all from different indexes), which means, we want to find out how many different paths which have total summation equal to zero. Below is an example of one possible path.

image

Then we can construct our DP solution

1. State Definition:

DP[i] is a dictionary (hash table), which records all the possible total summation from index j (<= i) to index i and how many paths they are. For example, if DP[i] = {1: 3, -2: 5}, which means we have 3 paths to get summation1 and 5 paths to get summation -2.

Now, take a look at the picture above again, you should get
DP[1] = {3: 1, -5: 1, 4: 1, -4: 1, 1: 1, -7: 1}

Try to figure it out firstly.

2. Transition of State
How can we get DP[i] from DP[i-1] ?

Since DP[i-1] already records all the possible summation from index j (<= i-1) to i-1, we only need to add up the contribution of index i now, which is, we should take out all the key-value pair from DP[i-1] and add each key by nums1[i] or -nums2[i].

n1 = nums1[i]
n2 = nums2[i]
# the contribution of index i only
DP[i][n1] += 1 
DP[i][-n2] += 1
# the contribution of index i plus "the contribution from index j (<= i - 1) to index i - 1" which is already recorded in DP[i-1]
for key, value in DP[i-1].items():
	DP[i][key + n1] += value
    DP[i][key - n2] += value
3. Will I count same path more than once?

This is the question you should always ask yourself for these kind of counting DP questions.

The answer is NO, since we start from the first index, so DP[i] records all the path includes nums1[i] or nums2[i] since now and not include any path contains nums1[i + k] or nums2[i + k] (for all k > 0). So all the paths record by DP[i] are independent from DP[j] (for all j != i).

4. Solution
FInally, the last step, we only need to sum up how many ways we can make the summation 0, that is, sum up the value of DP[i][0] for each index i.

The total solution will be:

class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = int(1e9) + 7
        N = len(nums1)
        DP = [defaultdict(int) for _ in range(N+1)]
        ans = 0
        for i in range(1, N+1):
            n1 = nums1[i-1]
            n2 = nums2[i-1]
            DP[i][n1] += 1
            DP[i][-n2] += 1
            
            for key, value in DP[i-1].items():
                DP[i][key + n1] = (DP[i][key + n1] + value) % MOD
                DP[i][key - n2] = (DP[i][key - n2] + value) % MOD
            
            ans = (ans + DP[i][0]) % MOD

        return ans
Note: Since I want DP[0] to be the initial state (empty dictionary), so I iterate from 1 to N instead of 0 to N-1, which means, DP[1] here actually deal with the states comes from index 0 of nums1 and nums2. It's a common trick for simplify the code of DP solution

The time and space complexity are both O(100 * N ^ 2)

Actually, you can save some space from DP since we only need the relation between each pair of DP[i] and DP[i-1]. So we can change it to:

class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = int(1e9) + 7
        N = len(nums1)
        DP = defaultdict(int)
        ans = 0
        for i in range(N):
            n1 = nums1[i]
            n2 = nums2[i]
            DP2 = defaultdict(int)
            DP2[n1] += 1
            DP2[-n2] += 1
            
            for key, value in DP.copy().items():
                DP2[key + n1] = (DP2[key + n1] + value) % MOD
                DP2[key - n2] = (DP2[key - n2] + value) % MOD
            
            ans = (ans + DP2[0]) % MOD
            DP = DP2

        return ans
The space complexity now is reduced to O(100 * N)

4. Time Complexity:

Iteration of each index take O(N)
The size of DP will not exceeded 2 * 100 * N, since the min and max possible summation value is -100 * N and 100 * N. So iterate all key-value pair of DP take O(100 * N) (or you can say O(200 * N), which makes no difference)
The total time complexity is then O(100 * N ^ 2)
