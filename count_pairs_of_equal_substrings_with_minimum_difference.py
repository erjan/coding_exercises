'''

You are given two strings firstString and secondString that are 0-indexed and consist only of lowercase English letters. Count the number of index quadruples (i,j,a,b) that satisfy the following conditions:

0 <= i <= j < firstString.length
0 <= a <= b < secondString.length
The substring of firstString that starts at the ith character and ends at the jth character (inclusive) is equal to the substring of secondString that starts at the ath character and ends at the bth character (inclusive).
j - a is the minimum possible value among all quadruples that satisfy the previous conditions.
Return the number of such quadruples.
'''

class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        s2idx2 = {s:i for i,s in enumerate(secondString)}
        min_value = float('inf')
        count = 0
        for i in range(len(firstString)):
            if firstString[i] in s2idx2:
                if i - s2idx2[firstString[i]] < min_value:
                    min_value = i - s2idx2[firstString[i]]
                    count = 1
                elif i - s2idx2[firstString[i]] == min_value:
                    count += 1
        return count 
