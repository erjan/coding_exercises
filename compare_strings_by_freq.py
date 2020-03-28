#Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

#Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

#TLE SOLUTION


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def helper(self, s):
            
            min_s = min(s)
            return s.count(min_s)
            
        
        answer = []
        for query in queries:
            c = 0
            for w in words:
                if helper(self,query) < helper(self,w):
                    c+=1
        
            answer.append(c)
        print(answer)
        return answer
