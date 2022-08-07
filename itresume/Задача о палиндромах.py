'''
Необходимо написать функцию is_palindrome, которая принимает на вход строку s и проверяет - является ли эта строка палиндромом.
'''



def is_palindrome(s):
    s = s.lower()
    s = s.split(' ')
    s = ''.join(s)
    return s[::-1] == s
