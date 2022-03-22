'''
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

'''

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        s = text.split()
        res = list()

        for i in range(len(s)-2):
            if s[i] == first and s[i+1] == second:
                res.append(s[i+2])

        print(res)
        return res
