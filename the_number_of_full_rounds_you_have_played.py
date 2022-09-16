'''
You are participating in an online chess tournament. There is a chess round that starts every 15 minutes. The first round of the day starts at 00:00, and after every 15 minutes, a new round starts.

For example, the second round starts at 00:15, the fourth round starts at 00:45, and the seventh round starts at 01:30.
You are given two strings loginTime and logoutTime where:

loginTime is the time you will login to the game, and
logoutTime is the time you will logout from the game.
If logoutTime is earlier than loginTime, this means you have played from loginTime to midnight and from midnight to logoutTime.

Return the number of full chess rounds you have played in the tournament.

Note: All the given times follow the 24-hour clock. That means the first round of the day starts at 00:00 and the last round of the day starts at 23:45.

 
 '''

class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        sh, sm = startTime.split(":")
        eh, em = finishTime.split(":")
		
        # sh - hour part of the start time
		# sm - minute part of the start time
		# eh - hour part of the finish time
		# em = minute part of the finish time
        sh, sm, eh, em = int(sh), int(sm), int(eh), int(em)
        
        if sh == eh:
            if sm <= em:
                return em//15 - (sm//15 + 1)
            else:
                val = 0
                sm = 60 - sm
                val += sm//15
                val += em//15
                return 23*4 + val 
        else:
            if eh < sh:
                eh += 24
            val = 0
            sm = 60 - sm
            val += sm//15
            val += em//15
            sh += 1
            return (eh-sh)*4 + val
          
----------------------------------------------------
def numberOfRounds(self, startTime: str, finishTime: str) -> int:
    s = int(startTime[:2]) * 60 + int(startTime[-2:])
    t = int(finishTime[:2]) * 60 + int(finishTime[-2:])
    if s > t:
        t += 24 * 60
    q, r = divmod(s, 15)
    s, t = q + int(r > 0), t // 15
    return max(0, t - s)
