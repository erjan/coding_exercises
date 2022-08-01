'''
Дано целое число n. Написать функцию-генератор fibonacci, которая будет возвращать n первых чисел Фиббоначи при вызове метода next.
'''

class Answer:
    def fibonacci(self, n): 
        a, b = 1, 1
        for _ in range(1,n+1):
            yield a
            a, b = b, a + b

        
