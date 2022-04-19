'''
You are given a string s and an array of strings words. You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag. If two substrings wrapped by bold tags are consecutive, you should combine them.

Return s after adding the bold tags.

 

Example 1:

Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
Example 2:

Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"
'''

Here are two key points:

Trie Tree is used to speed up string match (faster than find or startwith in large query request).
Using Merge Intervals instead of mask to reduce Time and Space Complexity, both from O(n) to O(m), m represets interval numbers after merged.
class Solution:
    def addBoldTag(self, s: str, dict: 'List[str]') -> str:
        trie, n, intervals, res = {}, len(s), [], ""

        # create trie tree
        for w in dict:
            cur = trie
            for c in w:
                cur = cur.setdefault(c, {})
            cur["#"] = 1

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, max_end = trie, None
            for j in range(i, n):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if "#" in cur:
                    max_end = j + 1
            # just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += s[prev_end:start] + '<b>' + s[start:end] + "</b>"
            prev_end = end
        return res + s[prev_end:]
      
------------------------------------------------------------------------------------
Difference in approach is that :

Trie is used to speed up match (faster than find or startwith in large query request).
Using Merge Intervals instead of mask to reduce Time Complexity coz in this case merge is O(1)
Both are same ques :

616. Add Bold Tag in String
758. Bold Words in String
Approach 1: Trie + Mask
class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        self.trie = Trie()
        dp = [False] * len(s)
        res = []
        
        # add dict to trie
        for word in dict:
            self.addToTrie(word)
        
        # mark all indexes that cover bold
        for i in range(len(s)):
            node = self.trie
            end = i
            
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.isWord:
                    end = j + 1
            
            dp[i:end] = [True] * (end - i)
        
        # insert bold tags
        for i in range(len(s)):
            
            # insert open tags
            if dp[i] and (i == 0 or not dp[i-1]):
                res.append('<b>')
            
            # insert char
            res.append(s[i])
            
            # insert closing tags
            if dp[i] and (i == len(s) - 1 or not dp[i+1]):
                res.append('</b>')
        
        return ''.join(res)
            
    
    def addToTrie(self, word):
        node = self.trie
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.isWord = True
Approach 2: Trie + Merged Intervals
class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        self.trie = Trie()
        self.mergedIntervals = []
        
        for word in words:
            self.addToTrie(word)
        
        for i in range(len(s)):
            node = self.trie
            end = None
            
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.isWord:
                    end = j + 1
            
            if end:
                self.addToIntervals([i, end])
        
        res = []
        prevEnd = 0
        for start, end in self.mergedIntervals:
            res.append(s[prevEnd:start])
            res.append('<b>')
            res.append(s[start:end])
            res.append('</b>')
            prevEnd = end
        
        # if anything remaining
        res.append(s[prevEnd:])
        
        return ''.join(res)
    
    def addToIntervals(self, interval):
        if not self.mergedIntervals or self.mergedIntervals[-1][1] < interval[0]:
            self.mergedIntervals.append(interval)
        else:
            self.mergedIntervals[-1][-1] = max(self.mergedIntervals[-1][-1], interval[1])
    
    def addToTrie(self, word):
        node = self.trie
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        
        node.isWord = True
----------------------------------------------------------------------------------------------------
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # first, match occurances of each word in s and mark start and end tags
        # reduction to merge intervals problem
        # then merge tags together (removing nested tags) 
        # apply the merged tags to the string s
        
        # build list of intervals -- start (inclusive) to end (exlusive) (no regex)
        intervals = []
        windows = set([len(word) for word in words]) # removing duplicate window lengths
        words = set(words) # hash words for quick lookup
        n = len(s)
        for window in windows: 
            for i in range(n-window+1): 
                if s[i:i+window] in words:
                    intervals.append([i, i+window])
        
        # reduction to merge intervals
        intervals.sort(key=lambda x: (x[0], x[1])) # O(n log n)
        merged = []
        for itv in intervals:
            if not merged or merged[-1][1] < itv[0]:
                merged.append(itv)
            else:
                merged[-1][1] = max(merged[-1][1], itv[1])
        
        # convert merged itvs to bold tags
        s_arr = list(s)
        for itv in merged[::-1]: # reverse to allow multiple insertions on the same list
            s_arr.insert(itv[1], '</b>')
            s_arr.insert(itv[0], '<b>')
            
        return ''.join(s_arr)
      
