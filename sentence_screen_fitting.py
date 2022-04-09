'''

Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

'''


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
            
        curr_row = 0
        curr_idx = 0
        total_sentences_ct = 0
        memo = {} # {word_idx: [completed_sentences_ct, next_start_word_idx]}
        
        while curr_row < rows:
            start_word_idx = curr_idx 
            if start_word_idx in memo:
                completed_sentences_ct, curr_idx = memo[start_word_idx]
                total_sentences_ct += completed_sentences_ct
            else:
                complete_sentences_ct = 0
                curr_col = 0

                while curr_col < cols:
                    curr_word_len = len(sentence[curr_idx])
                    if cols < curr_word_len:
                        return 0
                    if cols - curr_col < curr_word_len:
                        break
                    curr_col += (curr_word_len + 1)
                    if curr_idx == len(sentence) - 1:
                        complete_sentences_ct += 1
                    curr_idx = (curr_idx + 1) % len(sentence)
                memo[start_word_idx] = [complete_sentences_ct, curr_idx]
                total_sentences_ct += complete_sentences_ct
            curr_row += 1
        return total_sentences_ct

    
--------------------------------------

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        str=" ".join(sentence)+" "
        valid_space=0
        for i in range(rows):
            valid_space+=cols
            if str[valid_space%len(str)]==" ":
                valid_space+=1
            else:
                while valid_space>0 and str[valid_space%len(str)-1]!=" ":
                    valid_space-=1
        return valid_space//len(str)
