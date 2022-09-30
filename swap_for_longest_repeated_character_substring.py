'''
You are given a string text. You can swap two of the characters in the text.

Return the length of the longest substring with repeated characters.
'''

# Approach 1: 
# Identify the count for repeat characters
    # Let's say the example is aabaaba.
    # We should get some thing [[a , 2], [b, 1], [a, 2], [b,1], [a,1]]

# Get the total count of one character.
    # take the same case for example, aabaaba, a total count = {a: 5, b: 2}
    # This will be used later.

# The answer contains two scenarios.
# scenario 1: aaabba, find another a to replace b to increase maxlen+1; so result would be aaaabb.
# scenario 2: aabaaba, firstly find the middle char b, length equals to 1, then make sure the left side and right side character are the same, then find if there is another a to replace b, update maxLen accordingly.

# Space complexity: O(n)
# Time complexity:  O(n)

import itertools
import collections
def maxRepOpt1(S):
    """
    :type text: str
    :rtype: int
    """
    # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
    A = [[c, len(list(g))] for c, g in itertools.groupby(S)]

    # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
    count = collections.Counter(S)

    # scenario 1:
    # only extend 1 more, use min here to avoid the case that there's no extra char to extend
    res = max(min(k + 1, count[c]) for c, k in A)

    # scenario 2
    for i in range(1, len(A) - 1):
        # if both sides have the same char and are separated by only 1 char
        if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
            # min here serves the same purpose
            res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i - 1][0]]))
    return res
