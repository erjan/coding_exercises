'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
'''


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        self.total_sum = 0
        
        for weight in w:
            self.total_sum += weight
            self.prefix_sums.append(self.total_sum)

    def pickIndex(self) -> int:
        random_target = self.total_sum * random.random()
        
        left, right = 0, len(self.prefix_sums)
        
        while left < right:
            middle = left + (right - left) // 2
            if self.prefix_sums[middle] >= random_target:
                right = middle
            else:
                left = middle + 1
        
        return left
