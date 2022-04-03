'''


Given a string s of words delimited by spaces, reverse the order of words.

'''


class Solution:
    def solve(self, sentence):

        s = sentence.split()

        s = s[::-1]

        s = " ".join(s)
        return s
        
