'''
A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

Return true if so, or false otherwise.
'''

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        l = list()

        for i in range(len(s)):

            if s[i].isdigit():
                l.append(int(s[i]))

        for i in range(len(l)-1):

            if l[i] >= l[i+1]:
                return False
        return True
      
#much better solution

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1

        for w in s.split():
            if w.isdigit():
                if int(w) <= prev:
                    return False
                prev = int(w)
        return True
