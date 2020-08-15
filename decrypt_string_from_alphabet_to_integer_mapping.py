'''
Given a string s formed by digits ('0' - '9') and '#' . We want to 
map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
'''


from string import ascii_lowercase as asc
class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s.split('#')
        res = list()
        actual_doubles = len(s)-1
        counter = 0
        res = []
        for item in s:
            if counter < actual_doubles:
                singles = item[:-2]
                singles = list(map(lambda s: int(s),singles))
                doubles = item[-2:]
                doubles = [int(doubles)]
                counter+=1

            else:
                singles = item
                singles = list(map(lambda s: int(s),singles))

                doubles = []

            for x in singles:
                x = int(x)
                res.append(asc[x-1])
            for x in doubles:
                x = int(x)
                res.append(asc[x-1])

        res = ''.join(res)
        return res
