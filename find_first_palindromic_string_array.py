'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check_palindrome(s):
            if len(s) % 2 == 0:
                mid = len(s)//2
                first = s[:mid]
                second = s[mid:]
                second = second[::-1]
                return first == second
            else:
                mid = len(s)//2
                first = s[:mid]
                second = s[(mid+1):]
                second = second[::-1]       
                return first == second

        for word in words:
            if check_palindrome(word):
                return word
        return ''
