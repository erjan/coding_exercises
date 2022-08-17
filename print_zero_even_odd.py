'''
You have a function printNumber that can be called with an integer parameter and prints it to the console.

For example, calling printNumber(7) prints 7 to the console.
You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A: calls zero() that should only output 0's.
Thread B: calls even() that should only output even numbers.
Thread C: calls odd() that should only output odd numbers.
Modify the given class to output the series "010203040506..." where the length of the series must be 2n.

Implement the ZeroEvenOdd class:

ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
void zero(printNumber) Calls printNumber to output one zero.
void even(printNumber) Calls printNumber to output one even number.
void odd(printNumber) Calls printNumber to output one odd number.
'''


from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.gates = [Lock(),Lock(),Lock()]
        self.gates[0].acquire()
        self.gates[1].acquire()
        
    def zero(self, printNumber):
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.ct += 1
            self.gates[self.ct % 2].release()
        
    def even(self, printNumber):
        for _ in range(self.n//2):
            self.gates[0].acquire()
            printNumber(self.ct)
            self.gates[2].release()
        
    def odd(self, printNumber):
        for _ in range((self.n+1)//2):
            self.gates[1].acquire()
            printNumber(self.ct)
            self.gates[2].release()
