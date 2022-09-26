'''
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.
'''

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0
        prefix_sum = [0]*n
        d = {}
        for i in range(n):
            prefix_sum[i] = 1 if hours[i] > 8 else -1
            prefix_sum[i] += prefix_sum[i-1]
            if prefix_sum[i] > 0 : 
                ans = i + 1
            else:
                if prefix_sum[i] - 1 in d:
                    j = d[prefix_sum[i] - 1]
                    if i - j > ans: ans = i - j
            if prefix_sum[i] not in d: d[prefix_sum[i]] = i
        return ans
      
-------------------------------------------------------------------------------------------      

class Solution:
    def longestWPI(self,hours):

        max_wpi, ntv, first_preimage = 0, 0, {}

        for day_idx, hrs_today in enumerate(hours):

            # check if today was a tiring day or not
            ntv += 1 if hrs_today > 8 else -1

            # if our net is positive (the net here is starting from first 
            # day), we just set the longest wpi to days that has passed
            if ntv > 0: max_wpi = day_idx + 1

            # if we haven't seen this ntv before, we store it
            if not ntv in first_preimage: first_preimage[ntv] = day_idx

            # if the ntv that is 1 less is seen before (for a net 1 ntv)
            # we compute the wpi from that and see if that's longer than
            # the longest we've seen so far
            if ntv - 1 in first_preimage:
                max_wpi = max(max_wpi, day_idx - first_preimage[ntv - 1])

        return max_wpi
