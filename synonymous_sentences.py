'''
You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically.

 

Example 1:

Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
'''

Explanation
Use union find to effective find all synonyms and use backtracking to try out all possible solutions
Implementation
class UF:                                                    # pretty standard Union Find structure
    def __init__(self, words):
        self.p = [i for i in range(10)]
        
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj: self.p[pj] = pi
            
    def find(self, i):
        if self.p[i] != i: self.p[i] = self.find(self.p[i])
        return self.p[i]    
    
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        words = text.split(' ')                              # split text to list for easier alternation
        n, uf = len(words), UF(words)
        cur_id, word_id, id_word = 0, collections.defaultdict(int), collections.defaultdict(str)
        for a, b in synonyms:                                # create word_id, id_word relation for each word that has synonym
            if a not in word_id: word_id[a], id_word[cur_id], cur_id = cur_id, a, cur_id+1
            if b not in word_id: word_id[b], id_word[cur_id], cur_id = cur_id, b, cur_id+1
            ai, bi = word_id[a], word_id[b]
            uf.union(ai, bi)
        uf.p, ans = uf.p[:cur_id], list()
        def dfs(words, idx):                                 # backtracking
            if idx == n: ans.append(' '.join(words))
            else:
                for i in range(idx, n):
                    tmp_word = words[i]
                    if tmp_word not in word_id: continue     # if doens't have a synonym, skip
                    word_parent = uf.find(word_id[tmp_word])
                    for j, _ in enumerate(uf.p):             # try out all possible synonyms
                        pj = uf.find(j)
                        if pj == word_parent and tmp_word != id_word[j]:
                            words[i] = id_word[j]
                            dfs(words, i+1)
                    words[i] = tmp_word                      # remember to recover the word back to original for next iteration
                ans.append(' '.join(words))    
        dfs(words, 0)                    
        return sorted(ans)                                   # don't forget to sort the result
-------------------------------------------------------------------------------------------------------

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        G = defaultdict(set)
        for x,y in synonyms:
            G[x].add(y)
            G[y].add(x)
        
        def dfs(w,ans):
            ans.add(w)
            for x in G[w]:
                if x not in ans: dfs(x,ans)
                    
        X = text.split()
        out = []
        for w in X:
            out1 = []
            if w in G:
                wset = set()
                dfs(w, wset)
                for w1 in wset:
                    if out: out1.extend([x+" "+w1 for x in out])
                    else: out1.append(w1)
            else: out1 = [x+" "+w for x in out] if out else [w]
            out = out1
        return sorted(out)
-------------------------------------------------

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        g = defaultdict(list)
        for u, v in synonyms:
            g[u].append(v)
            g[v].append(u)
        
        def findSynonym(w):
            if w in syns:
                return syns[w]
            syn = set((w,))
            def dfs(u):
                syn.add(u)
                for v in g[u]:
                    if v not in syn:
                        dfs(v)
            dfs(w)        
            syn = sorted(syn)    
            for s in syn:
                syns[s] = syn
            return syn
        
        syns = {}
        words = []
        for w in text.split():
            words.append(findSynonym(w))
        return [" ".join(arr) for arr in itertools.product(*words)]
---------------------------------------------------------------------------

from copy import deepcopy


class Solution:
    def generateSentences(self, synonyms, text):
        ans = []
        for i in range(len(synonyms)): synonyms[i].sort()
        synonyms.sort()
        for i in range(len(synonyms)):
            if not synonyms[i]: continue
            for j in range(i + 1, len(synonyms)):
                if synonyms[j][0] in synonyms[i]:
                    synonyms[i].append(synonyms[j][1])
                    synonyms[j] = []
                elif synonyms[j][1] in synonyms[i]:
                    synonyms[i].append(synonyms[j][0])
                    synonyms[j] = []
            synonyms[i].sort()
        synonyms = list(filter(lambda x: x, synonyms))
        for word in text.split(" "):
            idx = -1
            for i, syn in enumerate(synonyms):
                if word in syn:
                    idx = i
                    break
            if idx == -1:
                if not ans:
                    ans.append([word])
                else:
                    for i in range(len(ans)): ans[i].append(word)
            else:
                if not ans:
                    ans.append([synonyms[idx][0]])
                    ans.append([synonyms[idx][1]])
                else:
                    nxt = []
                    for sentence in ans:
                        for syn in synonyms[idx]:
                            tmp = deepcopy(sentence)
                            tmp.append(syn)
                            nxt.append(tmp)
                    ans = nxt
        for i in range(len(ans)): ans[i] = " ".join(ans[i])
        return ans
      
      
      
      
      
