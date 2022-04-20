'''
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.

 

Example 1:

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
Example 2:

Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: true
Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.
Example 3:

Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: false
Explanation: "leetcode" is not similar to "onepiece".
 
 '''



Understand the problem
Basically we want to check the similarity between two sentences.

The length of two sentences should be the same.
If the lengths are not the same, we could immediately return False
Check similar meaning of two words by using list of similar pairs
Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
See any patterns?

It looks like we do grouping for words. In that example, it will be:

["great", "good", "fine"]
["drama", "acting"]
["skills", "talent"]
Explore Edge Cases
What if the word in either of the sentences doesn't exist in the list of similarPairs?
There are two possibilities.

The words on two sentences are exactly the same, return True

Input: sentence1 = ["mantap", "batik", "cat"], sentence2 = ["mantap", "motif", "canting"], similarPairs = [["motif", "canting"], ["batik", canting"], ["cat", "motif"]]
Output: True
Explanation: group: ["motif", "canting", "batik", "cat"]. Even though "mantap" word doesn't belong to any group, this word exists in the same index for both sentences.
The words on two sentences are different, return False

Input: sentence1 = ["webdev", "java", "kubernetes"], sentence2 = ["mobdev", "python", "docker"], similarPairs = [["java", "python"], ["kubernetes", docker"]]
Output: False
Explanation: group 1: ["java", "python"], group 2: ["kubernetes", docker"]. "webdev" and "mobdev" doesn't belong to any group and both words are different.
Build the solution
We can use DFS to traverse from word to another word to check whether the word will have the similar meanings or not. Using DFS, it will cost O(n.p) for n is the maximum length of the words and p for the length of pair.

Can we do better?
Seeing this problem like we are trying to make grouping.

How do we make it group?
We can start to connect two words from the list of similarPair. Let's use the number instead of word to make it easier.

similarPair = [[0, 1], [1, 2], [3, 4]] will be [0, 1, 2] and [3, 4].

We can make it as array: [0, 1, 2, 3, 4] and connect each pair one by one. Let's agree that we will pick the first number on the list become the root.

First pair [0, 1] will make [0, 0, 2, 3, 4] because number 1 will be changed since 0 as root
Second pair [0, 2] will make [0, 0, 0, 3, 4] because number 2 will be changed since 0 as root
Third pair [3, 4] will make [0, 0, 0, 3, 3] because number 4 will be changed since 3 as root
Now we have [0, 0, 0, 3, 3] and we can see that there are two groups which are 0 and 3.

This idea is Union Find.

Implement Union Find
Check the length of two sentences whether is the same or not. We could return False immediately if it's not the same.
Convert words into number to make it easier
Build Union Find with size of the unique word
Do compress to make the exact roots
Connect two word, but don't forget check first whether the word exists in similarPair or not
Return False immediately if the word can't be connected
Return True if we do union for the words and no obstacles
from collections import defaultdict

class UnionFind:
  def __init__(self, size):
    self.root = [i for i in range(size)]
    self.rank = [1]*size
    
  def find(self, x):
    rootX = self.root[x]
    
    if rootX == x:
      return x
    return self.find(rootX)

  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    
    if rootX == rootY:
      return True
    else:
      if self.rank[rootX] > self.rank[rootY]:
        self.root[rootY] = rootX
        self.rank[rootX] += 1
      else:
        self.root[rootX] = rootY
        self.rank[rootY] += 1
      return False
    
  def compress(self):
    for i in range(len(self.root)):
      res = self.find(self.root[i])
      self.root[i] = res
    return self.root
  
  def connected(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    return rootX == rootY
    
class Solution:
  def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2):
      return False
    
    maps = {}
    count = 0
    for pair in similarPairs:
      if pair[0] not in maps:
        maps[pair[0]] = count
        count += 1
      if pair[1] not in maps:
        maps[pair[1]] = count
        count += 1
    
    n = len(maps)
    uf = UnionFind(n+1)
    
    for pair in similarPairs:
      x = maps[pair[0]]
      y = maps[pair[1]]
      uf.union(x, y)
    
    uf.compress()
    
    for i in range(len(sentence1)):
      if sentence1[i] not in maps and sentence2[i] not in maps:
        if sentence1[i] == sentence2[i]:
          continue
      if sentence1[i] not in maps or sentence2[i] not in maps:
        return False
  
      x = maps[sentence1[i]]
      y = maps[sentence2[i]]
      
      if not uf.union(x, y):
        return False
    return True
--------------------------------------------------------------
                                                    
class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def contains(self, word):
        return word in self.parent

    def add(self, word):
        self.parent[word] = word
    
    def find(self, word):
        result = self.parent[word]
        while result != self.parent[result]:
            self.parent[result] = self.parent[self.parent[result]]
            result = self.parent[result]
        return result
    
    def union(self, first, second):
        p1 = self.find(first)
        p2 = self.find(second)
        
        if p1 == p2:
            return
        
        self.parent[p1] = p2
        

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        uf = UnionFind()
        
        l1 = len(sentence1)
        l2 = len(sentence2)
        
        if l1 != l2:
            return False
        
        for w1, w2 in similarPairs:
            if not uf.contains(w1):
                uf.add(w1)
            if not uf.contains(w2):
                uf.add(w2)
            
            uf.union(w1, w2)
        
        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            
            if (not uf.contains(word1)) or (not uf.contains(word2)):
                return False

            if uf.find(word1) != uf.find(word2):
                return False
        
        return True
                                                    
----------------------------------------------------------------
                                                    
                                                    def areSentencesSimilarTwo(sentence1, sentence2, similarPairs):
    """
    :type sentence1: List[str]
    :type sentence2: List[str]
    :type similarPairs: List[List[str]]
    :rtype: bool
    """
    import collections
    if len(sentence1) != len(sentence2):
        return False

    # build the graph
    graph = collections.defaultdict(list)
    for v1,v2 in similarPairs:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(w1, w2):
        seen.add(w1)
        if w1 == w2:
            return True
        for nei in graph[w1]:
            if nei not in seen:
                if dfs(nei, w2):
                    return True
        return False

    # check on each pair independently
    for w1, w2 in zip(sentence1, sentence2):
        seen = set()
        if not dfs(w1, w2):
            return False

    return True
--------------------------------------------
                                                    
                                                    class UnionFind: 

    def __init__(self): 
        self.parent = {}
        self.rank = defaultdict(lambda: 1)
        
    def find(self, p): 
        if p not in self.parent: self.parent[p] = p
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        
        uf = UnionFind()
        for x, y in similarPairs: uf.union(x, y)
        for x, y in zip(sentence1, sentence2): 
            if uf.find(x) != uf.find(y): return False 
        return True 
-----------------------------------------------------
                                                    class Solution:
    
    class DSU:
        def __init__(self, words):
            self.links = {w:w for w in words}
            self.sizes = defaultdict(lambda: 1)
            
        def find(self, u):
            parent = u
            while parent != self.links[parent]:
                parent = self.links[parent]
            curr = u
            while curr != parent: # path compression
                temp = curr
                curr = self.links[curr]
                self.links[temp] = parent
            return parent
            
        def union(self, u, v):
            u, v = self.find(u), self.find(v)
            if u == v:
                return
            if self.sizes[u] < self.sizes[v]: # merge the smaller set into the bigger set
                u,v = v,u
			self.links[v] = u
            self.sizes[u] += self.sizes[v]
            self.sizes[v] = 0
            
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        def wordsAreSimilar(i):
            return words1[i] == words2[i] or DSU.find(words1[i]) == DSU.find(words2[i])
        
        def sentencesAreSimilar():
            if len(words1) != len(words2):
                return False
            return all(wordsAreSimilar(i) for i in range(len(words1)))
        
        words = set(words1)|set(words2)|set([w for l in pairs for w in l]) # set containing all words in words1, words2, pairs
		DSU = self.DSU(words)
		for w1, w2 in pairs:
			DSU.union(w1, w2)
        return sentencesAreSimilar()
-----------------------------------------------------------------------                                                    
                                                    
                                                    
                                                    
                                                    
