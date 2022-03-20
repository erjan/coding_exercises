'''
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.
'''

class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        def check_mark(word):

            if len(word) == 1 and word[0] in ['!', '.', ',']:
                return True
            for i in range(len(word)-1):
                if word[i] in ['!', '.', ',']:
                    return False
            return True


        def check_hyphen(word):
            if '-' in word:

                if word.count('-') > 1:
                    return False
                i = word.index('-')
                if i == 0 or i == len(word)-1:
                    return False

                if word[i-1] not in string.ascii_lowercase or word[i+1] not in string.ascii_lowercase:
                    return False
                return True
            else:
                return True


        def check_digits(word):
            for w in word:
                if w.isdigit():
                    return False
            return True

        s = sentence
        s = s.split()

        valid = 0
        for i in range(len(s)):
            word = s[i]

            a1 = check_hyphen(word)
            a2 = check_digits(word)
            a3 = check_mark(word)

            if a1 and a2 and a3:
                valid += 1
        print(valid)
        return valid
