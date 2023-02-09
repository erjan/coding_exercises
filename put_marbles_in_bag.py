'''
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.
'''




class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        p = sorted([w[i] + w[i + 1] for i in range(len(w) - 1)])
        return sum(p[len(p) - k + 1:]) - sum(p[:k - 1])
      
------------------------------------------------------------------------------------------------------------
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        arr, res = sorted([weights[i]+weights[i+1] for i in range(len(weights)-1)]), 0
        for i in range(k-1): res += arr[-i-1]-arr[i]
        return res     
      
      
---------------------------------------------------------------------------------------------------------------------
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
        ans = 0
        ans1 = 0
        k -= 1
        res1 = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        res = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        res1.sort(reverse=True)
        res.sort()
        for i in range(k):
            ans1 += res1[i]
        for i in range(k):
            ans += res[i]
        return (ans1 - ans)
      
------------------------------------------------------------------------------------------------------------------------
Intuition
Since the problem mentions minimum and maximum 1st approach is to use DP but it fails to pass the time complexity so our go to method is greedy (usually faster than DP)

If w1,w2,w3,w4,w5,w6,w7,w8 are the weights and we are required to split it in 3 bags,then following would be the solution.

For this problem one needs to convince himself/herself for couple of things:

For k bags one need to make k-1 splits. For the given example 3 bags mean 2 splits.

Assume (for the maximum case) we make the 1st split between w2 and w3, 2nd split between w5 and w6 then the answer would be

Max:
w1+w2 (bag 1) + w3+w5 (bag2) + w6+w8 (bag3)

For the minimum case, we make 1st split between w3 and w4, 2nd split between w6 and w7

Min:
w1+w3 (bag 1) + w4+w6 (bag 2) + w7+w8 (bag3)

Obserse, w1 and w8 is present in both min and max case. Therefore effectively what we need to calculate is:

For max case: w2+w3, w5+w6
For min case: w3+w4, w6+w7

Which means sum of two adjacent weihts.

If you are convinced for above two things then reading the code makes it easier to follow.

Try it with any dummy array and see if it makes sense.

Approach
Calculate all the adjacent weights and sort them.

For max case pick top k-1 adjacent weights and
For min case pick lowest k-1 adjacet weights.

Code
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        if len(weights) == k or k == 1:
            return 0

        wt_sum = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        wt_sum.sort()

        return sum(wt_sum[-(k-1):]) - sum(wt_sum[:k-1])
