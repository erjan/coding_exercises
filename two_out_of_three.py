'''
Given three integer arrays nums1, nums2, and nums3, return a 
distinct array containing all the values that are present in at 
least two out of the three arrays. You may return the values in any order.
'''

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:           
        n1 = nums1
        n2 = nums2
        n3 = nums3
        
        main = set()
        for i in range(len(n1)):
            if n1[i] in n2:
                main.add(n1[i])

        for i in range(len(n2)):
            if n2[i] in n3:
                main.add(n2[i])

        for i in range(len(n3)):
            if n3[i] in n1:
                main.add(n3[i])
                
        main = list(main)
        print(main)
        return main
