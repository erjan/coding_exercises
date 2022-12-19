'''
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.
'''

class Solution:
    def largestVariance(self, s: str) -> int:
        # This is similar to the Kadane's algorithm, see problem 53 before attempting this one
        # Here we take every permutation of 2 characters in a string and then apply Kadane algo to it
        # Say string is 'abcdab'
        # From the perspective of characters a, b the string is +1, -1, +0, +0, +1, -1
        # and we want to maximize this sum
        # note that we also want to make sure both a and b are in there, otherwise the numbers
        # will be incorrect.
        # Also, our operation of finding the sum is not commutative, so we need permutations and
        # not combinations.
        cntr = Counter(s)
        res = 0
        for a, b in itertools.permutations(cntr, 2):
            a_cnt, b_cnt = cntr[a], cntr[b]
            var = 0; seen_a = seen_b = False
            
            for c in s:
                # this won't impact the variance -- so ignore
                if c not in (a, b): continue
                if var < 0:
                    # we have more b's than a's
                    # if no more a's left, var would ultimately be -ve -- so break
                    if not a_cnt: break
                    # just add the remaining a's to var
                    if not b_cnt:
                        res = max(res, var + a_cnt)
                        break
                    # we have a's and b's remaining, so restart
                    seen_a = seen_b = False
                    var = 0
                if c == a:
                    var += 1
                    a_cnt -= 1
                    seen_a = True
                if c == b:
                    var -= 1
                    b_cnt -= 1
                    seen_b = True
                if seen_a and seen_b:
                    res = max(res, var)
        return res
                
