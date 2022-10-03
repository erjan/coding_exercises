'''
You are playing a solitaire game with three piles 
of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.
'''



class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c], reverse=True)
        ans = 0
        while a > 0 and b > 0:
            a -= 1
            b -= 1
            ans += 1
            a, b, c = sorted([a, b, c], reverse=True)
        return ans
      
--------------------------------------------------------------------

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        # importing heap module
        import heapq
        
        l1 = []
        
        # convert list into heap
        heapq.heapify(l1)
        
        # using max heap and push a,b,c into max heap
        heapq.heappush(l1, -1*a)
        heapq.heappush(l1, -1*b)
        heapq.heappush(l1, -1*c)
        
        # count variable to store steps
        count = 0
        while True:
            
            # poping biggest 2 piles
            ans1 = heapq.heappop(l1)
            ans2 = heapq.heappop(l1)
            
            # terminating condition, if either of one or both of them is equal to zero then return the steps
            if ans1 == 0 or ans2 == 0:
                return count
            
            # subtracting 1 stone from biggest 2 piles
            temp = abs(ans1) - 1
            temp1 = abs(ans2) - 1
            
            # again pushing modified values of piles into the heap
            heapq.heappush(l1, -1*temp)
            heapq.heappush(l1, -1*temp1)
            
            # incrementing the step number
            count += 1
