'''
Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).
'''


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = list()
        for w in words:
            print('-----------------------------')
            for i in range(len(text)):

                if text[i] == w[0]:
                    #print('first match at', text[i])
                    if text[i: i + len(w)] == w:
                        print()
                        print('found! the word', w)
                        print('at i', i, ' and j: ', (i + len(w)-1))
                        res.append([i, (i + len(w)-1)])

        print('end')
        res.sort(key=lambda sl: (sl[0], sl[1]))

        print(res)
        return res
      
#alternative solution using TRIE

# https://leetcode.com/problems/index-pairs-of-a-string/discuss/1445555/Trie-with-detailed-explanation

def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
    
        result = []
        for idx in range(len(text)):
            self.traverse(idx, text, trie, result)
            
        return result
    
    def traverse(self, idx, text, trie, result):
        nodes = trie.root
        for i in range(idx, len(text)):
            letter = text[i]
            if letter not in nodes:
                return False
            nodes = nodes[letter]
            if '*' in nodes:
                result.append([idx, i])
                

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = True

        
#KMP solution

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        def KMP_table(pattern):
            lp = len(pattern)
            tb = [0 for _ in range(lp)]

            pidx = 0 
            for idx in range(1, lp): 
                while pidx > 0 and pattern[idx] != pattern[pidx]:
                    pidx = tb[pidx-1]

                if pattern[idx] == pattern[pidx] :
                    pidx += 1
                    tb[idx] = pidx

            return tb
        
        def KMP(word, pattern):
         
            table = KMP_table(pattern)

            results = []
            pidx = 0

            for idx in range(len(word)):
            
                while pidx > 0 and word[idx] != pattern[pidx] :
                    pidx = table[pidx-1]
            
                if word[idx] == pattern[pidx]:
                    if pidx == len(pattern)-1 :
                        results.append(idx-len(pattern)+1)
                        pidx = table[pidx]
                    else:
                        pidx += 1

            return results
        
        res = defaultdict(list)
        for pattern in words:
            result = KMP(text, pattern)
            for idx in result:
                res[idx].append(idx+len(pattern)-1)
                
        mink = float('inf')
        maxk = float('-inf')
        
        for k, v in res.items():
            v.sort()
            mink = min(mink, k)
            maxk = max(maxk, k)
        if not res:
            return []
        r = []    
        for k in range(mink, maxk + 1):
            for val in res[k]:
                r.append([k, val])
        
        
        return r
