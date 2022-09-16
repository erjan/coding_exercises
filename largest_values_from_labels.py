'''
There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

Choose a subset s of the n elements such that:

The size of the subset s is less than or equal to numWanted.
There are at most useLimit items with the same label in s.
The score of a subset is the sum of the values in the subset.

Return the maximum score of a subset s.

 
 '''

from collections import Counter
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        c = Counter()
        chosen = []
        for v, l in sorted(zip(values, labels), reverse=True):
            if l not in c or c[l] < use_limit:
                chosen.append(v)
                c[l] += 1
            if len(chosen) == num_wanted:
                break
        return sum(chosen)
      
----------------------------------------------------------------
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        labelsUsed = {}
        for label in set(labels):
            labelsUsed[label] = 0
        items = [(values[i], labels[i]) for i in range(len(values))]
        items.sort(reverse=True)
        score = 0
        for item in items:
            if numWanted == 0:
                return score
            if labelsUsed[item[1]] < useLimit:
                labelsUsed[item[1]] += 1
                score += item[0]
                numWanted -= 1
        return score
---------------------------------------------------------------------
def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
	d = defaultdict(int)
	ans = 0
	l = numWanted
	for i, j in sorted(list(zip(values, labels)), reverse = True):
		if(d[j] < useLimit and l):
			l -= 1
			d[j] += 1
			ans += i
	return ans
