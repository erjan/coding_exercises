'''
A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

You are given a string keysPressed of length n, where keysPressed[i] was 
the ith key pressed in the testing sequence, and a sorted list releaseTimes, where 
releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed. The 0th key was 
pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was released.

The tester wants to know the key of the keypress that had the longest duration. The ith 
keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].
'''

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        times = releaseTimes
        r = keysPressed
        res = [None] * len(times)
    
        res[0] = (times[0], r[0])

        for i in range(1,len(times)):
            res[i] = ( times[i] - times[i-1] , r[i])

        maxi = max(item[0] for item in res)
        #print(maxi)

        temp = list()
        for item in res:
            if item[0] == maxi:
                temp.append(item[1])
        temp.sort()
        print( temp[-1])
        return temp[-1]
        
