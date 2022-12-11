'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        out = []
        words.sort()
        len_w = len(words[0])
        combined_len =  len_w * len(words)
        for i in range(len(s)-combined_len+1):
            sample = s[i:i+combined_len]

            valid = True
            #print('sample:', sample)

            temp_word = []
            for j in range(len(words)):
              #  print(sample[j*len_w:j*len_w+len_w])
                temp_word.append(sample[j*len_w:j*len_w+len_w])
                # if sample[j*len_w:j*len_w+len_w] in words:
                #     j+= 1
                #     print(valid)
                # else:
                    
                #     valid = False
                #     print(valid)
                #     break

            # if valid:
            #     print('is valid')
            #     out.append(i)

            temp_word.sort()
            if (temp_word == words):
                out.append(i)

            

        # print(out)

        return out
        
--------------------------------------------------------------------------
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        n = len(words)
        p = len(words[0])
        i=0
        r=[]
        while  i + (n * p) <= len(s) :
            w = s[i :i+(n *p)]
            words2 = []
            for k in range(0 , n*p ,p):
                words2.append(w[k:k+p])
            words2.sort()
            if words == words2 :
                r.append(i)
            i+=1
        
        return r
----------------------------------------------------------------------------------------------


        
        
