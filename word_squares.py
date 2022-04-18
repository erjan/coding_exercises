'''
Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
'''


The idea is very simple: generate a hashmap for all possible prefixes with the words.

Perform backtracking on each combination so that the combination gets disgarded as quickly as possible.

To determine which prefix to use, simply make use of the current number of words included in the square.

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def search(square):
            n, m = len(square), len(square[0])
            if n == m:    # solution found
                ans.append(square)
                return
            req_prefix = ""    # Generate the required prefix
            for i in range(n):
                req_prefix += square[i][n]
            if req_prefix in prefixes:    # Perform backtracking
                all_prefixes = prefixes[req_prefix]
                for prefix in all_prefixes:
                    search(square + [prefix])
            else:    # Kills the current combination
                return
            
        # Generate all possible prefixes
        prefixes = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefixes[word[:i]].append(word)
        
        ans = []
        for word in words:
            search([word])

        return ans
      
--------------------------------------------------------------------------------
from collections import defaultdict
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def dfs(begin_with, path):
            if begin_with not in prefix: return
            #5 loop through each candidate with the prefix
            for next_candidate in prefix[begin_with]:
                #6 add the next_candidate to path
                path+=[next_candidate]
                #9 if path is equal to N (word length) then it formed square
                if len(path) == N:
                    result.append(list(path))
                    #10 after append to result list, 
                    # pop the last candidate and continue with next candidate
                    # no need to recurse anymore
                    path.pop()
                    continue
                #7 find next prefix need to be found
                # if the path is [ball, area], the next word we need to find is the ones with "le" (index 2)
                # therefore, "".join(word[len(path)]) for each word in path
                next_prefix = "".join([word[len(path)] for word in path])
                #8 recurse into same function
                dfs(next_prefix, path)
                path.pop()
            
        N = len(words[0])
        #1 if word length is 1, it means itself is a square
        # thus, return words
        if N == 1: return words
        
        #2 make prefix dictionary
        prefix = defaultdict(set)
        for word in words:
            for i in range(1, N):
                prefix[word[:i]].add(word)
        
        result = []
        #3 Try each word as possible leading candidate
        for word in words:
            #4 gives second char of the leading word as next prefix to search for
            # note index is 1
            dfs(word[1] ,[word]) 
        return result
      
      
----------------------------------------------------------------------
class Node:
    def __init__(self):
        self.value: str = None
        self.children: Dict[Node] = {}


class Trie:
    def __init__(self, words: List[str]) -> None:
        self.root: Node = Node()
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.value = word

    def predict(self, prefix: str) -> List[str]:
        # find deepest node with this prefix
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return []
            node = node.children[letter]
        # output all possible words from here on
        predictions = []

        def _r(node):
            if not node:
                return
            if node.value is not None:
                predictions.append(node.value)
            for child in node.children.values():
                _r(child)

        _r(node)
        return predictions


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie(words)
        res = []

        def explore(current):
            # are we done? add to results
            if len(current) == len(words[0]):
                res.append(current)
                return
            # find next prefix
            prefix_list = []
            for word in current:
                prefix_list.append(word[len(current)])
            # ask trie for predictions of words with this prefix
            prefix = "".join(prefix_list)
            predictions = trie.predict(prefix)
            for candidate in predictions:
                # no revisiting
                explore(current + [candidate])

        # start the dfs word by word
        for word in words:
            explore([word])
        return res
      
------------------------------------------------------------
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        wordsWithPrefix = defaultdict(list)
        for w in words:
            for i in range(1, n):
                wordsWithPrefix[w[:i]].append(w)
        ans = []
        def dfs(square):
            nonlocal n
            if (i := len(square)) == n:
                ans.append(square)
                return
            for w in wordsWithPrefix[''.join(list(zip(*square))[i][:i+1])]:
                dfs(square + [w])
        for w in words:        
            dfs([w])        
        return ans
