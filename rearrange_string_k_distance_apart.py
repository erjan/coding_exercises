'''
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".

 

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
'''

import heapq
from collections import deque
from collections import Counter
class Solution:
    def rearrangeString(self, s: 'str', k: 'int') -> 'str':
        if k == 0:
            return s
        counter = Counter(s)
        queue = [[-counter[char], char] for char in counter]
        heapq.heapify(queue)
        mem = deque()
        
        res = ''
        while len(queue) or len(mem):
            if len(mem) == k:
                current = mem.popleft()
                if current[0] < 0:
                    heapq.heappush(queue, current)
            if len(queue):
                current = heapq.heappop(queue)
                res += current[1]
                current[0] += 1
                mem.append(current)
            else:
                if sum([item[0] for item in mem]) == 0:
                    return res
                else:
                    return ''
                  
-----------------------------------------------------------------
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        ## RC ##
        ## APPROACH : GREEDY ##
        ## Similar to Leetcode: 621. Task Scheduler ##
        ## LOGIC ##
        """
         1. go through Task Scheduler problem first, https://leetcode.com/problems/task-scheduler/discuss/699297/Python-Very-detailed-explanation-with-examples
         2. Here the number of slots will be, Maximum freq number. ( consider a:4, b:4, c:4, d:2 )
         3. WATCH OUT, lets say for now there is no K given, fill all the slots. (Intially I was limiting my slot size to only k, question says minimum distance should be k, it doesn't matter if it is greater than k )
         4. a b c d
            a b c d
            a b c _
            a b c _
         5. another case: a:6, b:2, c:2 ( rearrange not possible )
            a b
            a b
            a c
            a c
            a 
            a
         After filling the slots when you try to join them, slot5 and slot6 are not k-distant apart, so we return false.
         6. But edge case comes : a:3, b:2, c:1, e:1
            a b e
            a b 
            a c
            This is wrong combination.
        If you carefully analyze, we donot actually care about last row if it has k characters or not. so we fill only till maxFreq - 1
            correct combination:
            a b c
            a b e
            a
         
         Time Complexicity : O(N) + O(26Log26) (sort)
        """
        
        counter = collections.Counter(s)
        items = sorted( [ (freq, ch) for ch,freq in counter.items() ] )
        maxFreq = items[-1][0]
        slots = [ "" for _ in range(maxFreq) ]
        
        slot = 0
        while( items ):
            freq, ch = items.pop()
            if( freq == maxFreq ):
                for i in range(maxFreq):
                    slots[i] = slots[i] + ch
            else:
                while( freq ):
                    slot = slot % (maxFreq-1)
                    slots[ slot ] = slots[ slot ] + ch
                    freq -= 1
                    slot += 1
        for i in range(maxFreq-1):  # up until last slot
            if len(slots[i]) < k:
                return ""
        return "".join(slots)
      
      ---------------------------------------------------------------------------
      This is a follow-up question from #767 (solution).

If you have understood the question and solution above,
to solve this question we just need to add a doubly-edge queue in order to maintain the k-distance.

O(n log m) with m represents the number of characters in heap.
Since there are only 26 possible characters, m is a constant value.
Thus the runtime complexity becomes O(n).

from collections import Counter, deque
from heapq import heapify, heappush, heappop

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k<2: return s
        q = deque([]) #to maintain used char, keep size k-1
        h = [(-count,ch) for ch,count in Counter(s).items()]
        heapify(h)
        
        ans = []
        while h:
            count, ch = heappop(h)
            ans.append(ch)
            if q and len(q) == k-1:
                next_item = q.popleft()
                if next_item[0] < 0:
                    heappush(h, next_item)
            q.append(( count+1, ch ))
        if len(ans) != len(s): return ""
        return ''.join(ans)
      
----------------------------------------------------------------------
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s        
        
        counter = Counter([c for c in s])
        
        # h - maxheap of (count, letter)
        h = [(-count, letter) for letter, count in counter.items()]
        heapq.heapify(h)
        
        answer = []
        
        # greedy - get the letter with max count from heap,
        # keep letter in queue (max size k) that cannot be used
        q = deque()
        while h:
            e = heapq.heappop(h)
            count, letter = -e[0], e[1]
            answer.append(letter)
            q.append((count - 1, letter))
                
            if len(q) >= k:
                count, letter = q.popleft()
                if count > 0:
                    heapq.heappush(h, (-(count), letter))
        
        # if any letters still in queue - its failure
        for e in q:
            if e[0] != 0:
                return ""
        
        return ''.join(answer)
        
        
-----------------------------------------------------------------------------
class Solution(object):
    def rearrangeString(self, s, k):
        # 1. We first need to know the frequency of each letter as later we will start with the most frequent charecter
        if k == 0: return s
        counter = Counter(s)
        # we want to have access to the high frequency charecters so we make a max heap
        #================================================================================================
        # 2.A . From here one way of solving the problem is to use max heap and alternate between two most 
        # freqeuent charecter at each time. The complexity of this approach is nlog(n)      
        maxheap = []
        for key, value in counter.items():
            heapq.heappush(maxheap, [-value, key])
        res = ""
        q = deque()
        while maxheap:
            freq, ch = heapq.heappop(maxheap)
            res += ch
            q.append([freq+1, ch])
            if len(q) == k: 
                freq, ch = q.popleft()
                if freq < 0:
                    heapq.heappush(maxheap, [freq, ch])            
        if len(s) != len(res):
            return ""
        return res
        #=======================================================================================================
        # 2.B. The next approach is to use bucket sort
        # in bucket sort we make a bucket based on the frequency of each character
        """
        max_freq = max(counter.values())
        #================================================
        # Let's the maximum frequency is 3 and k is 4.
        # We have to at least have 2 (max_freq - 1) |---|---| and some space 
        # after to hold the charecters with maximum frequency. What is the minimum
        # number of space we need after those two ? That will be the number of charecters
        # with maximum frequency. In our example let's say both a and b have the maximum
        # frequency of 2.
        # |ab-|ab-|ab & anything else we have with a freqency lower than 3 can be placed in the 
        # rest of spaces.
        #====================================================
        if (max_freq - 1) * k + counter.values().count(max_freq) > len(s):
            return ""
        buckets = [[] for _ in range(max_freq + 1)]
        for ch, freq in counter.items():
            buckets[freq].append(ch)
        idx = (len(s) - 1) % k # We start from the element that will fill the last element of our array
        res = []
        bidx = max_freq
        ans = list(s)
        # we go over the buckets starting from the bucket with highest frequency
        # we put charecters with distance of 2 first, the initial index is zero
        # in next round we start from index 1.
        while bidx > 0:
            # if the bucket is empty there were no charecter with that frequency
            if len(buckets[bidx]) < 1:
                bidx -= 1
                continue
            # putting the same charecters with distance of two
            for ch in buckets[bidx]:
                for i in range(bidx):
                    ans[idx] = ch
                    idx += k
                    if idx > len(ans) - 1:
                        idx = (idx - 1) % k
            # moving to the next bucket
            bidx -= 1                
        return ''.join(ans)
        """
	```

        
      
      
