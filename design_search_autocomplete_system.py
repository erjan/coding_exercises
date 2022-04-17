'''
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.
'''


Store sentences that have already been seen in a map (key = sentence, value = count).
When the first char of a new sentence is input, create a list of all previously seen sentences that match the first char, sorted by decreasing count.
Then for each subsequent char, all we need to do is filter the existing list, keeping only sentences that match the char in its correct position.
At the end of the input, simply increment the count.

We don't need to sort repeatedly for every input, we don't need to store multiple copies of each sentence.

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.partial = []           # previously seen chars of current sentence
        self.matches = []           # matching sentences in decreasing frequency order
        
        self.counts  = defaultdict(int)     # map from sentence to its frequency
        for sentence, count in zip(sentences, times):
            self.counts[sentence] = count

    def input(self, c):
        if c == "#":
            sentence = "".join(self.partial)
            self.counts[sentence] += 1
            self.partial = []       # reset partial and matches
            self.matches = []
            return []
        
        if not self.partial:        # first char of sentence
            self.matches = [(-count, sentence) for sentence, count in self.counts.items() if sentence[0] == c]
            self.matches.sort()
            self.matches = [sentence for _, sentence in self.matches]   # drop the counts
        else:
            i = len(self.partial)   # filter matches for c
            self.matches = [sentence for sentence in self.matches if len(sentence) > i and sentence[i] == c]
            
        self.partial.append(c)
        return self.matches[:3]
      
------------------------------------------------------------------------------------------------------------------------
Explanation:

We first build a trie for the given sentences and times. Note that we negate hot so that we can easily return the Top 3 hot sentences after sorting them in ascending order.
We initialize the following three variables to keep track of search state. They will be reset when the user types #:
search_term is used to track the current input.
last_node stores the previous node when we search in trie. It ensures that we do not always start searching from trie root when there are sentences that match the current input.
no_match is a flag. It ensures that we skip searching once there are no sentences that match the current input. The user can still type and we will record the input in search_term.
We only perform searching if the latest input character is in last_node's children.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_sentence = False
        self.hot = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, sentence, hot):
        node = self.root
        for char in sentence:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_sentence = True
        node.hot -= hot
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.build_trie(sentences, times)
        self.reset_search()

    def build_trie(self, sentences, times):
        self.trie = Trie()
        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[i])
    
    def reset_search(self):
        self.search_term = ""
        self.last_node = self.trie.root
        self.no_match = False
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.search_term, 1)
            self.reset_search()
        else:
            self.search_term += c

            if not c in self.last_node.children or self.no_match:
                self.no_match = True
                return []
            
            self.last_node = self.last_node.children[c]
            result = []
            self.dfs(self.last_node, self.search_term, result)

            return [sentences[1] for sentences in sorted(result)[:3]]

    def dfs(self, node, path, result):
        if node.is_sentence:
            result.append((node.hot, path))
        
        for char in node.children:
            self.dfs(node.children[char], path+char, result)
            
-------------------------------------------------------------------------------------
Explanation
At each prefix, store 3 most frequent sentences. It trades off space for better time complexity.
See below comments for more explanation
Implementation
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.three = []                                    # three sentences 
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, sentence, time):        
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]    
            for i, (t, s) in enumerate(node.three):        # update three sentences 
                if s == sentence:
                    tmp = node.three[:]
                    tmp[i][0] = time
                    break
            else:    
                tmp = node.three + [[time, sentence]]
            node.three = sorted(tmp, key=lambda x: (-x[0], x[1]))[:3]
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.d = collections.Counter()                      # keep tracking {sentence: time}
        self.trie = Trie()                                  # trie
        self.node = self.trie.root                          # pointer to root and move along with input characters
        for sentence, time in zip(sentences, times):        # add initial info
            self.d[sentence] += time       
            self.trie.add(sentence, time)       
        self.cur = ''                                       # prefix
        self.prefix_none = False                            # True if prefix cannot be found

    def input(self, c: str) -> List[str]:       
        if c == '#':                                        # input ends 
            self.node = self.trie.root                      # reset self.node to root
            self.d[self.cur] += 1                           # increment counter by 1
            self.trie.add(self.cur, self.d[self.cur])       # update sentence and time
            self.cur = ''                                   # reset prefix string
            self.prefix_none = False                        # reset this flag
            return []                                       # return
        self.cur += c                                       # making prefix
        if c not in self.node.children or self.prefix_none: # when prefix is not found the first time and time after 1st time
            self.prefix_none = True                         # set flag
            return []
        self.prefix_none = False                            # reset prefix_none flag
        self.node = self.node.children[c]                   # move to next node
        return [word for _, word in self.node.three]        # return 3 words
      
