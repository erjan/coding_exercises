'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
#my own solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = strs
        if len(words) == 1:
            return words[0]
        
        mini = min(words, key=len)
        words.remove(mini)
        good_prefix = ''
        for i in range(1, len(mini)+1):
            prefix_to_check = mini[:i]
            temp = list()
            curr_prefix = ''
            for word in words:
                word_prefix = word[:i]

                print(word_prefix)
                if word_prefix != prefix_to_check:
                    break
                else:
                    temp.append(word_prefix)
                    curr_prefix = word_prefix
            print('list temporary')
            print('length of temp', len(temp), '\t', *temp)

            print()
            if len(temp) == len(words):
                good_prefix = curr_prefix

        print('actual prefix', good_prefix)
        return good_prefix


            
