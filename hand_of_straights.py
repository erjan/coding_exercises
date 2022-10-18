'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
'''





'''
Explanation:

Since ordering does not matter, we convert hand to a counter count.
We always form new straights from the minimum value available in count, as that guarantees an increasing 'Hand of Straight'.
We simulate the using up of cards by reducing their frequencies in count. The goal is to reduce every frequency to 0.
We return True if we can reduce all the frequenies in count to 0 (i.e count[x] = 0 for all x in count).
We return False if there is a frequency count[x] = -1, as it indicates that we do not have the cards necessary to form the current 'Hand of Straight'

Time O(nlogn), Space O(n), where n is the number of elements in hand.
'''



class Solution:
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        for y in sorted(count):
            while count[y] > 0:
                for k in range(y, y + W):
                    count[k] -= 1
                    if count[k] < 0:
                        return False
        return True
      
-----------------------------------------------------------------------------------------      
