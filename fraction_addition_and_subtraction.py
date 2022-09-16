'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 
 '''

class Solution:
    def fractionAddition(self, exp: str) -> str:
        
        if not exp:
            return "0/1"
        
        if exp[0] != '-':
            exp = '+' + exp
        
        # Parse the expression to get the numerator and denominator of each fraction
        num = []
        den = []
        pos = True
        i = 0
        while i < len(exp):
            # Check sign
            pos = True if exp[i] == '+' else False
            
            # Get numerator
            i += 1
            n = 0
            while exp[i].isdigit():
                n = n*10 + int(exp[i])
                i += 1
            num.append(n if pos else -n)
            
            # Get denominator
            i += 1
            d = 0
            while i < len(exp) and exp[i].isdigit():
                d = d*10 + int(exp[i])
                i += 1
            den.append(d)
        
        # Multiply the numerator of all fractions so that they have the same denominator
        denominator = functools.reduce(lambda x, y: x*y, den)
        for i,(n,d) in enumerate(zip(num, den)):
            num[i] = n * denominator // d
        
        # Sum up all of the numerator values
        numerator = sum(num)
        
        # Divide numerator and denominator by the greatest common divisor (gcd)
        g = math.gcd(numerator, denominator)
        numerator = numerator // g
        denominator = denominator // g
        
        return f"{numerator}/{denominator}"
      
------------------------------------------------------------------------------------------------------
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = []
        den = []

        i=0
        status=False
        temp=''
        while i<len(expression):
            if expression[i]=='/':
                if status:
                    num.append(-int(temp))
                else:
                    num.append(int(temp))
                temp = ''
                status = False
            elif expression[i]=='+':
                den.append(int(temp))
                temp = ''
            elif expression[i]=='-':
                if temp!='':
                    den.append(int(temp))
                    temp = ''
                status = True
            else:
                temp += expression[i]
            i+=1
        den.append(int(temp))

        numerator=num[0]
        denominator=den[0]
        for i in range(1,len(num)):
            numerator = numerator*den[i] + denominator*num[i]
            denominator = denominator*den[i]

        g = gcd(numerator ,denominator)
        numerator //= g
        denominator //= g
        if denominator<0:
            numerator = -numerator
            denominator = -denominator

        return str(numerator)+'/'+str(denominator)
