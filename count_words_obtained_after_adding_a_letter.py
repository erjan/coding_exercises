'''
You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.
'''


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        starts, ans = set(), 0
        ans = 0
        for word in startWords:
            starts.add(''.join(sorted(word)))
        for word in targetWords:
            for i in range(len(word)):
                if ''.join(sorted(word[:i] + word[i+1:])) in starts:
                    ans += 1
                    break
        return ans
      
----------------------------------------------------------------------------------------
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # Sort each start word and add it to a hash set
        startWords_sorted = set()
        # O(S*26*log(26))
        for word in startWords:
            startWords_sorted.add("".join(sorted(list(word))))
        
        # sort each target word and add it to a list
        # O(T*26*log(26))
        targetWords_sorted = []
        for word in targetWords:
            targetWords_sorted.append(sorted(list(word)))
        
        # for each sorted target word, we remove a single character and 
        # check if the resulting word is in the startWords_sorted
        # if it is, we increment cnt and break the inner loop
        # otherwise we keep removing until we either find a hit or reach the
        # end of the string
        # O(T*26) = O(T)
        cnt = 0
        for target in targetWords_sorted:
            for i in range(len(target)):
                w = target[:i] + target[i+1:]
                w = "".join(w)
                if w in startWords_sorted:
                    cnt += 1
                    break
        
        return cnt
