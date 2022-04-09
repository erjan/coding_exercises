'''
Given an array of keywords words and a string s, make all appearances of all keywords words[i] in s bold. Any letters between <b> and </b> tags become bold.

Return s after adding the bold tags. The returned string should use the least number of tags possible, and the tags should form a valid combination.

 
 '''

class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        bold = [0] * len(S)
        
        for word in words:
            start = 0
            while start < len(S):
                idx = S.find(word, start)
                if idx >= 0 :
                    bold[idx:idx+len(word)] = [1] * len(word)
                    start = idx + 1
                else:
                    break
                    
        result = []
        for i, c in enumerate(S):
            if bold[i] and (i == 0 or not bold[i - 1]):
                result.append('<b>')
            result.append(c)
            if bold[i] and (i == len(S) - 1 or not bold[i + 1]):
                result.append('</b>')            
                
        return "".join(result)
