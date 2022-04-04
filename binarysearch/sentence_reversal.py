'''

Given a list of strings sentence where each sentence[i] is a string with single character, reverse the order of the words in the sentence.

You may assume there's no extraneous spaces in the sentence. Can you do modify sentence in-place and solve in \mathcal{O}(1)O(1) space?

'''


class Solution:
    def solve(self, sentence):
        s = sentence
        s = "".join(s)
        s = s.split()
        s = s[::-1]
        s = " ".join(s)
        s = list(s)
        print(s)
        return s
      
#another solution


class Solution:
    def solve(self, sentence):
        size = len(sentence)
        i, word_start, word_end = 0, 0, 0
        while i <= size:
            if i == size or sentence[i] == " ":
                word_end = i - 1
                self.reverse(sentence, word_start, word_end)
                word_start = i + 1
            i += 1
        return self.reverse(sentence, 0, size - 1)

    def reverse(self, sentence, start, end):
        size = end - start + 1
        mid = start + (size // 2)
        i = start
        while i < mid:
            sentence[i], sentence[end - (i - start)] = sentence[end - (i - start)], sentence[i]
            i += 1

        return sentence

#another 

class Solution:
    def solve(self, s):
        return list(" ".join("".join(s).split(" ")[::-1]))
