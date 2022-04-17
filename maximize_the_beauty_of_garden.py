There is a garden of n flowers, and each flower has an integer beauty value. The flowers are arranged in a line. You are given an integer array flowers of size n and each flowers[i] represents the beauty of the ith flower.

A garden is valid if it meets these conditions:

The garden has at least two flowers.
The first and the last flower of the garden have the same beauty value.
As the appointed gardener, you have the ability to remove any (possibly none) flowers from the garden. You want to remove flowers in a way that makes the remaining garden valid. The beauty of the garden is the sum of the beauty of all the remaining flowers.

Return the maximum possible beauty of some valid garden after you have removed any (possibly none) flowers.


Intuition

Length of flowers array is 10^5 => the algorithm needs to be O(n) or O(nlogn)
There is always a valid solution so don't worry about edge cases (e.g no solution)
In order to compute the max sum, we only need to include the positive numbers between the first and the last
First and last might be negative, so we have to take this into account when we compute the maxsum
Everything can be done in one traversal:
use a list for the positive prefix sums
use a hashtable to store the first position of every flower
Solution

        positive_prefix_sum = [0]
        positions = {}
        maxsum = -inf

        for idx, flower in enumerate(flowers):
            positive_val = flower if flower >= 0 else 0
            negative_val = flower if flower < 0 else 0
            positive_prefix_sum += [positive_prefix_sum[-1] + positive_val]
            # in order to maximize the sum, we are only interested in
            # the first position of every element
            if not flower in positions:
                positions[flower] = idx
            else:
                # given that negative numbers are not part of the prefix sum,
                # we need to include them if they are the first / last items
                first_pos = positions[flower]
                newsum = 2 * negative_val + positive_prefix_sum[idx + 1] - positive_prefix_sum[first_pos]
        
                maxsum = max(maxsum, newsum)
        return maxsum
      
----------------------------------------------------------------
Pretty straight forward, just carry all positive flowers as prefix sum, save minimum carry value for each flower type as the left boundary and calculate every time we saw the same flower type (from the 2nd time, of course)
The only point need our attention is to check whether the first flower is not carried since it's a negative value.

Time Complexity: O(n)
Space Complexity: O(k), where k = number of unique flower types

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        flower_type2min_prefix = {}
        greedy_carry = 0  # only carry positive flowers
        ans = -inf
        for flower in flowers:
            if flower in flower_type2min_prefix:
                # need manual adjustment for first and last flower (especially for negative ones)
                ans = max(ans, greedy_carry - flower_type2min_prefix[flower] + flower + (flower if flower < 0 else 0))
                flower_type2min_prefix[flower] = min(flower_type2min_prefix[flower], greedy_carry)
            else:
                flower_type2min_prefix[flower] = greedy_carry
            if flower > 0:
                greedy_carry += flower
        return ans
