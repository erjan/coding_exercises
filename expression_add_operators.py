'''
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.
'''

class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        res = []

        def dfs(num: str, path: str, curr_val: int, last_val: int):
            if not num:
                if curr_val == target:
                    res.append(path)
                return
            for i in range(1, len(num) + 1):
                val_i = num[:i]
                if i == 1 or (i > 1 and num[0] != '0'):
                    dfs(num[i:], path + '+' + val_i, curr_val + int(val_i), int(val_i))    # Note: Use int() to replace eval(). It can greatly reduce the calculation time.
                    dfs(num[i:], path + '-' + val_i, curr_val - int(val_i), -int(val_i))
                    dfs(num[i:], path + '*' + val_i, curr_val + last_val * int(val_i) - last_val, last_val * int(val_i))

        # find the result
        for i in range(1, len(num) + 1):
            val_i = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                dfs(num[i:], val_i, int(val_i), int(val_i))
        return res
