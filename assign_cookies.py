'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that 
the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we 
can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''


#my solution - after only watching the beginning of https://www.youtube.com/watch?v=EX2jEKJnzw4

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie_size = 0
        greed_factor = 0
        counter = 0
        while cookie_size < len(s) and greed_factor < len(g):
            if g[greed_factor] > s[cookie_size]:
                   cookie_size+=1

            else:
                greed_factor+=1
                cookie_size+=1
                counter+=1
        return (counter)

#TIP, INSIGHT from the wrong solution:

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counter=0
        for i in range(len(g)):
            
            for j in range(len(s)):
                if s[j] >= g[i]:
                    counter+=1
                    
        print(counter)
        
# here we need 2 pointers, cuz looping thru the array must happen in specific order! so we have to choose the approach of 2 pointers! 
# and not for loop, but while loop
        
