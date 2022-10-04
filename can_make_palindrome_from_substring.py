'''
You are given a string s and array queries where queries[i] = [lefti, righti, ki]. We may rearrange the substring s[lefti...righti] for each query and then choose up to ki of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return a boolean array answer where answer[i] is the result of the ith query queries[i].

Note that each letter is counted individually for replacement, so if, for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two of the letters. Also, note that no query modifies the initial string s.
'''


/*
    for every query, 
    if we have a map storing the counts of each letter, we can figure out whether 
    we can form a palindrom or not. 
    To a string to be a palindrome, there can be utmost one character with odd frequency
    rest all characters in the substring needs to have even count.
    Now, one operation can reduce the number of odd count characters in a substring by 2
*/
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        hash_map = {s[0]: 1}
        x = hash_map
        prefix = [hash_map]
        for i in range(1, len(s)):
            x = x.copy()
            x[s[i]] = x.get(s[i], 0) + 1
            prefix.append(x)
            
        result = []
        for query in queries:
            cnt = 0
            for key, value in prefix[query[1]].items():
                if query[0] > 0:
                    x = value - prefix[query[0]-1].get(key, 0)
                else:
                    x = value
                if x % 2:
                    cnt+=1
            if cnt - 2 * query[2] > 1:
                result.append(False)
            else:
                result.append(True)
        return result
