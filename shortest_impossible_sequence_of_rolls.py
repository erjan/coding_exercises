'''
You are given an integer array rolls of length n and an integer k. You roll a k sided dice numbered from 1 to k, n times, where the result of the ith roll is rolls[i].

Return the length of the shortest sequence of rolls that cannot be taken from rolls.

A sequence of rolls of length len is the result of rolling a k sided dice len times.

Note that the sequence taken does not have to be consecutive as long as it is in order.
'''

class Solution:
    def shortestSequence(self, rolls, k):
        res = 1
        s = set()
        for a in rolls:
            s.add(a)
            if len(s) == k:
                res += 1
                s.clear()
        return res
      
------------------------------------------------------------------------------------------------

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:

        z = set()
        res = 0

        for x in rolls:
            z.add(x)
            if len(z) == k:
                res += 1
                z.clear()
                
        return res + 1
