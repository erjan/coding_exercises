'''
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
'''


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pref = [0]*(n+1)
        vowel = 'aeiou'
        ans = []

        for i in range(n):
            pref[i+1] = pref[i] + \
                (1 if words[i][0] in vowel and words[i][-1] in vowel else 0)
        print(pref)

        for l, r in queries:
            ans.append(pref[r+1] - pref[l])
        print(ans)
        return ans

    
-------------------------------------------------------------------------------------------------------
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
                                                                # Example:
                                                                #    words = ['aba','bcb','ece','aa','e'] 
                                                                #  queries = [[0,2], [1,4], [1,1]]

        vowels = lambda w: w[0] in 'aeiou' and w[-1] in 'aeiou' #  <-- boolean function  

        words = map(vowels, words)                              #    words = [True, False, True, True, True]
        
        pref = list(accumulate(words, initial = 0))             #     pref = [0, 1, 1, 2, 3, 4]
        
        return [pref[r+1] - pref[l] for l,r in queries]         #   return [2-0, 4-1, 1-1] = [2,3,0]
