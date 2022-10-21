'''
You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.

Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.
'''

Create a Timeline list, the index is each second of starting time, value is the largest end time can be reached at this second. Search the maximum of each starting-ending interval till the end or stay fixed.

        //input: [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T=10
		
        maxlen = max([i[1] for i in clips])
        timeline = [0]*(maxlen+1)
        for clipstart, clipend in clips:
            timeline[clipstart] = max(timeline[clipstart], clipend)
			
        //Timeline looks like: [2, 9, 0, 0, 6, 9, 0, 0, 10, 0, 0]
        
        if timeline[0] == 0: return -1
        start = 0; end = timeline[0]; times = 1
        
        while end < T:
            maxpos, maxval = max(enumerate(timeline[start:end+1]), key=lambda x: x[1])
            if maxval > end:
                end = maxval
                start = maxpos
                times += 1
            else:
                return -1
        return times
      
----------------------------------------------------------------------------------------------------
Define dp(i) as the minimum number of clips needed to cover [0, i] sporting event.
We'll get the recursion below:
dp(i) = min(dp(j) + 1, dp(i)) if the clip covers [j, i] exists

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [float('inf')] * (T + 1)
        dp[0] = 0
        for i in range(1, T + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] + 1, dp[i])
        if dp[T] == float('inf'):
            return -1
        return dp[T]
      
-------------------------------------------------------------------------------------------------------------------
The intuitve heuristic is that we iterate clips with order by their starting time and keep increasing furthest ending time we can reach.

If the starting time of current clips is later than current furthest ending time, then stitching is not doable since none of the rest clips' starting time is earlier. Once furthest ending time >= T, we have finished video stitching.

And to get the minimal number of clips we need, we need to remove all unncessary clips during the scan.
Suppose we already have clips [s0, e0] and next two clips are [s1, e1] and [s2, e2]. If s2 <= e0, then s0 <= s1 <= s2 <= e0 and only one of two clips are needed. Thus, we use prev_end to store e0 and each time s <= prev_end, we don't add up cnt. Othwise, we have to add one more clip and update prev_end accordingly. The furthest ending time just gets updated each time as max(furthest_end, e).

def videoStitching(clips, T):
	prev_end, end, cnt = -1, 0, 0
	for i, j in sorted(clips):
		if i > end or end >= T: break
		if prev_end < i <= end: prev_end, cnt = end, cnt + 1
		end = max(end, j)
	return cnt if end >= T else -1
