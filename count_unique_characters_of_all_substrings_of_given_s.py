'''
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
'''

from collections import defaultdict
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        The key ideas behind the solution:
        1. The maximum possible substrings that can end at an index are i + 1.
        2. The contribution of a character to this substring is (i + 1) - it's last seen position.
        3. At each point, sum of all contributions, gives the number of total substrings found so far.
        4. The last seen position of char is actually i + 1.
        """
        last_position = defaultdict(int) # Used for storing the last position of each character
        contribution = defaultdict(int) # Used for storing the contribution of each character so far. This
        # will possibly be updated throughout the string traversal
        res = 0
        
        for i, char in enumerate(s):
            max_possible_substrs_at_idx = i + 1
            contribution[char] = max_possible_substrs_at_idx - last_position[char]
            
            res+=sum(contribution.values())
            last_position[char] = i + 1
            
        return res
