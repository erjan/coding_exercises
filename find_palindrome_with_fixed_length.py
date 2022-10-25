'''
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.


Intuition
The first half part of palindrome is ordered.
Not leading zeros allowd, so ther starts with 100000, 100001, 100002..
Every number is added a base in pow of 10.


Explanation
Find the base that we need to add to every element.
The pow equals to the half of the length l.

For each query index q,
we firstly turn it q - 1, whichis 0-based index,
then add it with the base.

Finally we make it palindrome by add its reversed string.
'''

  def kthPalindrome(self, queries, l):
        base = 10 ** ((l - 1) / 2)
        res = [q - 1 + base for q in queries]
        for i,a in enumerate(res):
            a = str(a) + str(a)[-1 - l % 2::-1]
            res[i] = int(a) if len(a) == l else -1
        return res

