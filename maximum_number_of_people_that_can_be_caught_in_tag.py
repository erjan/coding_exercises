'''
You are playing a game of tag with your friends. In tag, people are divided into two teams: people who are "it", and people who are not "it". The people who are "it" want to catch as many people as possible who are not "it".

You are given a 0-indexed integer array team containing only zeros (denoting people who are not "it") and ones (denoting people who are "it"), and an integer dist. A person who is "it" at index i can catch any one person whose index is in the range [i - dist, i + dist] (inclusive) and is not "it".

Return the maximum number of people that the people who are "it" can catch.
'''


Binary Search
put every zero into a sorted list
for every one, binary search the left most zero index and count it
Time O(NlogN) -> O(N^2) array.pop(i) in python takes O(N) but it is a fast O(N)
Space O(N)
3455 ms, faster than 100.00% for now

from bisect import *

class Solution:
    def catchAllPeople(self, team: List[int], dist: int) -> int:
        n = len(team)
        zeros = []
        for i in range(n):
            if team[i] == 0:
                zeros.append(i)
        res = 0
        for i in range(n):
            if team[i] == 0:
                continue
            j = bisect_left(zeros, i-dist)
            if 0 <= j < len(zeros) and i-dist <= zeros[j] <= i+dist:
                res += 1
                zeros.pop(j)
        return res
Queue
Then, I realized that because i go forward one by one, if i remove the leftmost out-of-bound indices, it should also work. So, I dit it with a queue

Time O(N)
Space O(N)
1040 ms, faster than 100.00%

from collections import deque

class Solution:
    def catchAllPeople(self, team: List[int], dist: int) -> int:
        n = len(team)
        zeros = deque()
        for i in range(n):
            if team[i] == 0:
                zeros.append(i)
        res = 0
        for i in range(n):
            if team[i] == 0:
                continue
            while len(zeros) > 0 and zeros[0] < i-dist:
                zeros.popleft()
            if len(zeros) > 0 and zeros[0] <= i+dist:
                zeros.popleft()
                res += 1
        return res
        
----------------------------------------


Intuition
When seeing dist being there, I know it has something to do with eliminating the outdated elements. It can surely be solved using a deque, but I decided to give it a second thought and it turns out that I found something different.

The code turned out to be highly symmetrical and easy to understand.

Explanation
There are only 0 and 1 in the team, if 0 is not seen, then you must be seeing 1, vice versa
Based on above knowledge, we will approach the question with a Greedy way, that is:
Always catch the earliest possible not_it with the earliest possible it
For example:
team = [1,0,0,0,0,1,1,0,0,0,1], dist = 2
Catch not_it at i = 1 with it at i = 0
Catch not_it at i = 3 with it at i = 5
Catch not_it at i = 4 with it at i = 6
Catch not_it at i = 8 with it at i = 10
Why not catch not_it at i = 7 with it at i = 10? Because dist = 2.
How to eliminate the outdated it or not_it?
Sure, an intuitive way is to use double-ended queue (deque), but in this scenario, it's a bit overkill
Because here we care about how many rather than which one, so we just need to make sure the count of it or not_it are in the range of [0, dist] (inclusive)
Time Complexity: O(N)
Space Complexity: O(1)
Implementation
class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        not_it = it = ans = 0
        for _, is_it in enumerate(team):
            if is_it:                   # if is `it`
                if not_it > 0:          #     if there are some non-caught `not_it`, try catch it
                    not_it -= 1
                    ans += 1            #     and count people caught
                else:
                    it += 1             #     if there are no non-caught `not_it`, increase count of `it`
            else:                       # it not `it`
                if it > 0:              #     if there are enough "catch quota" leftover, use them (catch `not_it` before previous index)
                    it -= 1 
                    ans += 1            #     decrease count of `it` and count people caught
                else:                   
                    not_it += 1         #     if there are no quota to catch `not_it`, increase count of `not_it`
            not_it = min(not_it, dist)  # eliminate outdated `not_it` by limiting its count under `dist`
            it = min(it, dist)          # eliminate outdated `it` by limiting its count under `dist`
        return ans
---------------------------------------------------------


class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        ans = 0 
        q0, q1 = deque(), deque()
        for i, x in enumerate(team): 
            if q0 and q0[0] < i-dist: q0.popleft()
            if q1 and q1[0] < i-dist: q1.popleft()
            if x == 0: 
                if q1: 
                    ans += 1
                    q1.popleft()
                else: q0.append(i)
            else: 
                if q0: 
                    ans += 1
                    q0.popleft()
                else: q1.append(i)
        return ans 
        
