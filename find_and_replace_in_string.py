'''
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.
'''

def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
	lookup = {i: (src, tgt) for i, src, tgt in zip(indexes, sources, targets)}
	i, result = 0, ""
	while i < len(S):
		if i in lookup and S[i:].startswith(lookup[i][0]):
			result += lookup[i][1]
			i += len(lookup[i][0])
		else:
			result += S[i]
			i += 1
	return result

--------------------------------------------

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        idxMap = {}
        for i, index in enumerate(indices):
            idxMap[index] = i
        
        def checker(strinPtr, source):
            for char in source:
                if s[strinPtr] != char:
                    return False
                strinPtr += 1
            return True
        
        res = ""
        strPtr = 0
        while strPtr < len(s):
            if strPtr in idxMap:
                if checker(strPtr, sources[idxMap[strPtr]]):
                    res += targets[idxMap[strPtr]]
                    strPtr += len(sources[idxMap[strPtr]])
                    continue
            res += s[strPtr]
            strPtr += 1
        
        return res
      
-------------------------------------
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:    
        result=list(s)
        for begin,src,tgt in zip(indices,sources,targets):
            if s.startswith(src,begin):
                result[begin]=tgt
                for idx in range(begin+1,begin+len(src)):
                    result[idx]=''
        return ''.join(result)
