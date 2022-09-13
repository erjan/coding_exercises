'''
You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string, and it must be from words. Master.guess(word) returns:

-1 if word is not from words, or
an integer representing the number of exact matches (value and position) of your guess to the secret word.
There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get:

"Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or
"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses.
The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).
'''

class Solution:
   def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
       while wordlist:
           word = wordlist.pop()
           matches = master.guess(word)
           # only those words that share exactly x characters with word can be
           # the solution.
           wordlist = [
               other
               for other in wordlist
               if matches == sum(w == o for w, o in zip(word, other))
           ]
------------------------------------------------------------------------------------
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        dic = wordlist
        for _ in range(10):
            word = random.choice(dic)
            matches = master.guess(word)
            if matches == 6: break  
            dic = [w for w in dic \
                    if w != word and self.guess(word, w) == matches]
      
    def guess(self, w1, w2):
        return sum(1 for c1, c2 in zip(w1,w2) if c1==c2)
