'''
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.
'''



"""ALGORITHM
TC = O(3n)  aprox = O(n)
Sc = O(n) for heap

Intution came to mind after reading the hint

** INTUTION ***
making an max heap with a copy of target.
then converting the the max heap array to >> arr mentioned in question
"""
"""
REFERENCE >> https://www.youtube.com/watch?v=voObxZxXoZw&t=0s  """

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        heap = []
        total = 0
        
        for i in range(len(target)):
            heap.append(-1 * (target[i]))
            total += target[i]
            
        heapq.heapify(heap)
                           
        while heap:
            
            maxVal = -1 * (heapq.heappop(heap))
            rem_sum = total - maxVal
                          
            if maxVal == 1 or rem_sum == 1:
                return True
            
            if rem_sum == 0 or maxVal < rem_sum:
                return False
                           
            newMaxVal = int(maxVal % rem_sum) #Changing operation for previous value 
            
            if newMaxVal == 0:  #value converted to less then 1
                return False
                           
            maxVal = newMaxVal  
            heapq.heappush(heap, -1 * (maxVal))
            total = newMaxVal + rem_sum
                           
        return True            
      
----------------------------------------------------------------------------------------------
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = list(map(lambda x: -x,target))
        heapq.heapify(heap)
        summ = sum(heap)
        while True:
            item = heapq.heappop(heap)
            if item == -1: return True
            summ-=item
            if item >= summ or summ == 0: return False
            item = item % summ if item % summ else summ
            if item > -1:
                return False
            heapq.heappush(heap,item)
            summ+=item
