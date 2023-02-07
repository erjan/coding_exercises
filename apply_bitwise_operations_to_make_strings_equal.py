'''
You are given two 0-indexed binary strings s and target of the same length n. You can do the following operation on s any number of times:

Choose two different indices i and j where 0 <= i, j < n.
Simultaneously, replace s[i] with (s[i] OR s[j]) and s[j] with (s[i] XOR s[j]).
For example, if s = "0110", you can choose i = 0 and j = 2, then simultaneously replace s[0] with (s[0] OR s[2] = 0 OR 1 = 1), and s[2] with (s[0] XOR s[2] = 0 XOR 1 = 1), so we will have s = "1110".

Return true if you can make the string s equal to target, or false otherwise.
'''

'''
If a string contains no 1, then there is no way to change
it any longer; If a string contains at least a 1, there is no way to change it 
to an all-zero string, under the rules of the problem.
'''
def makeStringsEqual(self, s: str, target: str) -> bool:
        if ('1' not in s) or ('1' not in target):
            return s == target
        return True
