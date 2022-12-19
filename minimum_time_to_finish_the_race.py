'''
You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri] indicates that the ith tire can finish its xth successive lap in fi * ri(x-1) seconds.

For example, if fi = 3 and ri = 2, then the tire would finish its 1st lap in 3 seconds, its 2nd lap in 3 * 2 = 6 seconds, its 3rd lap in 3 * 22 = 12 seconds, etc.
You are also given an integer changeTime and an integer numLaps.

The race consists of numLaps laps and you may start the race with any tire. You have an unlimited supply of each tire and after every lap, you may change to any given tire (including the current tire type) if you wait changeTime seconds.

Return the minimum time to finish the race.
'''

Let t[n] denotes the minimum time to run n laps, the DP equation is thus:
t[n] = min {r = 1 ~ min(maxt,n)} t[r] + changeTime + t[n-r]

Now we add some pre-treatment:

The default value of t[n] for any n can be set as changeTime * (n-1) + min(f) * n, i.e., change tire after every lap.
We don't need to consider all tires. If tire1 and tire2 satisfies f1<=f2 and r1<=r2, then tire1 dominates tire2. Therefore, suppose (in a sorted list of tires) the last tire we consider is tire1, we only consider tire2 if f2>f1 and r2<r1.
maxt is the largest possible number of laps to run without changing tires. Therefore, maxt can be quite small compared to numLaps. To get maxt, for every tire we consider in 2, try running it without changing tires until the time for running the next lap is greater than changeTime + f (and thus it's better to change tire). Or simply use maxt = 17 as 2^17 = 131072>10^5.
The current time complexity stands at O(T log T + (T+N) log C), where T = number of tires, N = numLaps and C = changeTime. O(T log T) from sorting the tires, O(T log C) to derive maxt (note that maxt < log2(changeTime)), and finally soving the DP for O(N log C).

Although ignoring pre-treatment 2 and considering all tires would eliminate the O(T log T) part, it will actually make the (hidden) constant larger for the O(T log C) part later, and the runtime comparison is 2600+ ms w/ pre-treatment 2 compared to 8000+ ms w/o, suggesting that in the testcases many tires are dominated.

Meanwhile, pre-treatment 3 is a huge improvement in terms of time complexity from O(N^2) of the usual DP to O(N log C). The runtime comparison is 2600+ ms w/ compared to 7500+ ms w/o.

Here's my code. On second thought the newTires list is not necessary but I am lazy so I will just leave it be.

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        tires.sort()
        newTires = []
        minTime = [changeTime*(i-1) + tires[0][0]*i for i in range(numLaps+1)]
        minTime[0] = 0
        maxi = 0
        for f,r in tires:
            if not newTires or f>newTires[-1][0] and r<newTires[-1][1]:
                newTires.append([f,r])
                t = f
                i = 1
                while i<numLaps and t*(r-1)<changeTime:
                    t = t*r + f
                    i += 1
                    if minTime[i]>t:
                        minTime[i]=t
                        maxi = max(i,maxi)
        for lap in range(numLaps+1):
            for run in range(min(lap,maxi+1)):
                minTime[lap] = min(minTime[lap],minTime[lap-run]+changeTime+minTime[run])
        return minTime[numLaps]
