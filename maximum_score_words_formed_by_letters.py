'''
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
'''

from collections import Counter
class Solution:
    def maxScoreWords(self, words, letters, score):
        def letterScore(c):
            return score[ord(c)-ord("a")]
        def helper(i,remaining,scoreSofar):
            if not remaining or i == len(words):
                return scoreSofar
            res = helper(i+1 , remaining,scoreSofar)
            cw = Counter(words[i])
            if not (cw - remaining):
                res = max(res,helper(i+1,remaining - cw,scoreSofar + sum(map(letterScore,words[i]))))
            return res
        return helper(0,Counter(letters),0)
      
----------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def maxScoreWords(self, words, letters, score):     
		#Used to store the frequency of characters
        c=Counter(letters)
        
		#used to check wheather the character given to us are enough  to form the group of words
        def check(w):
            a=Counter(''.join(w))                        
            for x in a:
                if c[x]<a[x]:
                    return False
            return True                    
        
        def A(ind,s,p):
            #if we reach towards the end of list then we need to return no more to check 
            if ind==len(words):
				#we check here wheather the words   we formed are sufficient 
                if check(p):return s
				#we return -float('inf')  if not satisfied
                else:return -float('inf')
            
            ans=0
			#find the score of the word
            for x in words[ind]:
                ans+=score[ord(x)-97]
                
            # don't consider the word
            a=A(ind+1,s,p)
			#consider the word 
            b=A(ind+1,s+ans,p+[words[ind]])            
            #return max of both 
            return max(a,b)
        
        return A(0,0,[])
