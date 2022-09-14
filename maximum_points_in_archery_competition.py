'''
Alice and Bob are opponents in an archery competition. The competition has set the following rules:

Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
The points are then calculated as follows:
The target has integer scoring sections ranging from 0 to 11 inclusive.
For each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
However, if ak == bk == 0, then nobody takes k points.
For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.

You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.

Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.

If there are multiple ways for Bob to earn the maximum total points, return any one of them.
'''


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ans = 0
        res = [0]*12
        for mask in range(2**12):
            bobTaken = 0
            temp = [0]*12
            bobPoints = 0
            for j in range(12):
                if ((1<<j)&mask)>0:
                    bobTaken+=aliceArrows[j]+1
                    bobPoints+=j
                    temp[j]=aliceArrows[j]+1
            if bobTaken>numArrows:
                continue
            if bobPoints>ans:
                ans = bobPoints
                temp[0]+=numArrows-bobTaken
                res = temp[:]
        return res
      
--------------------------------------------------------------------------------------------------------
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bobArrows = []
        for i in range(12):
            bobArrows.append(aliceArrows[i] + 1)
        maxScore, maxBinNum = 0, None
        for binNum in range(2 ** 12):
            tempScore, tempArrows = 0, 0
            tempBinNum = binNum
            k = 0
            while tempBinNum > 0:
                if tempBinNum % 2 == 1:
                    tempScore += k
                    tempArrows += bobArrows[k]
                tempBinNum //= 2
                k += 1
            if tempArrows <= numArrows and tempScore > maxScore:
                maxScore = tempScore
                maxBinNum = binNum
        output = [0] * 12
        k = 0
        while maxBinNum > 0:
            if maxBinNum % 2 == 1:
                output[k] = bobArrows[k]
            maxBinNum //= 2
            k += 1
        if sum(output) < numArrows:
            output[0] += numArrows - sum(output)
        return output
