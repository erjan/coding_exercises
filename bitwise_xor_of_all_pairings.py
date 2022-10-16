'''
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists 
another array, nums3, which contains the bitwise XOR of all pairings of 
integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.
'''


    def xorAllNums(self, A, B):
        x = y = 0
        for a in A:
            x ^= a
        for b in B:
            y ^= b
        return (len(A) % 2 * y) ^ (len(B) % 2 * x)
----------------------------------------------------------------------

class Solution:     # Example:  nums1 = [2,1,3] ; nums2 = [10,4,5,0]
                    # 
                    #    From Boolean algebra we know that n^0 = n and n^n = 0, from which we can infer that
                    #    the xor of an even count of an integer n is 0, and the xor of an odd count of an
                    #    integer n is n. We also know that the ^ operator is commutative and associative. 
                    #    So, from the Example:        

                    #       =>  nums3 = [2^10,2^2,2^5,2^0,1^10,1^2,1^5,3^0,3^10,3^2,3^5,3^0]

                    #       => answer = (2^10)^(2^4)^(2^5)^(2^0)^(1^10)^(1^4)^(1^5)^(3^0)^(3^10)^(3^4)^(3^5)^(3^0)
                    #                 = (2^2^2^2)^(1^1^1^1)^(3^3^3^3) ^ (10^10^10)^(4^4^4)^(5^5^5)^^(0^0^0)
                    #                 = 0^0^0  ^  10^4^5^0   =   0^11   =   11
                    #
                    #    The inferences we draw from this example lead to the code below.
                    #           
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        n1 = 0 if not len(nums2)%2 else reduce(xor,nums1)
        n2 = 0 if not len(nums1)%2 else reduce(xor,nums2)
        return n1^n2
