'''
You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.
'''

import string
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        w = widths    
        abc = string.ascii_lowercase
    
        res = dict(zip(abc, w))

        print(res)

        num_lines = 1
        ans = 0
        for i in s:
            print()
            print('current char ', i, ' current ans: ', ans)
            ans += res[i]
            if ans > 100:
                print('over 100 spill')
                num_lines += 1
                ans = res[i]

        print(num_lines, ans)
        return num_lines, ans
