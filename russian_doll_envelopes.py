'''
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.
'''

def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    # sort in one property and find the longest increasing subsequence
    # in the other property, that's it
    # to avoid cases such as [(3, 4), (3, 6)] - output should be 1
    # sort the (w) in ascending and (h) in descending

    #let's sort in second property(h) and then find LIS using first property(w)
    ln = len(envelopes)
    if ln <= 1:
        return ln
    
    envelopes = sorted(envelopes, key=lambda x:(x[1], -x[0]))
    #now find the LIS
    q = [envelopes[0][0]]
    
    for i in range(1, ln):
        num = envelopes[i][0]
        if q[-1] < num:
            q.append(num)
        elif q[-1] > num:
            # use binary search 
            idx = self.upperbound(q, num)
            q[idx] = num
    
    return len(q)

def upperbound(self, ls, num):
    ln = len(ls)
    s, e = 0, ln-1
    while s <= e:
        mid = (e-s)//2 + s
        if ls[mid] == num:
            #we can or we don't have to replace this
            return mid
        elif ls[mid] < num:
            if mid+1 < ln and ls[mid+1] > num:
                return mid+1
            s = mid + 1
        else:
            if mid == 0:
                return mid
            e = mid-1
            
------------------------------------------------------------------------------

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for envelope in envelopes:
            idx = self.findFisrtLarge(envelope, stack)
            if idx == -1:
                stack.append(envelope[1])
            else:
                stack[idx] = envelope[1]
        return len(stack)
        
    def findFisrtLarge(self, target, stack):
        left, right = 0, len(stack)-1
        while left <= right:
            mid = left + (right-left)//2
            if stack[mid]>=target[1]:
                if mid == 0 or stack[mid-1]<target[1]:
                    return mid
                else:
                    right = mid -1
            else:
                left = mid + 1
        return -1
