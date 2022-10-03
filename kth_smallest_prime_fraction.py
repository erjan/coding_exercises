'''
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
'''

class Solution:

	def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
		if len(arr) > 2:
			res = []  # list for storing the list: [prime fraction of arr[i]/arr[j], arr[i], arr[j]]

			for i in range(len(arr)):
				for j in range(i + 1, len(arr)):
					# creating and adding the sublist to res
					tmp = [arr[i] / arr[j], arr[i], arr[j]]
					res.append(tmp)

			# sorting res on the basis of value of arr[i] 
			res.sort(key=lambda x: x[0])

			# creating and returning the required list
			return [res[k - 1][1], res[k - 1][2]]
		else:
			return arr
    
---------------------------------------

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pairs = []
        ll = len(arr)
        for i in range(ll):
            for j in range(ll):
                if(i==j):
                    continue
                pairs.append([arr[i],arr[j]])
        
        return sorted(pairs, key=lambda x: x[0]/x[1])[k-1]
        
        
---------------------------------------------------------------------------------------------------------------

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            x=arr[i]
            y=arr[j]
            l.append([[x,y],arr[i]/arr[j]])
    l.sort(key = lambda x:x[1])
    return l[k-1][0]
