'''
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

 
 '''
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:


        res = []
        
        nums2_id = []

        for i in range(len(nums2)):
            id2,val2 = nums2[i]
            nums2_id.append(id2)

        d = dict()

        for i in range(len(nums1)):
            id1, val1 = nums1[i]
            if id1 not in d:
                d[id1] = val1
            else:
                d[id1] = val1
        
        for i in range(len(nums2)):
            id2, val2 = nums2[i]

            if id2 in d:
                d[id2]+=val2
            else:
                d[id2] = val2
        
        d = list(d.items())

        d.sort(key = lambda x: x[0])
        return d

---------------------------------------------------------------------------------------------------------------------
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                res.append(nums2[j])
                j += 1
            elif j == len(nums2):
                res.append(nums1[i])
                i += 1
            else:
                if nums1[i][0] == nums2[j][0]:
                    res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                    i += 1
                    j += 1
                elif nums1[i][0] < nums2[j][0]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
        return res

