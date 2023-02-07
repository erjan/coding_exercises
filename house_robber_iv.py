'''
There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.
'''


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(cap):
            count=taken=0
            for x in nums:
                if taken:
                    taken=False
                elif x<=cap:
                    count+=1
                    taken=True
            return count>=k
        l,r=min(nums),max(nums)
        while l<=r:
            mid=l+(r-l)//2
            if check(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        
        
---------------------------------------------------------------------------------------
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(x):
            flag=False
            count=0

            for val in nums:
                if flag==True:
                    flag=False
                    continue
                else:
                    if val<=x:
                        count+=1
                        flag=True
            
            return count>=k

        
        low,high=min(nums),max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if check(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
