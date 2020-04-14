'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
'''




class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s)== 0:
            return ''
        s = list(s)
        for q in shift:
            direction = q[0]
            amount = q[1]
            if direction == 0:
                c = 0
                while c < amount:

                    first = s[0]
                    s.pop(0)
                    s.append(first)
                    c+=1
            else:
                c = 0
                while c < amount:
                    last = s[-1]
                    s.pop()
                    s.insert(0, last)
                    c+=1
        s = ''.join(s)    
        print(s)
        return s
