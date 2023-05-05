'''
You are given a string s, a string chars of distinct characters and an integer array vals of the same length as chars.

The cost of the substring is the sum of the values of each character in the substring. The cost of an empty string is considered 0.

The value of the character is defined in the following way:

If the character is not in the string chars, then its value is its corresponding position (1-indexed) in the alphabet.
For example, the value of 'a' is 1, the value of 'b' is 2, and so on. The value of 'z' is 26.
Otherwise, assuming i is the index where the character occurs in the string chars, then its value is vals[i].
Return the maximum cost among all substrings of the string s.
'''



class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        cost1 = dict(zip(chars, vals))

        ind = [i for i in range(1, 27)]
        val = string.ascii_lowercase

        cost = dict(zip(val, ind))

        for k, v in cost1.items():
            if k in cost:
                cost[k] = v

        max_cost = 0
        cur_cost = 0
        for i in range(len(s)):

            cur_cost += cost[s[i]]

            if cur_cost < 0:
                cur_cost = 0
            max_cost = max(cur_cost, max_cost)
        print(max_cost)
        return max_cost
