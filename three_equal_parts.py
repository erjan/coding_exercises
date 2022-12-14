'''
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
'''


class Solution:
    def threeEqualParts(self, arr):
        ones, remain = divmod(arr.count(1), 3)

        if remain != 0: return [-1, -1]  # can not be divided equally
        if ones == 0: return [0, 2]  # all zero

        L, tail_zero_cnts = len(arr), arr[::-1].index(1)

        I, J, cnt = 0, L - 1, 0
        for i in filter(arr.__getitem__, range(L)):  # for all ones
            cnt += 1
            if cnt == ones:
                I = i + tail_zero_cnts
            if cnt == 2 * ones:
                J = i + tail_zero_cnts
                break

        if int(''.join(map(str, arr[:I + 1]))) == int(''.join(map(str, arr[I + 1:J + 1]))) == int(''.join(map(str, arr[J + 1:]))):
            return [I, J + 1]

        return [-1, -1]
----------------------------------------------------------------------------------------------------------------------------------------
def threeEqualParts(self, arr: List[int]) -> List[int]:
	n = len(arr)
	pos = [i for i in range(n) if(arr[i])]
	l = len(pos)
	if(l == 0):
		return [0, 2]
	if(l % 3):
		return [-1, -1]
	ones = l//3
	c = 0
	for i in arr[::-1]:
		if(i == 1):
			break
		c += 1
	ans = [-1, -1]
	# one hoga pos[ones-1] tak
	# uske bad chaiye meko c zeros
	# toh index pos[ones-1] + c tak first segment ho jayega
	ans[0] = pos[ones-1] + c
	ans[1] = pos[2*ones-1] + c + 1
	seg1, seg2, seg3 = arr[pos[0]:ans[0]+1], arr[pos[ones]:ans[1]], arr[pos[2*ones]:]
	# without leading zeros
	if(seg1 != seg2 or seg1 != seg3):
		return [-1, -1]
	return ans
