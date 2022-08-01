'''
Дано число n. Необходимо разложить факториал этого число на простые множители и представить результат в строковом виде.
'''


from collections import Counter


class Answer:

    def decomp(self, n):
        
        def f(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return factors
    
        res = list()
        for i in range(1, n+1):
            res.append(i)

        d = list()
        for n in res:
            temp = f(n)
            d.extend(temp)

        d = dict(Counter(d))
        res = ''
        for k, v in d.items():
            if v != 1:
                res += str(k) + "^" + str(v) + " * "
            else:
                res += str(k) + " * "
        res = res[:-2]
        res = res.rstrip()
        return res

        
        

