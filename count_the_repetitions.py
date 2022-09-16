'''
We define str = [s, n] as the string str which consists of the string s concatenated n times.

For example, str == ["abc", 3] =="abcabcabc".
We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.

For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing the bolded underlined characters.
You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings str1 = [s1, n1] and str2 = [s2, n2].

Return the maximum integer m such that str = [str2, m] can be obtained from str1.
'''

This is a difficult problem (for me anyway). I kept thinking that there had to be a trick

Firstly, if there is any character in s2 that is not in s1 then we can never obtain [S2, M] from S1.

Then I step through s1, incrementing an index pointer in s2 whenever characters match :

When I reach the end of s2, go back to the start and increment the counter s2_reps that tells me how many complete copies of s2 I have used.
Similarly when I reach the end of s1, go back to the start and increment s1_reps.
At then end of s1 record in a dictionary a mapping from the next index to be matched in s2 as key and the pair of (s1_reps, s2_reps) as value.
If the key has been seen before then we are in a loop, every time we go through s1 we are at the same position in s2. So we can break from stepping through the strings and work out how many loops we can go through for all of [s1, n1].
(Potentially we never find a loop and have reached n1 repetitions of s1 already so can just return s2_reps // n2)

Having found how many repetitions of s1 and s2 there are in a loop, we use as many loops as possible to go through n1 copies of s1. Bear in mind that there may be some repetitions before the loop is entered.
Then all that remains is if we have not seen n1 copies of s1 after the final loop, step through the strings again until we reach n1.

I suspect the code below could be made a little more efficient. Comments welcome!

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):

        if any(c for c in set(s2) if c not in set(s1)):   # early return if impossible
            return 0

        s2_index_to_reps = {0 : (0, 0)}   # mapping from index in s2 to numbers of repetitions of s1 and s2
        i, j = 0, 0
        s1_reps, s2_reps = 0, 0

        while s1_reps < n1:

            if s1[i] == s2[j]:
                j += 1     # move s2 pointer if chars match
            i += 1

            if j == len(s2):
                j = 0
                s2_reps += 1

            if i == len(s1):
                i = 0
                s1_reps += 1
                if j in s2_index_to_reps:   # loop found, same index in s2 as seen before
                    break
                s2_index_to_reps[j] = (s1_reps, s2_reps)

        if s1_reps == n1:    # already used n1 copies of s1
            return s2_reps // n2

        initial_s1_reps, initial_s2_reps = s2_index_to_reps[j]    # repetitions before loop starts
        loop_s1_reps = s1_reps - initial_s1_reps
        loop_s2_reps = s2_reps - initial_s2_reps
        loops = (n1 - initial_s1_reps) // loop_s1_reps

        s2_reps = initial_s2_reps + loops * loop_s2_reps
        s1_reps = initial_s1_reps + loops * loop_s1_reps

        while s1_reps < n1:   # if loop does not end with n1 copies of s1, keep going

            if s1[i] == s2[j]:
                j += 1
            i += 1

            if i == len(s1):
                i = 0
                s1_reps += 1

            if j == len(s2):
                j = 0
                s2_reps += 1

        return s2_reps // n2
      
----------------------------------------------------------------------
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp = []
        for i in range(len(s2)):
            start = i
            cnt = 0
            for j in range(len(s1)):
                if s1[j] == s2[start]:
                    start += 1
                    if start == len(s2):
                        start = 0
                        cnt += 1
            dp.append((start,cnt))
        res = 0
        next = 0
        for _ in range(n1):
            res += dp[next][1]
            next = dp[next][0]
        return res // n2
