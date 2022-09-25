'''
Given a string s, return the lexicographically smallest
subsequence of s that contains all the distinct characters of s exactly once.
'''


class Solution:
    def smallestSubsequence(self, s: str) -> str:
            stack = []
            seen = set()
            last_occurance = {}
            for i in range(len(s)):
                last_occurance[ s[i] ] = i

            # print(last_occurance)

            for i, ch in enumerate(s):
                if( ch in seen ):
                    continue
                else:
                    # 3
                    while( stack and stack[-1] > ch and last_occurance[stack[-1]] > i ):
                        removed_char = stack.pop()
                        seen.remove(removed_char)
                    seen.add(ch)
                    stack.append(ch)
                # print(stack)
            return ''.join(stack)
