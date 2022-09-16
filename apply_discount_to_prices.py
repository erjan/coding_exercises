'''
A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.

For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence.

Note that all prices will contain at most 10 digits.
'''

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split() # convert to List to easily update
        m = discount / 100 
        for i,word in enumerate(s):
            if word[0] == "$" and word[1:].isdigit(): # Check whether it is in correct format
                num = int(word[1:]) * (1-m) # discounted price
                w = "$" + "{:.2f}".format(num) #correctly format
                s[i] = w #Change inside the list
        
        return " ".join(s) #Combine the updated list
      
--------------------------------

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sp  = sentence.split()
        for i, word in enumerate(sp):
            if word[0] == '$' and str.isdigit(word[1:]):
                amount = (100 - discount) * int(word[1:])/ 100
                sp[i] = f'${amount:.2f}'
        return ' '.join(sp)
