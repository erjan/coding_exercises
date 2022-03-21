'''
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 '''

class Solution:
    def makeGood(self, s: str) -> str:
        def check(c1, c2):
            if c1.islower() and c2.isupper() and c1.upper() == c2:
                return True

            elif c1.isupper() and c2.islower() and c1.lower() == c2:
                return True
    
        res = []
        s = list(s)

        for i in range(len(s)):
            if len(res) > 0 and check(res[-1], s[i]):
                print('bad combo')
                res.pop()
            else:
                res.append(s[i])

        res = ''.join(res)
        print(res)
        return res
