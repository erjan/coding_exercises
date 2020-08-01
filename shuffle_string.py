'''
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
'''

#my own solution
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = list( s[0] * len(indices))

        counter = 0
        for i in indices:
            temp[i] = s[counter]
            counter+=1
        print(temp)
        temp = ''.join(temp)
        return temp