--------------------------------------------------------------------------------------------
This solution uses Trie data structure. To understand how it works you might want start with https://leetcode.com/problems/implement-trie-prefix-tree/

This Trie is going to store its nodes in a dict and will have only two methods:

insert - to insert sentence and its hot value
collect - to collect sentences in a manner that AutocompleteSystem needs it.
It will store the sentence and its hot value in a node in a special key HOT, and the value of this key is going to be the tuple(hot_value, sentence).
With such Trie data structure implementation of AutocompleteSystem becomes pretty straightforward.

class AutocompleteTrie:
    # special key that indicates of the end of the sentence and stores tuple(hot_value, sentence)
    HOT = '$'

    def __init__(self, max):
        # collect will result in not more than max sentences
        self.max = max
        self.trie = {}

    def insert(self, string, increment):
        node = self.trie
        for char in string:
            node = node.setdefault(char, {})
        prev = node.get(self.HOT, (0,))
        node[self.HOT] = (prev[0] + increment, string)

    def collect(self, prefix):
        # look for prefix node
        node = self.trie
        for char in prefix:
            node = node.get(char)
            if not node:
                return []

        # dfs for sentences starting with prefix node
        # heapq will help not to store more than self.max sentences
        stack, heap = [iter(node.items())], []
        while stack:
            char, next_node = next(stack[-1], (None, None))
            if char is None:
                stack.pop()
            elif char == self.HOT:
                heapq.heappush(heap, self._HeapComparator(next_node))
                if len(heap) > self.max:
                    heapq.heappop(heap)
            else:
                stack.append(iter(next_node.items()))

        # prepare final result
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        res.reverse()
        return res

    # wrapper class to handle same degree of hot in heapq
    class _HeapComparator(tuple):
        def __lt__(self, other):
            time1, sentence1 = self
            time2, sentence2 = other
            if time1 == time2:
                return sentence1 > sentence2
            return time1 < time2


class AutocompleteSystem:
    MAX = 3

    def __init__(self, sentences: list[str], times: list[int]):
        self.sentence = ''
        self.trie = AutocompleteTrie(self.MAX)
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)

    def input(self, c: str) -> list[str]:
        if c == '#':
            self.trie.insert(self.sentence, 1)
            self.sentence = ''
            return []

        self.sentence += c
        return self.trie.collect(self.sentence)
      
      
------------------------------------------------------------------------------------
import collections
from heapq import *
from typing import List

