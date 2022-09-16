'''
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
'''

class Solution(object):
    # DFS: iterative implement.
    def isAdditiveNumber(self, num):
        length = len(num)
        for i in range(1, length/2+1):
            for j in range(1, (length-i)/2 + 1):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if ((len(first) > 1 and first[0] == "0") or
                        (len(second) > 1 and second[0] == "0")):
                    continue

                while others:
                    sum_str = str(int(first) + int(second))
                    if sum_str == others:
                        return True
                    elif others.startswith(sum_str):
                        first, second, others = (
                            second, sum_str, others[len(sum_str):])
                    else:
                        break

        return False
