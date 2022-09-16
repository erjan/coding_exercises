'''
Convert a non-negative integer num to its English words representation.
'''


class Solution:        
    def numberToWords(self, num: int) -> str:
        if num == 0 : return 'Zero' #if condition to handle zero
        d = {1000000000 : 'Billion',1000000 : 'Million',1000 : 'Thousand',100 : 'Hundred', 
		90:'Ninety',80:'Eighty',70:'Seventy',60:'Sixty',50: 'Fifty', 40 : 'Forty', 30 : 'Thirty', 20 : 'Twenty',
		19 :'Nineteen',18 :'Eighteen',17:'Seventeen',16:'Sixteen',15:'Fifteen',14:'Fourteen',13:'Thirteen',12:'Twelve',11:'Eleven',
		10:'Ten',9:'Nine',8:'Eight',7:'Seven',6:'Six',5:'Five',4:'Four',3:'Three',2:'Two',1:'One'} #initiating a dictionary to handle number to word mapping
        ans = ""                      #initialising the returnable answer variable
        for key, value in d.items():  #for loop to iterate through each key-value pair in dictionary 
            if num//key>0 :           #checking if number is in the range of current key
                x = num//key          #finding the multiple of key in num
                if key >= 100 :       #logic to add the multiple number x above as word to our answer, We say "One Hundred", "One thoushand" but we don't say "One Fifty", we simply say "Fifty"
                    ans += self.numberToWords(x) + ' '
                ans  += value + " "
                num = num%key         #preparing the number for next loop i.e removing the value from num which we have already appended the words to answer.
        return ans.strip()            #returning answer removing the last blank space
