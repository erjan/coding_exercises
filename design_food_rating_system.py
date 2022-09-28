'''
Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
'''


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.foods = foods; self.cuisines = cuisines; self.ratings = ratings
        self.index = dict(zip(foods, range(n)))
        self.cuisinesMap = defaultdict(list)
        for i, cuisine in enumerate(cuisines):
            heappush(self.cuisinesMap[cuisine], (-self.ratings[i], self.foods[i]))
            
    def changeRating(self, food: str, newRating: int) -> None:
        i = self.index[food]
        self.ratings[i] = newRating; cuisine = self.cuisines[i]
        heappush(self.cuisinesMap[cuisine], (-self.ratings[i], self.foods[i]))

    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisinesMap[cuisine][0]
        while rating != -self.ratings[self.index[food]]:  # check highest rating is current
            heappop(self.cuisinesMap[cuisine])
            rating, food = self.cuisinesMap[cuisine][0]
        return food
