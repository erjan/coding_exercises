'''
You are given an integer array score of size n, where score[i] is the score of the ith athlete 
in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place 
athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
 '''

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)

        d = dict()
        c = 1
        s = sorted_score
        for i in range(len(s)):
            if i == 0:
                d[s[i]] = 'Gold Medal'
            elif i == 1:
                d[s[i]] = 'Silver Medal'
            elif i == 2:
                d[s[i]] = 'Bronze Medal'
            else:
                d[s[i]] = str(c)
            c += 1

        answer = list()

        for i in range(len(score)):
            answer.append(d[score[i]])
        return answer
