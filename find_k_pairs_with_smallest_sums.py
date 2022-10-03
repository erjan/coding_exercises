'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
'''


def kSmallestPairs_alt(nums1, nums2, k):  # O(logn * logm) and O(mn), where m and n are lengths of lists 
    h, res = [], []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            heapq.heappush(h, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
    for _ in range(min(k, len(h))):  # handling an edge case when we have fewer than k elements inside the heap
        _, pair = heapq.heappop(h)
        res.append(pair)
    return res
  
------------------------------------------------------------------------------------------------------------------------

'''
I learned this from other brilliant post and just wanted to expand upon it.

Step 1: We are building a heap using tuples. That tuple will contain (sum of both list indices, indices of list1, and first index of list2) Our heap ordering will be base off the sum. We will need the next two elements in the tuple later.
Step 2: After building our heap, We can now do a tuple unpacking using heappop(). This will pop the lowest value. (Which is the sum in the tuple) We won't be needing the sum value any more so it is just assigned to a underscore _.
Step 3: Since we know that heappop() unpacked the lowest pair values for us. we can append those pair values to our result array.
Step 4: We now should update our heap with the sums of list2 values.
Step 5: Since we upacked the index of list2 toj. We can use this to update the heap by doing the same process Step1 but instead incrementing j by +1. The heap will automatically sort that tuple in the correct order and our while loop will append the lowest value pair to our result array.
I'd Like to Thank cenkay My code is base upon. I think lot of people post answers on the discussion doesn't seem to credit who or where they learned it from. I just like to give credit where credit is due. Hope this helps
'''

class Solution:
    def kSmallestPairs(self, n1: List[int], n2: List[int], k: int) -> List[List[int]]:
        if not n1 or not n2: return []
        
        heap = []
        for i in range(len(n1)):                                  
            heapq.heappush(heap, (n1[i] + n2[0], i, 0))           #Step 1
            
        result = []
        while heap and k > 0:                                     
            _, i, j = heapq.heappop(heap)                         #Step 2
            result.append([n1[i],n2[j]])                          #Step 3
            
            if j+1 < len(n2):                                     #Step 4
                heapq.heappush(heap, (n1[i]+n2[j+1],i, j+1))      #Step 5
            k-=1
        return result
