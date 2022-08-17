'''
You have the four functions:

printFizz that prints the word "fizz" to the console,
printBuzz that prints the word "buzz" to the console,
printFizzBuzz that prints the word "fizzbuzz" to the console, and
printNumber that prints a given integer to the console.
You are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four different threads:

Thread A: calls fizz() that should output the word "fizz".
Thread B: calls buzz() that should output the word "buzz".
Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
Thread D: calls number() that should only output the integers.
Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the ith token (1-indexed) of the series is:

"fizzbuzz" if i is divisible by 3 and 5,
"fizz" if i is divisible by 3 and not 5,
"buzz" if i is divisible by 5 and not 3, or
i if i is not divisible by 3 or 5.
'''


from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzLock = Lock(); self.fizzLock.acquire()
        self.buzzLock = Lock(); self.buzzLock.acquire()
        self.fzbzLock = Lock(); self.fzbzLock.acquire()
        self.numberLock = Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while True: 
            self.fizzLock.acquire()
            if self.n == 0: break 
            printFizz()
            self.numberLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True: 
            self.buzzLock.acquire()
            if self.n == 0: break 
            printBuzz()
            self.numberLock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True: 
            self.fzbzLock.acquire()
            if self.n == 0: break  
            printFizzBuzz()
            self.numberLock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1, self.n+1):
            self.numberLock.acquire()
            if x % 15 == 0: 
                self.fzbzLock.release()
            elif x % 3 == 0: 
                self.fizzLock.release()
            elif x % 5 == 0: 
                self.buzzLock.release()
            else: 
                printNumber(x)
                self.numberLock.release()
                
        self.numberLock.acquire()
        self.n = 0 
        self.fizzLock.release()
        self.buzzLock.release()
        self.fzbzLock.release()
