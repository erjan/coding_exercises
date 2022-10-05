'''
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = self.function(spells,potions,success)
        return result
    
    def function(self,arr1,arr2,success):
        n2 = len(arr2)
        arr2.sort() #Sorting Enables Us To Do Binary Search
        ans = []
        for i in arr1:
            val = math.ceil(success/i) #Finding the Value Of Portion With Least Strength So That It Can Be Greater Than Success
            idx = bisect.bisect_left(arr2,val) #Finding The Left Most Index So That The Value Can Be Inserted
            res = n2-idx+1  #Calculating the remaining numbers after finding the suitable index
            ans.append(res-1)
        return ans
---------------------------------------------------------------------------------------------------------------------------------------
def successfulPairs(self, spells: List[int], potions: List[int], s: int) -> List[int]:
    q=[]
    potions.sort()                                      #Sort the potion array
    a=len(potions)
    for i in spells:
        count=0
        l=0                                   #We have to find a value which is less than (success/i) in sorted array  
         r=len(potions)                # binary seach will give index of that point and onwards that index all are 
        x=s/i                                #greater values 
        while l<r:
            mid=l+(r-l)//2
            if potions[mid]>=x:
                r=mid
            else:
                l=mid+1
        
        count=(a-l)                                      #Last - index that came with binary search
        q.append(count)
    return q
