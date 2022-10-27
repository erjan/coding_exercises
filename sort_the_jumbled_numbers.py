'''
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
'''

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def tval(val):
            val = str(val)
            return int("".join([ str(mapping[int(val[i])]) for i in range(len(val))]))
        nums.sort(key = lambda e:tval(e))
        return nums
      
------------------------------------------------------------------------------------------------------------
class Solution:
	def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
		res = []
		for num in nums:
			ans = ""
			for char in str(num):
				ans += str(mapping[int(char)])
			res.append(int(ans))
		final = list(zip(nums, res))
		final = sorted(final, key=lambda x: x[1])
		return [tup[0] for tup in final]
  
------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        m = { str(i): str(v) for i, v in enumerate(mapping) }

        def mapFunc(n):
            return int(''.join(m[i] for i in str(n)))
                
        return sorted(nums, key=mapFunc)

