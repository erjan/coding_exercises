'''
You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0.
'''

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
            n1 = num1
            n2 = num2
            c = 0
            while n1 != 0 and n2 != 0:
                print('n1:', n1, ' n2:', n2)
                c += 1
                if n1 >= n2:
                    n1 = n1 - n2
                else:
                    n2 = n2 - n1

            print(c)
            return c
          
class Solution:
    def countOperations(self, a: int, b: int) -> int:
        return 0 if a * b == 0 else a // b + self.countOperations(b, a % b)          
