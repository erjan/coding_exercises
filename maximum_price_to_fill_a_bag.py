'''
You are given a 2D integer array items where items[i] = [pricei, weighti] denotes the price and weight of the ith item, respectively.

You are also given a positive integer capacity.

Each item can be divided into two items with ratios part1 and part2, where part1 + part2 == 1.

The weight of the first item is weighti * part1 and the price of the first item is pricei * part1.
Similarly, the weight of the second item is weighti * part2 and the price of the second item is pricei * part2.
Return the maximum total price to fill a bag of capacity capacity with given items. If it is impossible to fill a bag return -1. Answers within 10-5 of the actual answer will be considered accepted.
'''

'''
Intuition
Greedily take items (or their parts) with a highest price/weight ratio.

Approach
Since all items can be split into parts, we can always replace a part of an item with a lower price/weight ratio with a part of an item with a higher price/weight ratio.

Specifically, if price[i] / weight[i] > price[j] / weight[j] and we take some part[j] > 0 of items[j] but don't take all of items[i] (part[i] < 1), then an exchange argument applies.

Consider two other solutions:

with part[i] = 1, and part[j] = x. Find x from the weight condition:
weight[i] * part[i] + weight[j] * part[j] = weight[i] * 1 + weight[j] * x
implying x = weight[i] / weight[j] * (part[i] - 1) + part[j]
with part[i] = y, and part[j] = 0. Find y from the weight condition:
weight[i] * part[i] + weight[j] * part[j] = weight[i] * y + weight[j] * 0
implying y = part[i] + weight[j] / weight[i] * part[j]
Exercise: show that either x >= 0 or y <= 1, meaning that at least one of these solutions is actually valid and does not exceed the capacity. Hint: both conditions transform into a comparison of the form part[j] * weight[j] + part[i] * weight[i] v weight

Exercise: show that both solutions improve upon the total price. Hint: the gain of both solutions is proportional to price[i] / weight[i] - price[j] / weight[j] > 0

Therefore, if we ever take a part of some item, then

all items with bigger price/weight ratio are fully taken;
none of the items with smaller price/weight ratio are taken at all.
This result prompts us to come up with the following algorithm: sort items by price/wieght ratio descending, then take as much of each item as we can (either by fully taking it, or by filling the capacity).

Note: if you got some spare capacity at the end, the problem required to return -1 for rather unclear reasons.

Complexity
Time complexity: O(sort). Can be less than O(nlog⁡n)O(n \log n)O(nlogn) if we use counting sort.

Space complexity: O(sort). Depends on the language and the sorting algorihm used.


'''

class Solution:
    def maxPrice(self, items: list[list[int]], capacity: int) -> float:
        score = 0
        ratio = lambda item: item[0] / item[1]
        for price, weight in sorted(items, key=ratio, reverse=True):
            take = min(weight, capacity)
            score += price * take / weight
            capacity -= take
        return -1 if capacity else score
