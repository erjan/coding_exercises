'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
'''


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        total=0
        if x>y:
            first_priority_string='ab'
            second_priority_string='ba'
            first_priority_value=x
            second_priority_value=y
        else:
            first_priority_string='ba'
            second_priority_string='ab'
            first_priority_value=y
            second_priority_value=x

        temp=""
        for i in s:
            temp+=i
            if temp[-2:]==first_priority_string:
                temp=temp[:-2]
                total+=first_priority_value
        s=temp
        temp=""
        for i in s:
            temp+=i
            if temp[-2:]==second_priority_string:
                temp=temp[:-2]
                total+=second_priority_value
        return total
