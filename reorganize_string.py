'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
'''


import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if S == "":
            return "" 
        
        # create a counter 
        d = collections.Counter(S)
        
        heap = []
        for key, value in d.items():
            heapq.heappush(heap,[-value,key])
        
        res = ""
        pre = heapq.heappop(heap)
        res+= pre[1]

        while heap: 
            curr = heapq.heappop(heap)
            res+=curr[1]
            
            pre[0]+=1
            if pre[0]<0:
                heapq.heappush(heap,pre)
            pre = curr 
            
        if len(res)!=len(S):
            return ""
        else:
            return res
          
-------------------------------------------------------------------
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:        
        maxHeap = []
        res = []
        prev = None
        
        # Use Counter() to build a maxHeap with priority key as the count of the char
        count = collections.Counter(s)
        for char, count in count.items():
            heappush(maxHeap, (count * -1, char))
            
        while maxHeap:
            count, char = heappop(maxHeap)
            count +=1 # Since it's a maxHeap we increment count to 'count down'
            res.append(char)
            
            # Push the element from previous iteration to heap 
            # since we can reuse the char after appending a different char to res
            if prev:
                heappush(maxHeap, prev)
                
            # Set prev to current element since we can't reuse it just yet
            # or not if count for the char is 0
            if count == 0:
                prev = None
            else:
                prev = (count, char)
        
        # If we have a prev value then there are too many of the same char to return 
        # a solution that fit the requirement
        return "" if prev else "".join(res)
