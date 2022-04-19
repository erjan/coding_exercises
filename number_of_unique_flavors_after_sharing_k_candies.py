'''
You are given a 0-indexed integer array candies, where candies[i] represents the flavor of the ith candy. Your mom wants you to share these candies with your little sister by giving her k consecutive candies, but you want to keep as many flavors of candies as possible.

Return the maximum number of unique flavors of candy you can keep after sharing with your sister.

 

Example 1:

Input: candies = [1,2,2,3,4,3], k = 3
Output: 3
Explanation: 
Give the candies in the range [1, 3] (inclusive) with flavors [2,2,3].
You can eat candies with flavors [1,4,3].
There are 3 unique flavors, so return 3.
Example 2:

Input: candies = [2,2,2,2,3,3], k = 2
Output: 2
Explanation: 
Give the candies in the range [3, 4] (inclusive) with flavors [2,3].
You can eat candies with flavors [2,2,2,3].
There are 2 unique flavors, so return 2.
Note that you can also share the candies with flavors [2,2] and eat the candies with flavors [2,2,3,3].
Example 3:

Input: candies = [2,4,5], k = 0
Output: 3
Explanation: 
You do not have to give any candies.
You can eat the candies with flavors [2,4,5].
There are 3 unique flavors, so return 3.
 
 '''


Move the k-size window from left and right and keep updating the counter ctr which counts the number of each unique candy.
When the left end candy's count change from 0 to 1, increase the cnt by 1 (You get that candy back from your sister)
When the right end candy' count change from 1 to 0, decrease the cnt by 1 (You share this candy to your sister)

def shareCandies(candies: List[int], k: int) -> int:
	ctr = collections.Counter(candies[k:])
	ans = cnt = sum(v != 0 for v in ctr.values())
	for i, x in enumerate(candies[k:]):
		ctr[x] -= 1
		cnt += (ctr[candies[i]] == 0) - (ctr[x] == 0)
		ctr[candies[i]] += 1
		ans = max(ans, cnt)
	return ans

--------------------------------------------------------------------------------------------------
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return len(set(candies))
        
        d = Counter(candies)
        left = 0
        ans = 0
         
        for right, candie in enumerate(candies):
            d[candie] -= 1
            
            if d[candie] == 0:
                del d[candie]
                
            if right - left + 1 == k:
                ans = max(ans, len(d))
                leftCandie = candies[left]
                d[leftCandie] = d.get(leftCandie, 0) + 1 
                left += 1
        
        return ans
      
-----------------------------------------------------------------------------------------
Begin by counting how many of each flavor candy there is. We do this in the form of a hashmap. Next we initialize our starting window of size k, then interate over our candies using this logic: For every candy we add to our window, we remove a flavor from the general set of candies. For every candy we remove from our window, we add to our general set of candies. If we remove all of our candies for a flavor, remove the key from the map. If we ecounter a candy we have removed from our map, add it back in and reinitialize it to 1. The max # of keys in we've encountered at any given window is our answer.

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        candy_map = {}
        
        for candy in candies:
            if candy in candy_map:
                candy_map[candy] += 1
            else:
                candy_map[candy] = 1
        
        for i in range(k):
            candy_map[candies[i]] -= 1
            if candy_map[candies[i]] == 0:
                del candy_map[candies[i]]
        
        unique_candies = len(candy_map)
            
        for i in range(1, len(candies)-k+1):
            if candies[i-1] not in candy_map:
                candy_map[candies[i-1]] = 1
            else:
                candy_map[candies[i-1]] += 1
            if candy_map[candies[i+k-1]] == 1:
                del candy_map[candies[i+k-1]]
            else:
                candy_map[candies[i+k-1]] -= 1
            unique_candies = max(unique_candies, len(candy_map))
        
        return unique_candies
---------------------------------------------------------------------------------------------------
Explanation
Count frequency of each flavor (number)
Imagine a window of size k, slide the window to the right
Decrease the frequency of the flavor when the flavor enter the window from the right side
Increase the frequency of the flavor when the flavor leave the window from the left side
Maintain a cur variable to count current maximum flavor left
Return the maximum possible cur
Implementation
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        c = collections.Counter(candies)
        if not k: return len(c)
        
        cur = len(c)
        for i in range(k):                  # Initialize window of length `k`
            c[candies[i]] -= 1
            if not c[candies[i]]: cur -= 1
                
        ans = cur
        for i in range(k, len(candies)): 
            c[candies[i]] -= 1              # decrease frequency when flavor enter the window
            c[candies[i-k]] += 1            # increase frequency when flavor enter the window
            if c[candies[i-k]] == 1 and \
                candies[i-k] != candies[i]: # adjust `cur` accordingly
                cur += 1
            if not c[candies[i]]:           # adjust `cur` accordingly
                cur -= 1
            ans = max(cur, ans)
        return ans
You can also get rid of cur by tracing the size of counter

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        c = collections.Counter(candies)
        if not k: return len(c)
        
        for i in range(k):
            c[candies[i]] -= 1
            if not c[candies[i]]: 
                del c[candies[i]]
                
        ans = len(c)
        for i in range(k, len(candies)):                
            c[candies[i]] -= 1
            c[candies[i-k]] += 1
            if not c[candies[i]]:
                del c[candies[i]]
            ans = max(ans, len(c))
        return ans
      
      
