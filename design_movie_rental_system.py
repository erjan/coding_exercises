'''
You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.

The system should support the following functions:

Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
Rent: Rents an unrented copy of a given movie from a given shop.
Drop: Drops off a previously rented copy of a given movie at a given shop.
Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
Implement the MovieRentingSystem class:

MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
void rent(int shop, int movie) Rents the given movie from the given shop.
void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.
'''

import heapq
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = {}
        self.rented = set()
        for (shop, movie, price) in entries:
			# we store [price, shop, movie] as a list rather than a tuple because it enables mutable assignment in rent() and drop()
            self.movies.setdefault(movie, {}).setdefault(shop, [price, shop, movie])

    def search(self, movie: int) -> List[int]:
        return [shop for price,shop,_ in heapq.nsmallest(5, self.movies.get(movie, {}).values()) if price < 10001]

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))
        self.movies[movie][shop][0] += 10001
        
    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))
        self.movies[movie][shop][0] -= 10001

    def report(self) -> List[List[int]]:
        return heapq.nsmallest(5, self.rented, key=lambda sm: self.movies[sm[1]][sm[0]])
      
-------------------------------------------------------------------------------------------------------

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.avail = {}
        self.price = {}
        self.movies = defaultdict(list)
        for s, m, p in entries: 
            heappush(self.movies[m], (p, s))
            self.avail[s, m] = True # unrented 
            self.price[s, m] = p
        self.rented = []
        

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies: return []
        ans, temp = [], []
        while len(ans) < 5 and self.movies[movie]: 
            p, s = heappop(self.movies[movie])
            temp.append((p, s))
            if self.avail[s, movie]: ans.append((p, s))
        for p, s in temp: heappush(self.movies[movie], (p, s))
        return [x for _, x in ans]
            

    def rent(self, shop: int, movie: int) -> None:
        self.avail[shop, movie] = False
        p = self.price[shop, movie]
        heappush(self.rented, (p, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        self.avail[shop, movie] = True 
        

    def report(self) -> List[List[int]]:
        ans = []
        while len(ans) < 5 and self.rented: 
            p, s, m = heappop(self.rented)
            if not self.avail[s, m] and (not ans or ans[-1] != (p, s, m)): 
                ans.append((p, s, m))
        for p, s, m in ans: heappush(self.rented, (p, s, m))
        return [[s, m] for _, s, m in ans]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
