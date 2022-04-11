'''

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

'''


class Solution:
    def fractionToDecimal(self, numerator, denominator):

        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        integer = sign + str(n)
        if remainder == 0: return integer
        
        rs = {}       
        decimal = ''
        i = 0
        while remainder > 0 and remainder not in rs:
            rs[remainder] = i
            n, remainder = divmod(remainder*10, abs(denominator))
            decimal += str(n)
            i +=  1
        
        if remainder in rs:
            i = rs[remainder]
            return integer + '.' + decimal[:i] + '(' + decimal[i:] + ')'
        else:
            return integer + '.' + decimal[:]
          
---------------------
class Solution:
# @return a string
def fractionToDecimal(self, numerator, denominator):
    res=""
    if numerator/denominator<0:
        res+="-"
    if numerator%denominator==0:
        return str(numerator/denominator)
    numerator=abs(numerator)
    denominator=abs(denominator)
    res+=str(numerator/denominator)
    res+="."
    numerator%=denominator
    i=len(res)
    table={}
    while numerator!=0:
        if numerator not in table.keys():
            table[numerator]=i
        else:
            i=table[numerator]
            res=res[:i]+"("+res[i:]+")"
            return res
        numerator=numerator*10
        res+=str(numerator/denominator)
        numerator%=denominator
        i+=1
    return res
  Idea is to put every remainder into the hash table as a key, and the current length of the result string as the value. When 
  the same remainder shows again, it's circulating from the index of the value in the table.
  
  
  ----------------------------
  
  def fractionToDecimal(self, numerator, denominator):
    sign = '-' if numerator * denominator < 0 else ''
    head, remainder = divmod(abs(numerator), abs(denominator))
    tail, seen = '', {}
    while remainder != 0:
        if remainder in seen:
            tail = tail[: seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
            break
        seen[remainder] = len(tail)
        digit, remainder = divmod( remainder*10, abs(denominator) )
        tail+=str(digit)
    return sign + str(head) + (tail and '.' + tail)
