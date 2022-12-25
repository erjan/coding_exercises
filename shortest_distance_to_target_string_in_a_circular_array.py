'''
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.
'''


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = -1
        i = 0
        l = len(words)
        while i < l:
            next_ = words[(startIndex + i ) % l]
            prev_ = words[(startIndex - i ) % l]
            if next_ == target or prev == target:
                return i
            i += 1
        return ans
        
-----------------------------------------------------------------------------------------------
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        # moving right
        moveright = 0
        flag = False
        for i in range(startIndex,len(words)+startIndex):
            if words[(i+1)%n] == target:
                flag = True
                moveright += 1
                break
            else:
                moveright += 1
        # If target is not present so its no use searching to the left so we return -1
        if flag == False:
            return -1
        
        # moving left
        moveleft = 0
        pointer = startIndex
        while True:
            if words[pointer] == target:
                break
            else:
                pointer = (pointer - 1 + n) % n
                moveleft += 1
        return min(moveleft,moveright)
        
