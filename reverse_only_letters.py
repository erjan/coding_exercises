'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        news = ''.join(list(filter(lambda x: x.isalpha(), s))[::-1])

        bad_index = list()

        for i in range(len(s)):
            if s[i].isalpha() == False:
                bad_index.append(i)
        c = 0
        res = ''
        for i in range(len(s)):
            if i not in bad_index:
                res += news[c]
                c += 1
            else:
                res += s[i]
        print('result')
        print(res)
        return res
