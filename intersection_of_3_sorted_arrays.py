'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly 
increasing order, return a sorted array of only the integers that appeared in all three arrays.
'''

#my own solution

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        arr1 = set(arr1)
        arr2 = set(arr2)
        arr3 = set(arr3)
        
        
        arr1.intersection_update(arr2)
        
        arr1.intersection_update(arr3)
        
        arr1 = list(arr1)
        arr1 = sorted(arr1)
        return arr1
      
      
#another

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))
      
      
      
#another 3 pointers

def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
	result = []
	i = j = k = 0
	
	while i<len(arr1) and j<len(arr2) and k<len(arr3):
		if arr1[i] == arr2[j] == arr3[k]:
			result.append(arr1[i])
			i, j, k = i+1, j+1, k+1
		elif arr1[i] < arr2[j]:
			i+=1
		elif arr2[j] < arr3[k]:
			j += 1
		else:
			k += 1
			
	return result


#another

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = arr1 + arr2 + arr3
        res = []
        freq = collections.Counter(result)
        for i, val in freq.items():
            if val == 3:
                res.append(i)
                
        return res
        
