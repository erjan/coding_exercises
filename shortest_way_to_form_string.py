'''
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
'''

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        i, minimum = 0, 1
        
        for c in target:
            
			# Get leftmost char after previously matched index
            i = source.find(c, i)

			# If not found
            if i == -1:
                
				# Get leftmost char from begining of string and increase number of concatenated string
                i = source.find(c)
                minimum += 1
                
				# if not found, then target can't be formed. Return -1
                if i == -1:
                    return i
                
            i += 1
                
            
                
        return minimum
--------------------------------------------------------------------

from collections import defaultdict
import bisect

class Solution(object):

    # Greedy solution using two pointer. time O(M*N)
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        targetIdx, subsequencesCount = 0, 0
        while targetIdx < len(target):
            sourceIdx = 0
            subsequencesExists = False
            while sourceIdx < len(source) and targetIdx < len(target):
                if source[sourceIdx] == target[targetIdx]:
                    sourceIdx += 1
                    targetIdx += 1
                    subsequencesExists = True
                else:
                    sourceIdx += 1
            subsequencesCount += 1
            if not subsequencesExists:
                return -1
        return subsequencesCount




    # DP approach using two pointer. time O(M*N)
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        cache = [float('inf')] * (len(target) + 1)
        cache[0] = 0
        for cacheIdx in range(1, len(target) + 1):
            sourceIdx, targetIdx = len(source) - 1, cacheIdx - 1
            while sourceIdx >= 0 and targetIdx >= 0:
                if source[sourceIdx] == target[targetIdx]:
                    if cache[targetIdx] != float('inf'):
                        cache[cacheIdx] = min(cache[cacheIdx], cache[targetIdx] + 1)
                    targetIdx -= 1
                sourceIdx -= 1
        return -1 if cache[-1] == float('inf') else cache[-1]



    # Binary Search approach. time O(M*logN)  -  https://tinyurl.com/twomotm
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        sourceCharIndices = defaultdict(list)
        for idx, char in enumerate(source):
            sourceCharIndices[char].append(idx)
        sourceIdx, subsequencesCount = 0, 0
        for char in target:
            if char not in sourceCharIndices:
                return -1
            j = bisect.bisect_left(sourceCharIndices[char], sourceIdx)          # index in char_indices[c] that is >= sourceIdx
            if j ==len(sourceCharIndices[char]):                                # wrap around to beginning of source
                subsequencesCount += 1
                j = 0
            sourceIdx = sourceCharIndices[char][j] + 1                          # next index in source
        return subsequencesCount if sourceIdx == 0 else subsequencesCount + 1   # add 1 for partial source

-----------------------------------------------------------------------------------

This one is really simple. We have two pointers, one to track our source(j) and one to track our target(i). We compare our chars at our respective pointers, and if they match we increment both source(j) and target(i), if they don't match then we just increment source(j) pointer. If source(j) pointer goes above the length of source that means we have to increase our result by 1 because we have to match with a new source.

We handle the -1 exception right at the start, although it can be handled in the while loop itself by always querying if not target[i] in source.

    def shortestWay(self, source: str, target: str) -> int:
        for t in target:
            if not t in source:
                return -1
        
        result = 1
        i, j = 0, 0
        
        while i < len(target):
            if j >= len(source):
                j = 0
                result += 1
            if target[i] == source[j]:
                i += 1
            j += 1
            
        return result
--------------------------------------------------------

A concise runtime analysis would be: O(M + N * logD) where M is characters count in , D is the max number of character duplications in (since we are traversing a list to find min index over thershold), and N is character count in

from collections import defaultdict
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not target:
            return 0
        
        # build a map between a char and its indices <in source>
        charmap = defaultdict(list)
        for idx, char in enumerate(source):
            charmap[char].append(idx)
        
        substrings_used = 1   # substring used
        src_idx = -1    # last index used from source string
        for char in target:
            if char not in charmap:
                return -1
            
            # get the index of the next occurence of char in <source>. 
            # if there's none, jump back to first occurence and increase substrings_used by 1
            char_indices = charmap[char]
            next_list_idx = bisect.bisect_left(char_indices, src_idx+1)
            next_char_idx = char_indices[next_list_idx] if next_list_idx < len(char_indices) else char_indices[0]
            
            if next_char_idx <= src_idx:
                substrings_used += 1
            
            src_idx = next_char_idx
                
        return substrings_used
--------------------------------------------------------------------------------------

import collections
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:


        def indexer():
            map = collections.defaultdict(list)
            for i, char in enumerate(source):
                map[char].append(i)

            return map

        indexMap = indexer()

        splitNum = 1

        delimiter = -2
        for i in range(len(target)):
            char = target[i]
            if char not in indexMap:
                return -1

            candidate = bisect.bisect_left(indexMap[char], delimiter + 1)

            if len(indexMap[char]) == candidate:
                candidate -= 1

            if indexMap[char][candidate] > delimiter:
                delimiter = indexMap[char][candidate]
            else:
                splitNum += 1
                delimiter = indexMap[char][0]


        return splitNum
----------------------------------------------------------------------------

class Solution(object):
    def shortestWay(self, source, target):
        count, i = 0, 0
        while i < len(target):
            j = source.find(target[i])
            if j == -1:
                return -1
            count += 1
            while j != -1 and i < len(target) - 1:
                i += 1
                k = source[j + 1:].find(target[i])
                j = -1 if k == -1 else j + k + 1
            if j != -1:
                i += 1
        return count
      
      
      
      
      
      
