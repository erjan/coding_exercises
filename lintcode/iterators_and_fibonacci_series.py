'''

In this problem we need to customize an iterator to generate Fibonacci series, we have already written the code to set two initial values and return the iterator itself in solution.py for you, and you don't need to instantiate the class or call the method, we have already written in main.py. you just need to fill in the rest of the __next__() You just need to fill in the rest of the code in __next__() to implement the accumulation and assignment of initial values , and the evaluator will automatically form a set of Fibonacci series with your return value as the right boundary.

'''


class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self   

    def __next__(self):
        # write your code here:
        self.a = self.a + self.b
        self.a, self.b = self.b, self.a
        return self.a
