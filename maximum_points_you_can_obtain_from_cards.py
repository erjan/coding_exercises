'''
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # Take the k left most elements to start
        best = score = sum(cardPoints[:k])
        
        for i in range(1, k+1):
            
            # Lose an element from the left, add an element from the right
            score = score - cardPoints[k-i] + cardPoints[-i]
            best = score if score > best else best
            
        return best
-------------------------------------------------      

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        remaining_length = n - k
        subarray_sum = sum(cardPoints[:remaining_length])
        
        min_sum = subarray_sum
        for i in range(remaining_length, n):
            # Update the sliding window sum to the subarray ending at index i
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - remaining_length]
            # Update min_sum to track the overall minimum sum so far
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum
      
------------------------------------------
class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        sm=sum(card[:k])
        mx=sm
        for i in range(1,k+1):
            sm=sm+card[-i]-card[k-i]
            mx=max(mx,sm)
        return mx
