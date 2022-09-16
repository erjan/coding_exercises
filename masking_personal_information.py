'''
You are given a personal information string s, representing either an email address or a phone number. Return the masked personal information using the below rules.

Email address:

An email address is:

A name consisting of uppercase and lowercase English letters, followed by
The '@' symbol, followed by
The domain consisting of uppercase and lowercase English letters with a dot '.' somewhere in the middle (not the first or last character).
To mask an email:

The uppercase letters in the name and domain must be converted to lowercase letters.
The middle letters of the name (i.e., all but the first and last letters) must be replaced by 5 asterisks "*****".
Phone number:

A phone number is formatted as follows:

The phone number contains 10-13 digits.
The last 10 digits make up the local number.
The remaining 0-3 digits, in the beginning, make up the country code.
Separation characters from the set {'+', '-', '(', ')', ' '} separate the above digits in some way.
To mask a phone number:

Remove all separation characters.
The masked phone number should have the form:
"***-***-XXXX" if the country code has 0 digits.
"+*-***-***-XXXX" if the country code has 1 digit.
"+**-***-***-XXXX" if the country code has 2 digits.
"+***-***-***-XXXX" if the country code has 3 digits.
"XXXX" is the last 4 digits of the local number.
'''

class Solution(object):
    def maskPII(self, s):
        phone = "***-***-"
        mail = ""
        num_counter = 0
        if '@' not in s:
            last_digit = ""
            counter = -1
            while len(last_digit) < 4:
                if s[counter].isnumeric():
                    last_digit += s[counter]
                counter -= 1
            for a in range(len(s)):
                if s[a].isnumeric():
                    num_counter += 1
            if num_counter==10:
                return phone+last_digit[::-1]
            elif num_counter==11:
                return '+*-'+phone+last_digit[::-1]
            elif num_counter==12:
                return '+**-'+phone+last_digit[::-1]
            elif num_counter==13:
                return '+***-'+phone+last_digit[::-1]        
        else:
            control= '1'
            step = 0
            while(control != '@'):
                control = s[step]
                step += 1
            mail += s[0]
            mail += "*****"
            mail += s[step-2:len(s)]
            return mail.lower()
          
----------------------------------------------------------
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            user,domain=s.split('@')
            return f'{user[0].lower()}{"*"*5}{user[-1].lower()}@{domain.lower()}'
        s=''.join([x for x in s if x.isdigit()])  ; n=0
        return f'+{"*"*(n-10)}-***-***-{s[-4:]}' if n>10 else f'***-***-{s[-4:]}'
