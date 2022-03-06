'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
'''

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)+1
        n = [i for i in range(0, n)]
        mini = min(n)
        maxi = max(n)
        total = list()

        for i in range(len(s)):
            if s[i] == "I":

                total.append(mini)
                mini += 1

            elif s[i] == "D":
                total.append(maxi)
                maxi -= 1       
                
        total.append(maxi)
        print(total)
        return total
