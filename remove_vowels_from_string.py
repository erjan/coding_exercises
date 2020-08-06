'''
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
'''


def f(s):
    s = list(s)
    vowels = 'aeiou'
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = ''
    s = ''.join(s)
    print(s)
    return s
