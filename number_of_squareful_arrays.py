'''
An array is squareful if the sum of every pair of adjacent elements is a perfect square.

Given an integer array nums, return the number of permutations of nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].
'''

class Solution:
	def numSquarefulPerms(self, nums: List[int]) -> int:
		def is_perfect(v):
			k=int(math.sqrt(v))
			return k*k==v
		nums.sort()
		def perm(A,prev):
			if len(A)==0:
				self.res+=1
				return 
			for j in range(len(A)):
				if j>0 and A[j]==A[j-1]:continue
				if prev is None:
					perm(A[:j]+A[j+1:],A[j])
				elif is_perfect(prev+A[j]):
					perm(A[:j]+A[j+1:],A[j])
		self.res=0
		perm(nums,None)
		return self.res
  
---------------------------------------------------------------------------
Since the size of nums array is at max 12 this situation a perfect fit for such problems in which time complexity is usually high

Now the first thing is to make a dictionary which stores nums[i]'s for every nums[i] such that the pair's sum is a perfect square

Now we try to make every permutation with the condition that:
    The prev item and the current item we are adding will add to form a perfect square
	Now keep in mind that once we add any item we mark it as used for further recursion
	when the recurson is done we free the it 
	
	this is called backtracking

How to get free from repeating permutation's ?
Say list is [5,2,5,0,2]
We Took 5 as starting the rest is [2,5,2,0]
Now if we take 2 (index 0 ) with 5 we should not takr 2 ( index 2 ) with 5 as we have processed every permutaion having 2 next to 5 at a specific position


class Solution:
    def isSquare(self,num):
        return int(num**0.5)**2 == num
    def makePermutation(self,used,vis,prev,n):
        if used == n: 
            #we reached the end
            self.ans += 1
            return
        tmp = {}
        for i in range(n):
            if vis[i] == False and self.nums[i] not in tmp:
                tmp[self.nums[i]] = True
                if self.nums[i] in self.d[prev]:
                    vis[i] = True
                    self.makePermutation(used+1,vis,self.nums[i],n)
                    vis[i] = False
        
    def numSquarefulPerms(self, nums: List[int]) -> int:
        d = { x:{} for x in nums}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if self.isSquare(nums[i] + nums[j]):
                    d[nums[i]][nums[j]] = True
                    d[nums[j]][nums[i]] = True
        self.nums = nums
        self.ans = 0
        self.d = d
        vis = [False]*n
        tmp = {}
        for i in range(n):
            if nums[i] in tmp: continue
            tmp[nums[i]] = True
            vis[i] = True
            self.makePermutation(1,vis,self.nums[i],n)
            vis[i] = False
        return self.ans
----------------------------------------------------------------------------
class Solution:

    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        @lru_cache   
        def square(m):
            left, right = 1, m 
            while left < right:
                mid = (left + right) // 2
                if mid**2 >= m:
                    right = mid
                else:
                    left = mid + 1
            return m == right**2
        
        n = len(nums)
        cnt = set()
        stack = []
        visited = set()
        
        for i in range(n):
            stack.append((nums[:i] + nums[i+1:], [nums[i]]))
    
        while stack:
            
            arr, res = stack.pop()
            visited.add((tuple(arr), tuple(res)))
            if len(arr) == 0:
                cnt.add(tuple(res))
            for i in range(len(arr)):
                if square(res[-1] + arr[i]):
                    if (tuple(arr[:i] + arr[i+1:]), tuple(res + [arr[i]])) not in visited:
                        stack.append((arr[:i] + arr[i+1:], res + [arr[i]]))
        return len(cnt)
