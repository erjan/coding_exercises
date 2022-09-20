'''
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.
'''


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friendsCount = len(times)
        targetFriendTime = times[targetFriend]
        times.sort(key=lambda x: x[0])
        chairs = list(range(friendsCount))
        heapq.heapify(chairs)
        # occupiedChairs will have values like this: [time till it is occupied, chair number]
        occupiedChairs = []
        heapq.heapify(occupiedChairs)
        for arrival, leaving in times:
			# Vacate all the occupied chairs which are free by now.
            while occupiedChairs and occupiedChairs[0][0] <= arrival:
                _, chairAvailable = heapq.heappop(occupiedChairs)
                heapq.heappush(chairs, chairAvailable)
            smallestChairNumberAvailable = heapq.heappop(chairs)
            if arrival == targetFriendTime[0] and leaving == targetFriendTime[1]:
                return smallestChairNumberAvailable
            else:
                heapq.heappush(occupiedChairs, (leaving, smallestChairNumberAvailable))
