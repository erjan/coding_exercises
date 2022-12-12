'''
Winston was given the above mysterious function func. He has an integer array arr and an integer target and he wants to find the values l and r that make the value |func(arr, l, r) - target| minimum possible.

Return the minimum possible value of |func(arr, l, r) - target|.

Notice that func should be called with the values l and r where 0 <= l, r < arr.length.
'''


class SegmentTree:
    def __init__(self, values):
        self.data = [0 for _ in values] + values
        self.n = len(values)

        for idx in reversed(range(1, self.n)):
            self.data[idx] = self.data[2*idx] & self.data[2*idx+1]


    def query(self, left, right):                            
        if left>right:
            return -1000000000
            
        right += 1
        left += self.n
        right += self.n
        ans = self.data[left]

        while left < right:
            if left % 2:
                ans = ans & self.data[left]
                left += 1
            if right % 2:
                right -= 1                               
                ans = ans & self.data[right]
            left //= 2
            right //= 2

        return ans
    

class Solution:
    
    def SlidingWindow(self, arr, target):
        
        st = SegmentTree(arr)
        l = 0
        r = 0
        ans = target + 10**9    # base case when l>r
    
        
        while r<len(arr):
            v = st.query(l, r)
            ans = min(ans, abs(v-target))
            
            if v>=target:
                r+=1
            else:
                if l<r:
                    l+=1
                else:
                    l+=1
                    r+=1
                  
        return ans
    
----------------------------------------------------------------------
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans, seen = inf, set()
        for x in arr: 
            tmp = set() #new set 
            seen.add(0xffffffff)
            for ss in seen:
                ss &= x
                ans = min(ans, abs(ss - target))
                if ss > target: tmp.add(ss) #fine tuning 
            seen = tmp
        return ans 
        
        
        
