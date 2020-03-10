#leetcode easy problem - I spent 3h doing it and made a mistake of not refreshing the original chars list
#Description:

#You are given an array of strings words and a string chars.
#A string is good if it can be formed by characters from chars (each character can only be used once).
#Return the sum of lengths of all good strings in words.


class Solution(object):
    def countCharacters(self, words, chars):
        total_count = 0
        original_c = chars
        for word in words:
        #print('-------------------------------------------------')
        #print('current word : ' + word)
            word = list(word)
            chars = list(original_c)
            bad_found = False
            for w in word:

                #print( *chars)            
                if w in chars:
                    chars.remove(w)
                    #print('removed w from chars : ' + ''.join(chars))
                else:
                    #print('this character %s is not in word %s' %(w, chars))
                    bad_found = True
                    break
            if not bad_found:
                #print('good word!')
                total_count += len(word)
            #else:
                #print('bad word!')
        #print('total count %d ' % total_count)
        return total_count
