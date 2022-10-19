'''
Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.
'''


class Solution:
    def arrangeWords(self, text: str) -> str:
        
        # convert string to an array
        arr = text.split()
        
        # convert the first letter of the array to a lower case letter
        arr[0] = arr[0].lower()
        
        # sort array by length
        arr.sort(key=len)
        
        # convert the first letter of the array to an upper case letter
        arr[0] = arr[0].capitalize()
        
        # convert array to string
        return " ".join(arr)
      
---------------------------------------------------------------------

sort by length of each word
capitalize the first word and merge rest of words

class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        res = []
        for w in text.split():
            w = w.lower()            
            res.append(w)
        res = sorted(res, key=len)
        res = [res[0].capitalize()] + res[1:]
        return ' '.join(res)
