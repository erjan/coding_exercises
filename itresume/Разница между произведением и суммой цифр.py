
'''
Дано целое число n. Найти разницу 
между произведение и суммой цифр в записи числа n.


'''

class Answer:
    def subtractProductAndSum(self, n):
        
        m = list(str(n))
        m = [int(i) for i in m]
        
        t = 1
        for i in m:
            t = t*i

    
        s = sum(m)
        return t - s
      
-----------------------------------------------------------------------
from functools import reduce
import operator

class Answer:
  def subtractProductAndSum(self, n):      
      A = list(map(int, str(n)))
      return reduce(operator.mul, A) - sum(A)
