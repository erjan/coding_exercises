'''
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to 
pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
'''
#exact same as https://leetcode.com/problems/longest-substring-without-repeating-characters/

def minimumCardPickup(self, cards: List[int]) -> int:
    seen = {}
    s = cards
    smallest_card_len = sys.maxsize
    start, end = 0, 0

    if len(s) == 0:
        return 0

    while end < len(s):
        c = s[end]

        if c in seen:
            # invalid window
            # update start
            start = seen[c] + 1
            smallest_card_len = min(smallest_card_len, end - start + 1)

        seen[c] = end

        end += 1

    if smallest_card_len == sys.maxsize:
        return -1

    return smallest_card_len + 1
  
-----------------------------------------------------------------------------
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lastOccurence, ans = defaultdict(list), float('inf')
        for i in range(len(cards)):
            lastOccurence[cards[i]].append(i)
        if len(lastOccurence.keys()) == len(cards):
            return -1
        for card in lastOccurence:
            diff = float('inf')
            if len(lastOccurence[card]) > 1:
                for i in range(len(lastOccurence[card])):
                    diff = min(diff, abs(lastOccurence[card][i - 1] - lastOccurence[card][i]) + 1)
            ans = min(ans, diff)
        return ans
