#Write a function that takes a string as input and reverse only the vowels of a string
#ugly solution, my own!
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aieuoAOIUE'
        res = list()
        for i in range(len(s)):
            if s[i] in vowels:
                res.append(i)
        res2 = sorted(res, reverse=True)
        e = list(zip(res,res2))
        s = list(s)
        print(e)
        for i in range(int(len(e)/2)):
            old = e[i][0]
            new = e[i][1]
            s[old], s[new] = s[new], s[old]
        s = ''.join(s)
        return s