class Sentence:
    def __init__(self, content, count):
        self.content = content
        self.count = count

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count == other.count and self.content > other.content:
            # If several sentences have the same hot degree (count)
            # use ASCII-code order (smaller one appears first)
            # Hence, smaller string is considered larger in ranking
            return True
        return False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # Not necessary since we have `self.sentence`
        self.sentence = ''
        self.count = 0

    def search_char(self, ch):
        # returns the child node for `ch` if it exists, otherwise None
        if ch in self.children:
            return self.children[ch]
        return None

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.query_str = []  # current input query string
        self.query_node = self.root  # TrieNode that corresponds to the last char of current input query string

        for sent, time in zip(sentences, times):
            self.insert(sent, time)

    def insert(self, sentence, count=1):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.sentence = sentence
        node.count += count

    def topk(self, node, k=3):
        def dfs(node):
            if node.is_end:
                heappush(min_heap, Sentence(node.sentence, node.count))
                if len(min_heap) > k:
                    heappop(min_heap)
            for ch in node.children:
                dfs(node.children[ch])

        # Use a min heap to keep track of the top k queries
        min_heap = []
        # Starting from `node`, performs DFS to find all queries
        # Stores the k largest queries in the min_heap
        dfs(node)

        # Return top k queries from larger to smaller, hence using deque (doubly linked list)
        res = collections.deque()
        while min_heap:
            res.appendleft(heappop(min_heap).content)
        return res

    def input(self, c: str) -> List[str]:
        # The end of query
        # 1. save the query to the system
        # 2. clear query string and restore query node
        # 3. return []
        if c == '#':
            self.insert(''.join(self.query_str))
            self.query_str.clear()
            self.query_node = self.root
            return []

        # save newly typed charater to current query string
        self.query_str.append(c)

        # Try to get top k historical hot queries that have the same prefix as current query string
        # If query node is None --> query string (without newly typed character) is already not found in the system
        if self.query_node is not None:
            # For the current query node, try to find its child node for 'c'
            self.query_node = self.query_node.search_char(c)
            # If None --> query string (with newly typed character) is not found
            # Otherwise, find top k historical hot queries given the current query string
            if self.query_node is not None:
                return self.topk(self.query_node, k=3)

        # No sentense that have current "query_str"
        return []
Use backtracking to avoid storing every query string in trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

    def search_char(self, ch):
        # returns the child node for `ch` if it exists, otherwise None
        if ch in self.children:
            return self.children[ch]
        return None

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.query_str = []  # current input query string
        self.query_node = self.root  # TrieNode that corresponds to the last char of current input query string

        for sent, time in zip(sentences, times):
            self.insert(sent, time)

    def insert(self, sentence, count=1):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.count += count

    def topk(self, node, k=3):
        def dfs(node, path):
            if node.is_end:
                heappush(min_heap, Sentence(''.join(path), node.count))
                if len(min_heap) > k:
                    heappop(min_heap)
            for ch in node.children:
                path.append(ch)
                dfs(node.children[ch], path)
                path.pop()

        # Use a min heap to keep track of the top k queries
        min_heap = []
        # Starting from `node`, performs DFS to find all queries
        # Stores the k largest queries in the min_heap
        dfs(node, [])

        # Return top k queries from larger to smaller, hence using deque (doubly linked list)
        res = collections.deque()
        while min_heap:
            res.appendleft(''.join(self.query_str) + heappop(min_heap).content)
        return res

    def input(self, c: str) -> List[str]:
        # The end of query
        # 1. save the query to the system
        # 2. clear query string and restore query node
        # 3. return []
        if c == '#':
            self.insert(''.join(self.query_str))
            self.query_str.clear()
            self.query_node = self.root
            return []

        # save newly typed charater to current query string
        self.query_str.append(c)

        # Try to get top k historical hot queries that have the same prefix as current query string
        # If query node is None --> query string (without newly typed character) is already not found in the system
        if self.query_node is not None:
            # For the current query node, try to find its child node for 'c'
            self.query_node = self.query_node.search_char(c)
            # If None --> query string (with newly typed character) is not found
            # Otherwise, find top k historical hot queries given the current query string
            if self.query_node is not None:
                return self.topk(self.query_node, k=3)

        # No sentense that have current "query_str"
        return []
      
-------------------------------------------------------------------------------------------------------------------------------

import heapq

class TrieNode:
    def __init__(self):
        self.map = {}
        self.words = collections.defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        
        for sentence, time in zip(sentences, times):
            self.addWord(sentence, time)
        
        self.curinput = ''
        self.curNode = self.root
        
    def addWord(self, sentence,times):
            node = self.root
            for c in sentence:
                if c not in node.map:
                    node.map[c] = TrieNode()
                node = node.map[c]
                node.words[sentence]+=times

    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.curinput:
                self.addWord(self.curinput, 1)
                
            self.curinput = ''
            self.curNode = self.root
            return []
            
        self.curinput = self.curinput + c

        if not self.curNode or c not in self.curNode.map:
            self.curNode = None
            return []
    
        node = self.curNode.map[c]
        
        self.curNode = node
        result = heapq.nsmallest(3, [ (-freq, v) for v, freq in node.words.items()])
        
        return [ v for freq, v in result]
