'''
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
'''



class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # Initialize the left and right boundaries.
        # left = 1 and right = (total sweetness) / (number of people).
        number_of_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // number_of_people
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # cur_sweetness stands for the total sweetness for the current person.
            # people_with_chocolate stands for the number of people that have 
            # a piece of chocolate of sweetness greater than or equal to mid.  
            mid = (left + right + 1) // 2
            cur_sweetness = 0
            people_with_chocolate = 0
            
            # Start assigning chunks to the current person.
            for s in sweetness:
                cur_sweetness += s
                
                # If the total sweetness is no less than mid, this means we can break off
                # the current piece and move on to assigning chunks to the next person.
                if cur_sweetness >= mid:
                    people_with_chocolate += 1
                    cur_sweetness = 0

            if people_with_chocolate >= k + 1:
                left = mid
            else:
                right = mid - 1
                
        return right
      
--------------------------------------------------------------------------------------------------------
# time O(n log n)
# space O(1)
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        min_sweet, max_sweet = min(sweetness), sum(sweetness) // (k + 1)
        while min_sweet < max_sweet:
            mid = min_sweet + (max_sweet - min_sweet + 1) // 2 # +1 for base the mid to the right, for finding `maximum` answer
            if self.cutChoco(sweetness, mid) > k:
                min_sweet = mid
            else:
                max_sweet = mid - 1
        return min_sweet
    
    def cutChoco(self, sweetness, sweet):
        currSweet, cuts = 0, 0
        for s in sweetness:
            if currSweet + s >= sweet:
                cuts += 1
                currSweet = 0
            else:
                currSweet += s
        return cuts
      
-------------------------------------------------------------
class Solution:
    def maximizeSweetness(self, sweetness: List[int], bars: int) -> int:
        if bars == 0:
            return sum(sweetness)
        s = sum(sweetness)
        low =  min(sweetness)
        high = int(s//bars)
        
        
        res = 0
        while low <= high:
            mid = int(low + (high-low)//2)
            barL = []
            curBar = 0
            minB = 0
            for chunk in sweetness:
                curBar += chunk
                if curBar >= mid:
                    barL.append(curBar) 
                    curBar = 0
                
            if len(barL) >= bars+1:
                res = max(res, min(barL))
                low = mid + 1
            else:
                high = mid -1
        
        return res
      
----------------------------------------------------------------------------------
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        total_persons = k + 1
        
        def is_possible(sweet: int) -> bool: # check that all pieces are at least as sweet as `sweet`.
            curr_sweet, pieces = 0, 0
            for s in sweetness:
                curr_sweet += s
                if curr_sweet >= sweet: # sweet enough
                    pieces += 1 # cut; add a piece
                    curr_sweet = 0 # reset sweetness
            return pieces >= total_persons
        
        min_sweet, max_sweet = min(sweetness), sum(sweetness) // total_persons
        while min_sweet < max_sweet:
            curr_sweet = min_sweet + (max_sweet - min_sweet) // 2 + 1 # add one; try for sweeter one
            if is_possible(curr_sweet):
                min_sweet = curr_sweet
            else:
                max_sweet = curr_sweet - 1 # `max_sweet` should be less than `curr_sweet` since `curr_sweet` is not possible to get
        return max_sweet
      
------------------------------------------------------------------------------------------------------
Basically let's denote the values of each split to be v_1, v_2, ..., v_k+1 and we want to maximize the value, say val, we can get such that val <= v_i for i in 1...k+1.

We want first to take a greedy approach where we go through sweetness array and cut once our current split v_curr>=val so that we make sure val <= v_i for i in 1...k+1 and in the end we make cuts number of cut.

Notice that cuts * val is proportional to k * max_val where max_val is the max value we can get. If cuts > k, it means val < max_val, and vice versa if cut <= k, it means val >= max_val. And this is where binary search comes in. The possible number for val is between 1 and sum(sweetness)//(K+1) (the average sweetness) and we want to search for max_val.

Runtime: O(nlog(avg(sweetness)))
Space: O(1)

def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
	     l, r = 1, sum(sweetness) // (K+1)
        while l <= r:
            mid = (l+r)//2
            total, cut = 0, 0
            for num in sweetness:
                total += num
                if total >= mid:
                    cut += 1
                    total = 0
            if cut > K:
                l = mid + 1
            else:
                r = mid - 1
        return r
