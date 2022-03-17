'''
A string s is nice if, for every letter of the alphabet that s contains, it 
appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' 
and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there 
are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
'''

def check_substring(s):
    return len(set(s.lower())) == (len(set(s)) // 2)
  
def f(s):
    res = list()
    occurrence = float('-inf')
    max_len = float('-inf')
    nice = ''
    for i in range(len(s)):
        j = i+1
        for j in range(i+1, len(s)+1):

            substring = s[i:(j)]
            temp = check_substring(substring)
            if temp:
                if len(substring) > max_len and occurrence <= i:
                    max_len = len(substring)
                    nice = substring
                    occurrence = i

    if max_len != float('-inf'):
        return nice
    else:
        return ''
