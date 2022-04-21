'''
You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.

 

Example 1:

Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: s = "abcd"
Output: ["abcd"]
'''

so for input like {a, b, c}de{k, g} -> converting into [[a, b, c], [d], [c], [k, g]] and solve recursively to find all the permutation for the positions. After the conversion, let's say N for length of array, and K for maximum length of choices at each position.

Time Complexity -> (Edited, thanks to @user6299e)
First of all, we can consider this as repeat-allwowed permutation with K choices where K is length of nested array, and for N positions. So we have K^N choices
Then we have to take N times to build each permutations.
So it is O(N * K^N) where N is length of array and K is length of nested arrary.

consider we have these possible cases => [{a,b} x 10] vs [{a,b,c} x 7] vs [{a,b,c,d} x 5] (since we know length of s <= 50)
we have 2^10 vs 3^7 vs 4^5 = 1024 vs 2187 vs 1024
It seems the worst case we can have is where every list has 3 choices with 7 positions.

Space Complexity -> Since we are analyzing based on the structure of list from the input where K is number of choices for each position and N position (length of list)
Space used to build the options array is O(N * K). And recursive call can get stack upto O(N)
Therefore O(N * K)

class Solution:
    def expand(self, s: str) -> List[str]:
        i = 0
        options = []
        res = []
        
        # turn string into graph "{a, b}c{d, e}f" -> [[a, b], [c], [d, e], [f]]
        while i < len(s):
            if s[i] == '{':
                tmpArr = []
                while s[i] != '}':
                    if s[i].isalpha():
                        tmpArr.append(s[i])
                    i += 1
                tmpArr.sort()
                options.append(tmpArr)
            elif s[i].isalpha():
                options.append([s[i]])
            i += 1
        
        # classic backtracking template
        def backtrack(index, tmpStr):
            if len(tmpStr) == len(options):
                res.append(tmpStr)
                return
            for s in options[index]:
                prev = tmpStr
                tmpStr += s
                backtrack(index + 1, tmpStr)
                tmpStr = prev
        
        backtrack(0, "")
        return res
---------------------------------------------------------------------

class Solution:
    def expand(self, s: str) -> List[str]:
        ans = [""]
        for z in s.replace("{", " ").replace("}", " ").split():
            ans = [x + y for x in ans for y in sorted(z.split(","))]
                
        return ans
----------------------------------

class Solution:
    def expand(self, s: str) -> List[str]:
        from itertools import product
        #Checking for no brace
        if '{' not in s:
            return [s]
        
        combos, result = [], []
        blueprint = ''
        flag = False
        
        #1.Collecting list of combos and creating a blueprint of result
        #Ex: combos = [[a,b],[d,e]], blueprint = '_c_f'
        for i in s:
            if i == '}':
                flag = False
                combos.append(new)
                
            elif i =='{':
                flag = True
                new = []
                blueprint += '_'
            else:
                if i != ',':
                    if flag == True:
                        new.append(i)
                    else:
                        blueprint += i
                        
        #2.Get the resultant combinations 
        #Ex:[('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e')]

        req_combos = list(product(*combos))
        
        #3. Insert combo to blueprint
        for i in req_combos:
            idx = 0
            other = blueprint
            for k,j in enumerate(other):
                if j == '_':
                    other = other[:k] + i[idx] + other[k+1:]
                    idx += 1
            result.append(other)
        
        result.sort()
        
        return result 
            
--------------------------------------------------------------------------

class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        to_expand = collections.deque()
        to_expand.append(s)
        
        while to_expand:
            poped_s: str = to_expand.popleft()
            if "{" in poped_s:
                open_bracket_idx = poped_s.index("{")
                close_bracket_idx = poped_s.index("}", open_bracket_idx + 1)
                prefix = poped_s[:open_bracket_idx]
                suffix = poped_s[close_bracket_idx+1:]
                for ch in sorted(poped_s[open_bracket_idx+1:close_bracket_idx].split(",")):
                    to_expand.append(prefix + ch + suffix)
            else:
                res.append(poped_s)
        
        return res
-----------------------------------------------------------------

class Solution:
    def expand(self, s: str) -> List[str]:
        dic = defaultdict(list)
        key = 0
        i = 0
        # in the curly braces or not, at the beginning it is False
        flag = False
        
        # preprocess the input string, store as dict
        for i in range(len(s)):
            if s[i].islower() and not flag:
                dic[key].append(s[i])
                key += 1
            
            if s[i].islower() and flag:
                dic[key].append(s[i])
                
            elif s[i] == '{':
                flag = True

            elif s[i] == '}':
                key += 1
                flag = False
                
        # sort the dic
        for arr in dic.values():
            arr.sort()
        
        
        final_len = len(dic)
        result = []
        
        def backtrack(index, path):
            nonlocal final_len
            
            if index == final_len:
                # attention: deep copy here!
                result.append(path[:])
            
            for i in range(len(dic[index])):
                path += dic[index][i]
                backtrack(index + 1, path)
                path = path[:-1]
        
        backtrack(0, "")
        
        return result
-----------------------------------------------------------------------------

class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        
        n = len(s)
        i = 0 
        j = 0 
        flag = False
        chars = defaultdict(set)
        
        while i < n:
            if s[i] == '{':
                flag = True
                i += 1
            elif flag and s[i].isalpha():
                chars[j].add(s[i])
                i += 1
            elif not flag and s[i].isalpha():
                chars[j].add(s[i])
                i += 1
                j += 1
            elif s[i] == ',':
                i += 1
            elif s[i] == '}':
                i += 1
                j += 1
                flag = False
                 
        stack = []
        for c in chars[0]:
            stack.append((c, 0))
            
        while stack:
            char, idx = stack.pop()
            if idx +1 not in chars:
                res.append(char)
            else: 
                for c_ in chars[idx+1]:
                    stack.append((char + c_, idx+1))

        res.sort()
        return res
      
      
      
      
        
      
      
