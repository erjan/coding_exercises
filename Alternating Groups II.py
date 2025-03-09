'''

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
'''

---------------------------------------
#wrong solution
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)


        upper = colors[:k-1]
        colors.extend(upper)
        left = 0
        res = 0



        for i in range(n-k+1):
            subarray = colors[i:i+k]

            status = True
            if subarray[0] == 1:
                for i in range(len(subarray)-1):
                    if subarray[i:i+1] == [0,1]:
                        status = False
                        break
            elif subarray[0] == 0:
                for i in range(len(subarray)-1):
                    if subarray[i:i+1] == [1,0]:
                        status = False
                        break

            if status:
                res+=1
        
        return res

--------------------------------------------------------------------------------
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        colors.extend(colors[:(k-1)])
        left = 0
        count = 0
        
        n = len(colors)

        for i in range(n):
            if i > 0 and colors[i] == colors[i-1]:
                left = i
                
            if i - left + 1 >= k:
                count+=1

        return count
          
