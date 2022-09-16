'''
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.
'''

def numRabbits(self, ans: List[int]) -> int:
		result=0
		d=Counter(ans)    # Inbuilt function to form dictionary/Map
		for i,j in d.items():
			if j>i+1:    
				temp=ceil(j/(i+1))
				result+= temp*(i+1)
			else:
				result+= i+1
		return result
  
-----------------------------------------------------------------------
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        res = 0
        d = {}
        for i in range (n):
            try:
                d[answers[i]] += 1
            except:
                d[answers[i]] = 1
        for x in d:
            while d[x] >= x+1:
                print(res, "res at ",x)
                res += (x+1)
                d[x] = d[x] - (x+1)
            else:
                if d[x] > 0:
                    res += (x+1)
        return res
