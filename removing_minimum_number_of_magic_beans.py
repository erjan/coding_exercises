'''
You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.

Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.

Return the minimum number of magic beans that you have to remove.
'''


def minimumRemoval(self, beans: List[int]) -> int:
	beans.sort()
	s = sum(beans)
	l = len(beans)
	res = float('inf')

	for i in range(len(beans)):
		res = min(res, s - l * beans[i])
		l -= 1
		
	return res

-----------------------------------------------------------------------------------------------------------

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans = sorted(beans)
        S = sum(beans)
        min_operations = []
        for i in range(len(beans)):
            min_operations.append(S - beans[i] * (len(beans) - i))
            
        return sorted(min_operations)[0]

-------------------------------------------------------------------------------------------------------------------------------
