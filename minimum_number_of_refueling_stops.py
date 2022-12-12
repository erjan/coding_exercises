'''
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
'''


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:

        last_station = {0: startFuel}
        for station in stations:
            cur_station = {}
            for stop, fuel in last_station.items():
                if fuel >= station[0]:
                    cur_station[stop] = fuel

            if last_station[stop] >= station[0]:
                cur_station[stop + 1] = last_station[stop] + station[1]

            for stop, fuel in last_station.items():
                if fuel >= station[0]:
                    cur_station[stop + 1] = max(
                        fuel + station[1], cur_station[stop + 1]
                    )

            if not cur_station.keys():
                return -1

            last_station = cur_station

        for stop, fuel in last_station.items():
            if fuel >= target:
                return stop
        return -1

      
