'''
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.
'''


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [[0, 0] for i in range(n)]
        ans = []
        
        for i, j, k in bookings:
            arr[i-1][0] += k
            arr[j-1][1] += k
        
        curr = 0
        
        for i in range(len(arr)):
            ans.append(curr + arr[i][0])
            curr += arr[i][0] - arr[i][1]
    
        return ans
    
---------------------------------------------------------------------------------------
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for booking in bookings:
            ans[booking[0]-1]+=booking[2]
            ans[booking[1]]-=booking[2]
        for i in range(1,n):
            ans[i]+=ans[i-1]
            
        return ans[:n]
