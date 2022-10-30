'''
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
'''

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        self.shelf_width = shelf_width
        # caches the minimal height with key of the book index and left width 
        cache = {}
        def dfs(i, width, cur_height):
            if i >= len(books):
                return cur_height
            key = str(i) + "_" + str(width)
            if key in cache:
                return cache[key]
            # put current book on the next level of shelf
            cache[key] = cur_height+dfs(i+1, self.shelf_width-books[i][0], books[i][1])
            # if the book could be put on this level of shelf, try to put it
            if books[i][0] <= width:
                cache[key] = min(cache[key], dfs(i+1, width-books[i][0], max(cur_height, books[i][1])))
            return cache[key]
        return dfs(0, shelf_width, 0)
      
---------------------------------------------------------------------------------------------------------------
class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:        

        @cache
        def dp(idx: int, curr_height: int, curr_width: int):
            if curr_width < 0:
                return float("inf")

            if idx == len(books):
                return curr_height

            thickness, height = books[idx]
            same_shelf = dp(idx + 1, max(curr_height, height), curr_width - thickness)
            change_shelf = curr_height + dp(idx + 1, height, shelfWidth - thickness)
            return min(same_shelf, change_shelf)

        return dp(0, 0, shelfWidth)
