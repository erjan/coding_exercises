'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the 
strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing 
order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s 
comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is 
smaller if and only if s.length < t.length.
'''


We do not need a DFS or BFS to detect if there is a cycle, because if the graph stop shrinking before all nodes are removed, it indicates that solution doesn't exist (a cycle in the graph)

class Node(object):
def __init__(self):
    self.IN = set()
    self.OUT = set()

class Solution(object):
def alienOrder(self, words):
   # find out nodes
   graph = {}
    for word in words:
        for letter in word:
            if letter not in graph:
                graph[letter] = Node()

    # find out directed edges (from StefanPochmann)
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                graph[a].OUT.add(b)
                graph[b].IN.add(a)
                break

    # topo-sort
    res = ""
    while graph:
        oldlen = len(graph)

        for key in graph:
            if not graph[key].IN:   # to remove this
                for key2 in graph[key].OUT:
                    graph[key2].IN.remove(key)
                del graph[key]
                res += key
                break

        if oldlen == len(graph): # if shrinking stops, solution doesn't exist
            return ""
        oldlen = len(graph)
    return res
  
------------------------------------------------------------------------------
from collections import deque

class Solution(object):
    def alienOrder(self, words):
        chars = set(c for w in words for c in w)
        graph, indeg = {c:[] for c in chars}, {c:0 for c in chars}
        for pair in zip(words, words[1:]):
            for c1, c2 in zip(*pair):
                if c1 != c2:
                    graph[c1] += c2,
                    indeg[c2] += 1
                    break

        queue = deque([char 
                       for char in indeg 
                       if not indeg[char]])
        ret = ""
        while queue:
            char = queue.popleft()
            ret += char
            for n in graph[char]:
                indeg[n] -= 1
                if not indeg[n]:
                    queue.append(n)
        return ret * (set(ret) == chars)

-------------------------------------------------------------------------------------------------
DFS:

    import collections
    
    self.greater = collections.defaultdict(set)
    
    for i in range(len(words)-1):
        minlen = min(len(words[i]), len(words[i+1]))
        j=0
        while j < minlen and words[i][j] == words[i+1][j]:
            j+=1
        if j < minlen:
            self.greater[words[i][j]].add(words[i+1][j])
            
    charset = set(''.join(words))
    
    self.mark = {}
    
    self.orderlist = collections.deque()
    
    for i in charset:
        if i not in self.mark:
            if not self.visit(i):
                return ""
    
    return "".join(self.orderlist)
        
def visit(self, i):
    
    if i in self.mark and self.mark[i] == 2:
        return False
    elif i in self.mark and self.mark[i] == 1:
        return True
    
    if i not in self.mark:
        self.mark[i] = 2
        
        for j in self.greater[i]:
            if not self.visit(j):
                return False
            
        self.mark[i] = 1
        
        self.orderlist.appendleft(i)
        
        return True
BFS:

    import collections
    
    que = collections.deque()
    
    less = collections.defaultdict(set)            
    greater = collections.defaultdict(set)
    
    for i in range(len(words)-1):
        minlen = min(len(words[i]), len(words[i+1]))
        j=0
        while j < minlen and words[i][j] == words[i+1][j]:
            j+=1
        if j < minlen:
            less[words[i][j]].add(words[i+1][j])
            greater[words[i+1][j]].add(words[i][j])
            que.append([words[i][j],words[i+1][j]])
            
    charset = set(''.join(words))
    
    subset = [x for x in charset if x not in greater]
    
    while que:
        [k,l] = que.popleft()
        if l in less:
            for m in less[l]:
                if m == k:
                    return ""
                elif k not in greater[m]:
                    greater[m].add(k)
                    que.append([k,m])
                    
    return ''.join(subset)+''.join(w[0] for w in sorted(greater.items(), key=lambda x: len(x[1])))
Toposort:

    import collections
    
    less = collections.defaultdict(set)            
    greater = collections.defaultdict(set)
    
    for i in range(len(words)-1):
        minlen = min(len(words[i]), len(words[i+1]))
        j=0
        while j < minlen and words[i][j] == words[i+1][j]:
            j+=1
        if j < minlen:
            less[words[i][j]].add(words[i+1][j])
            greater[words[i+1][j]].add(words[i][j])
            
    charset = set(''.join(words))
    
    orderlist = []
    
    deque = collections.deque([x for x in charset if x not in greater])
    
    while deque:
        i = deque.popleft()
        if i in less:
            for j in less[i]:
                greater[j].remove(i)
                if len(greater[j]) == 0:
                    del greater[j]
                    deque.append(j)
        orderlist.append(i)
        
    if len(greater) > 0:
        return ""
    else:
        return "".join(orderlist)
      
      
-----------------------------------------------------------------------------------------
Hopefully this is simple and easy to understand. I went through many solutions but felt like either there were too many fancy tricks in there or they were too bloated.

We need to build a graph by traversing the input. We can compare the (i)th word with the (i+1)th word to determine the relationship i.e w comes before e so in our graph we would have an entry {"w": "e"}

The second important bit is counting how many nodes are dependent on a node. For example, in ["ac","ab",b"], b has a dependency on "a" and c". So we can't just append "b" (or any character) to the result when we see it in our BFS. We need to reduce the count by 1 on every occurence and once the count hits 0 we can be satisfied that no one else will be looking for "b".

def alienOrder(self, words: List[str]) -> str:

    graph = {}
    dependencyCount = {}
	
    # add all possible values in graph
    for word in words:
        for char in word:
            graph[char] = []
            dependencyCount[char] = 0
			
    # make our graph
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
        index = 0; length = min(len(word1),len(word2))
        while index < length and word1[index] == word2[index]:
            index+=1
			
		# you can use break and have a different loop but most interviewers don't like breaks
        if index < length:
            graph[word1[index]].append(word2[index])
            dependencyCount[word2[index]]+=1
     
	# figure out the staring point. The starting point has to be nodes that aren't dependent on someone else - hence the 0.
    seed = [];
    for key, val in dependencyCount.items():
        if val == 0:
            seed.append(key)
    result  = []

	# Straight forward BFS
    while len(seed) > 0:
        curr = seed.pop(0)
        result.append(curr)
        for nei in graph[curr]:
            dependencyCount[nei] = dependencyCount[nei]  - 1
            if dependencyCount[nei] == 0:
                seed.append(nei)
     
	 # It must have all the nodes in the graph
    return ''.join(result) if len(result) == len(dependencyCount) else ''
                                                                                              
-----------------------------------------------------------------------------------
                                                                                              The tricky part is to build the graph and model the relationship correctly. Here are some corner cases to watch out for when building the graph:

cases like ["abc, ab"] is not valid but ["ab", "abc"] is valid
cases like ["a", "b", "ab"], when we compare "a", "b", we already marked a < b and increase b's indegree. When we compare "a" and "ab", we don't want to double count the indegree. That's why I have the if w2[i] not in graph[w1[i]] statement
from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # the first letter would be - no other letters smaller than it
        # then after removing the first letter, 
        # find the second one w/ no smaller letters
        graph, degree = self.build_graph(words)
        
        source = deque()
        for key in degree:
            if degree[key] == 0:
                source.append(key)
        
        res = []
        while source:
            char = source.popleft()
            res.append(char)
            
            for child in graph[char]:
                degree[child] -= 1
                if degree[child] == 0:
                    source.append(child)
        
        if len(res) < len(degree):
            return ""
        
        return ''.join(res)
        
    def build_graph(self, words):
        graph, degree = {}, {}
        
        # add vertices
        for w in words:
            for char in w:
                if char in graph:
                    continue
                graph[char] = []
                
                if char in degree:
                    continue
                degree[char] = 0
        
        
        # build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # a flag to prevent cases like "abc", "ab"
            # while "ab", "abc" is okay
            found = False
            for i in range(min_len):
                if w1[i] != w2[i]:
                    # w1[i] < w2[i]
                    if w2[i] not in graph[w1[i]]:
                        graph[w1[i]].append(w2[i])
                        degree[w2[i]] += 1
                    found = True
                    break
            
            if found == False and len(w1) > len(w2):
                return "", ""
        return graph, degree
