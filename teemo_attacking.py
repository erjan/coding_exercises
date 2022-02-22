'''
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.
'''

# ill working solution

class Solution:
    def f(self, t, d):
        total = 0

        if d == 0:
            return 0

        intervals = list()
        last = None
        for i in range(len(t)):
            if last is not None and last >= t[i]:
                temp = [last,  t[i] + d]
                last = t[i] + d
                intervals[-1][1] = last

            else:
                temp = [t[i], t[i] + d - 1]
                last = t[i] + d - 1
                intervals.append(temp)

        print(intervals)

        for i in range(len(intervals)):
            cur = intervals[i]
            diff = cur[1] - cur[0]
            if diff <= 1:
                diff = 2

            total += diff

        print('total is %d' % total)
        return total


if __name__ == '__main__':

    x = Solution()

    t = [1, 4]
    d = 2

    t = [1, 7, 13]
    d = 14

    t = [1, 2, 6, 10]
    d = 4

    t = [1]
    d = 4

    t = [1, 2, 3, 4]
    d = 1
    x.f(t, d)

    
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        res = duration
        
        for i in range(len(timeSeries)-1):
            res += min(duration, timeSeries[i+1] - timeSeries[i])
        return res    
    
