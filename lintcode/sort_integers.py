#Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

#i used bubble sort


class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
        # write your code here

        for i in range(len(a)):

            for j in range(len(a)-1):

                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a
