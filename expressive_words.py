'''
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.
'''

To make the code more readable, a possible way is to define helper functions.

compress(word)
A word can be compressed to be a letter sequence and a corresponding counts.
For example, 'abbaaa' will be compressed to be ['a', 'b', 'a'] and [1, 2, 3].
A helper function compress(word) is defined to do it.

is_strechy(word)
Before checking if a word is strechy, we compress both the word and S.
The word will be compressed to be w_letters and w_counts, and S will be S_letters and S_counts.
check letters sequence
It is obvious that if w_letters and S_letters are not identical, the word is not stretchy.
check counts sequence
For a index i,

S_counts[i] < 3 means the letter is not expended, so the count of this letter should be identical in S and in the word. In other word, if w_letters[i] != S_letters[i], the word is not strechy.
S_counts[i] >= 3 means either (i) the letter is expended to be larger than 3, or (ii) not streched with an original count larger than 3. Whicever case it is, if S_counts[i] < w_counts[i], the word is not stretchy.
If none of above happens, the word is stretchy.

Python

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:

        # compress a word into a letter sequence and corresponding counts
        def compress(word):
            letters = []
            counts = []
            for l in word:
                if not letters or l != letters[-1]:
                    letters.append(l)
                    counts.append(1)
                else:
                    counts[-1] += 1
                    
            return letters, counts
        
        # check if a word is stretchy by comparing to compressed S
        def is_stretchy(w):
            
            # S_letters, S_counts are the output of compress(S)
            nonlocal S_letters, S_counts
            
            w_letters, w_counts = compress(w)
            
            if w_letters != S_letters:
                return False
            
            for i in range(len(S_counts)):
                if S_counts[i] < 3 and S_counts[i] != w_counts[i]:
                    return False
                if S_counts[i] >= 3 and S_counts[i] < w_counts[i]:
                    return False
                    
            return True

        # main body
        S_letters, S_counts = compress(S)
        res = 0
        for w in words:
            if is_stretchy(w):
                res += 1
        
        return res
      
------------------------------------------------------------------------------
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        res = 0
        s_chars, s_counts = self.process(s)
        for word in words:
            w_chars, w_counts = self.process(word)
            
            if s_chars != w_chars:
                break

            can_match = True
            for k in range(len(w_chars)):
                if not (w_counts[k] == s_counts[k] or (w_counts[k] < s_counts[k] and s_counts[k] >= 3)):
                    can_match = False
                    break
            if can_match:
                res += 1

        return res
    
    def process(self, strs):
        if not strs:
            return [], []
        chars, counts = [strs[0]], [1]

        for i in range(1, len(strs)):
            if strs[i] == chars[-1]:
                counts[-1] += 1
            else:
                chars.append(strs[i])
                counts.append(1)
        return chars, counts
