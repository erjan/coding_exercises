'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = Counter(words)

        res = sorted(list(d.keys()), key = lambda x: (-d[x], x))
        return res[:k]
      
------------------------------------------------------------------------
def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]
-----------------------------------------------------------------------------------------
from heapq import heappush, heappop, heappushpop

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapper = defaultdict(int)
        for word in words:
            mapper[word] += 1
        
        h = list()
        for word, freq in mapper.items():
            node = Node(word, freq)
            if len(h) == k:
                heappushpop(h, node)
            else:
                heappush(h, node)
                
        result = list()
        while h:
            result.append(heappop(h).word)
        return result[::-1]
----------------------------------------------
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a = {}
        
		for word in words:
            if word in a:
                a[word] += 1
            else:
                a[word] = 1
        
		l = list(a.items())
        l = [(-j,i) for i,j in l]
        heapq.heapify(l)
        ret = []
        for i in range(k):
            _,w = heapq.heappop(l)
            ret.append(w)
        return ret
