'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        news = ''.join(list(filter(lambda x: x.isalpha(), s))[::-1])

        bad_index = list()

        for i in range(len(s)):
            if s[i].isalpha() == False:
                bad_index.append(i)
        c = 0
        res = ''
        for i in range(len(s)):
            if i not in bad_index:
                res += news[c]
                c += 1
            else:
                res += s[i]
        print('result')
        print(res)
        return res

    
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        size = len(s)
        
        # convert into array of characters
        array = [*s]
        
        # two pointers, initialized with boundary index
        left, right = 0, size-1
        
        #  swap english letter with two-pointers
        while left < right:
            
            # keep moving until we meet english letter on left hand side
            if not array[left].isalpha():
                left += 1
                continue
            
            # keep moving until we meet english letter on right hand side
            if not array[right].isalpha():
                right -= 1
                continue
            
            # swap english letters
            array[left], array[right] = array[right], array[left]
            
            # update index of two pointer
            left, right = left+1, right-1
        
        
        # convert to string and output
        return "".join(array)    
