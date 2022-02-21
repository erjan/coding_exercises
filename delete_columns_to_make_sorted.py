'''
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
'''

#my own solution

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        nums = strs
        s = list(zip(*nums))
        print(s)
        for i in range(len(s)):
            temp = s[i]
            temp = ''.join(temp)
            temp2 = ''.join(sorted(temp))

            print(temp, temp2)
            if temp2 != temp:
                count += 1
        print(count)
        return count
