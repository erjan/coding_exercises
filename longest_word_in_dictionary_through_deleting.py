'''
Given a string s and a string array dictionary, return the 
longest string in the dictionary that can be formed by deleting some of the given 
string characters. If there is more than one possible result, return the longest word with the smallest 
lexicographical order. If there is no possible result, return the empty string.
'''



class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        #Sort the dictionary by length and then lexographical order
        dictionary.sort(key= lambda x: (-len(x),x))

        for d in dictionary:   
            count = 0
            i = j = 0
            while j < len(d) and i < len(s):
				#Start counting whenever a character matches 
                if s[i] == d[j]:
                    j += 1
                    count += 1
                i += 1
			#return as soon as you find all the characters from dictionary word in s
            if count == len(d):
                return d
            
        return ''
      
----------------------------------------------------------------------------------      

#AA#> Two level Sort of words: 1st length, 2nd lexiographic order 
dictionary.sort(key = lambda x: (-len(x),x))
for word in dictionary:
	j = 0 #AA#> word pointer
	for i in range(len(s)): #AA#> string pointer
		if s[i] == word[j]: j+=1

		if j == len(word): return word

return ''
