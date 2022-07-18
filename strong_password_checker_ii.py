'''
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.
'''

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        p = password
        if len(p) < 8:
            return False
        low = 0
        for i in p:
            if i.islower():
                low +=1
        if low == 0:
            return False
        up = 0
        for i in p:
            if i.isupper():
                up+=1
        if up == 0:
            return False

        dig = 0
        for i in p:
            if i.isdigit():
                dig+=1
        if dig == 0:
            return False
        spec = 0
        for i in p:
            if i in "!@#$%^&*()-+":
                spec+=1
        if spec == 0:
            return False

        for i in range(len(p)-1):
            if p[i] == p[i+1]:
                return False
        return True
      
---------------------------------
class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        n = len(password)
        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        spcl_char= "!@#$%^&*()-+"
        for i in range(n):
            if password[i].islower():
                hasLower = True
            if password[i].isupper():
                hasUpper = True
            if password[i].isdigit():
                hasDigit = True
            if password[i] in spcl_char:
                specialChar = True
        for i in range(1,n):
            if(password[i-1]==password[i]):
                return False
            
        if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
            return True
        else:
            return False
