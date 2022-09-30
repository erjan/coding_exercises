'''
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
'''

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ifTrueIsAnswer = self.confuseStudents(answerKey, k, "T")
        ifFalseIsAnswer = self.confuseStudents(answerKey, k, "F")
        return max(ifTrueIsAnswer, ifFalseIsAnswer)
    
    def confuseStudents(self, array, k, key):
        left, result = 0, 0
        for right in range(len(array)):
            if array[right] == key:
                k -= 1
            if k < 0:
                result = max(result, right-left)
                while k < 0:
                    if array[left] == key:
                        k += 1
                    left += 1
        return max(result, right+1-left)
      
------------------------------------------------------------------------------------------------

One left and one right pointer to determine a window, calculate the amount of T and F in that window, when one of them is less than k, we can change all those letters to another, so that all the letters in the window are the same, then the window size is an alternative answer. Traverse the entire string to get maximum value.

Slide the right pointer to calculate the number of T and F in the window
If the number of T and F are both greater than k, that is, all letters in the window cannot be changed to be the same by modifying one letter, and the left pointer needs to be moved
After the left pointer is moved, the window size can be used as the answer, compared with the current maximum value and updated
Runtime: 332 ms, faster than 82.95% of Python3 online submissions for Maximize the Confusion of an Exam.
Memory Usage: 14.4 MB, less than 83.16% of Python3 online submissions for Maximize the Confusion of an Exam.

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = ret = numT = numF = 0
        
        for right in range(n):
            if answerKey[right]=='T':
                numT+=1
            else:
                numF+=1
            while numT>k and numF>k:
                if answerKey[left]=='T':
                    numT-=1
                else:
                    numF-=1
                left+=1
            ret = max(ret, right-left+1)
        return ret
