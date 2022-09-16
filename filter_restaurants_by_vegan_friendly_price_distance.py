'''
Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.

The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.

Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.
'''

class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        arr = []
        for i,r,vf,p,d in restaurants: # [idi, ratingi, veganFriendlyi, pricei, distancei]
			if veganFriendly and not vf:
                continue
            if p<=maxPrice and d<=maxDistance:
                arr.append([-r,-i])
        arr.sort()
        return [-i for r,i in arr]
---------------------------------------------------------------------------------------------------
import heapq
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        heap = []
        for r in restaurants:
            rest = Node(r)
            if rest.matchFilters(veganFriendly, maxPrice, maxDistance):
                heappush(heap, rest)
        rs = []
        while heap:
            curr = heappop(heap)
            rs.append(curr.id)
        return reversed(rs)
            
                
        
class Node:
    def __init__(self, values):
        self.id = values[0]
        self.rating = values[1]
        self.vegan = values[2]
        self.price = values[3]
        self.distance = values[4]
    
    def matchFilters(self, vegan, price, dist):
        if ((self.vegan == 1 and vegan == 1) or vegan == 0) and self.price <= price and self.distance <= dist:
            return True

        return False
        
    def __gt__(self, other):
        if self.rating > other.rating:
            return True
        elif self.rating == other.rating:
            return self.id > other.id
        else:
            return False
--------------------------------------------------

def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    
    # if veganFriendly matters - it will be 1 and take only with 1 otherwise take all.
       
    filtered_restaurants = list(filter(lambda x: x[3] <= maxPrice and x[4] <= maxDistance and (x[2] == 1 or x[2]==veganFriendly) , restaurants))
    
    
    # reverse= True means highest to lowest (descending order)
    # key means sort by x[1] ie rating if x[1] values are equal then see x[0] ID
    filtered_restaurants.sort(key=lambda x: (x[1],x[0]), reverse = True)
    
    return [x[0] for x in filtered_restaurants] # return IDs
