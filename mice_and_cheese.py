'''
There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.

A point of the cheese with index i (0-indexed) is:

reward1[i] if the first mouse eats it.
reward2[i] if the second mouse eats it.
You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.

Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.
'''









'''
The first mice will eat exactly k types, and the second mice will eat others.
Sort reward1 - reward2 in descending order. Let the first mice eat those types with highest difference.
'''

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = [[reward1[i] - reward2[i], i] for i in range(len(reward1))]
        diff.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += reward1[diff[i][1]]
        for i in range(k, len(reward1)):
            ans += reward2[diff[i][1]]
        return ans
