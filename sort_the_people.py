'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        d = dict(zip(heights, names))
        
        d = sorted(d.items() , key = lambda x: -x[0])
        
        d = [v for k,v in d]
        return d

---------------------------------------------------------

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {heights[i] : names[i] for i in range(len(names))}
        heights.sort(reverse=True)
        for i in range(len(heights)):
            names[i] = d[heights[i]]
        return names
      
-----------------------------------------------

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]: 
        l=[]
		## making the pairs of both the elements of same indeces of heights and names and storing in list l
        for i in range(len(names)):
            l.append([names[i],int(heights[i])])
			
		## now sorting the pair list l according to the heights, with the help of lambda function
		## BELOW  l[i][1] == x[1] , which has heights stored at 1th index
		## and -x[1] is sorting the heights in decreasing order cause of negative sign
		
        l.sort(key=lambda x:(-x[1]))
        d=[]
        for i in l:
            d.append(i[0])
        return d
