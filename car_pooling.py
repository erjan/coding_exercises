'''
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



The idea is very simple we will check that if at any station the no of passengers are more than
the capacity
'''


#non working

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        trips = sorted(trips, key = lambda x: x[1])
        
        prev_from = trips[0][1]
        prev_to = trips[0][2]
        capacity = capacity - trips[0][0]
        
        for psng, from_,to_ in trips[1:]:
            
            if from_ > prev_from:
                capacity -= psng
                if capacity < 0:
                    return False
                prev_from = from_
                prev_to = to_
                
            elif from_ > prev_from:
                capacity += psng
                

        return True
-----------------------------------------------------------------------------------------------------------

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x: x[2])
        stations = trips[-1][-1]
        people = [0] * (stations+1)
        
        
        for psng, from_,to_ in trips:
            people[from_] += psng
            people[to_] -= psng
        
        if people[0] > capacity: return False
        
        for i in range(1, stations+1):
            people[i] += people[i-1]
            
            if people[i] > capacity:
                return False
        return True