---------------------------------------------------------------------------------------------------
Explanation
First find all open & close tags, and sort by index & open tag first
Similar to Meeting Rooms II, merging tags and keep only valid, non-nested tags
Apply valid tags on original string
Implementation
Time Complexity: O(m*n), m = len(words), n = len(s)
Space Complexity: O(n)
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        windows = set([len(word) for word in words])  # get unique window length (reduce iteration), O(m)
        words = set(words)                            # convert `words` to hash set for faster search, O(m)
        n = len(s)
        tag_list = []
        for window in windows:                        # for each window size, O(m)
            for i in range(n-window+1):               # for each word at this size, O(n)
                if s[i:i+window] in words:            # see if each word at current window size is in the set
                    tag_list.append((i, 1))           # append open tag index, 1 meaning open tag
                    tag_list.append((i+window, -1))   # append close tag index, -1 meaning close tag
        tag_list.sort(key=lambda x: (x[0], -x[1]))    # sort by index & open tag first, O(n*logn)
        dq = collections.deque()
        cnt = 0
        for idx, sign in tag_list:                    # merging tags, O(n)
            if not cnt:                               # if no open tags, add open tag
                cnt += 1
                dq.append(idx)
            elif cnt == 1 and sign == -1:             # append close tag only when previous tag is open tag (no nested tags)
                cnt -= 1
                dq.append(idx)
            else:                                     # any other cases, only count tags, not append any
                cnt += 1 if sign == 1 else -1
        ans = ''
        open_tag = True
        for i, c in enumerate(s):                     # apply tags on original string `s`, O(n)
            if dq and i == dq[0]:                     # add tags
                ans += '<b>' if open_tag else '</b>'  
                open_tag = not open_tag
                dq.popleft()                          # remove used tag
            ans += c
        return ans + '</b>' if dq else ans            # add ending tag if there is one
      
--------------------------------------------------------------------------------------------------------------------------------------
Main idea:
create a trie for words
for each char in the s with index i, we do search word on the trie, we will return the longest match word from the i. We will return the longest match word that can be reached from the index i, return empty if not found
if we find a word with length len form index i, we can say: index from i to i + len - 1 should be wrapped by and
store the valid index in a set indices, note: as we add index from front to end, the elements in indices are in increasing order
add <b> and </b> to the original s according to indices
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        r = self.root
        for char in word:
            if char in r:
                r = r[char]
            else:
                r[char] = {}
                r = r[char]
        r['in'] = word
                          
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        indices = set()
        root = trie.root
        n = len(s)
        
        def search(s, index, r):
            result = ""
            for i in range(index, n):
                char = s[i]
                if char not in r:
                    return result
                else:
                    r = r[char]
					
                # update the longest match word
                if 'in' in r:
                    if not result:
                        result = r['in']
                    elif len(r['in']) > len(result):
                        result = r['in']
						
            return result
                
        for i, char in enumerate(s):
            r = root
            result = search(s, i, r)
            if result:
                # [index, index + length] occurs in words
                # becasue we add the index from front to end, the elements in indices are in increasing order
                for j in range(i, i + len(result)):
                    indices.add(j)
        
        # add <b> and </b> to the original s
        # boolean variable start and end means the next symbol we will add
        result = ""
        start = True
        end = False
        print(indices)
        for i in range(n):
            if i in indices:
                if start:
                    result = result + '<b>'
                    start = False
                    end = True
                result = result + s[i]
            else:
                if end:
                    result = result + '</b>'
                    start = True
                    end = False
                result = result + s[i]
        
        if n-1 in indices:
            result = result + '</b>'
            
        return result
      
        
      
