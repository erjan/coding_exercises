'''
You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.
'''


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        left, right = 0, k + sum(stations)
        while left <= right:
            x = (left + right) // 2
            use = 0
            # v is the stations after adding
            v = stations.copy()
            # s means the power of city i
            # at first, it record the sum of v[0,r)
            s = sum(stations[0: r])
            for i in range(n):
                # add to t if needed
                t = n - 1 if n - 1 < i + r else i + r
                # update s
                # find a city should be added
                if i + r < n: s += v[i+r]
                # find a city should be removed
                if i - r > 0: s -= v[i-r-1]
                # mising power stations
                diff = x - s if x - s > 0 else 0 
                v[t] += diff
                s += diff
                use += diff
            
            if use <= k:
                left = x + 1
            else:
                right = x - 1
        return right
      
-------------------------------------------------------------------------------------------------------
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def isGood(minPowerRequired, additionalStations):
            windowPower = sum(stations[:r])  # init windowPower to store power of 0th city (minus stations[r])
            additions = [0] * n
            for i in range(n):
                if i + r < n:  # now, windowPower stores sum of power stations from [i-r..i+r], it also means it's the power of city `ith`
                    windowPower += stations[i + r]

                if windowPower < minPowerRequired:
                    needed = minPowerRequired - windowPower
                    if needed > additionalStations:  # Not enough additional stations to plant
                        return False
                    # Plant the additional stations on the farthest city in the range to cover as many cities as possible
                    additions[min(n - 1, i + r)] += needed
                    windowPower = minPowerRequired
                    additionalStations -= needed

                if i - r >= 0:  # out of window range
                    windowPower -= stations[i - r] + additions[i - r]

            return True

        left = 0
        right = sum(stations) + k  # The answer = `right`, when `r = n`, all value of stations are the same!
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if isGood(mid, k):
                ans = mid  # This is the maximum possible minimum power so far
                left = mid + 1  # Search for a larger value in the right side
            else:
                right = mid - 1  # Decrease minPowerRequired to need fewer additional power stations
        return ans
