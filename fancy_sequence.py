'''
Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
'''

Explanation
Count the prefix sum add of addAll
Count the prefix mul mul of mulAll

class Fancy(object):

    def __init__(self):
        self.A = []
        self.add = [0]
        self.mul = [1]

    def append(self, a):
        self.A.append(a)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc):
        self.add[-1] += inc

    def multAll(self, m):
        self.add[-1] = self.add[-1] * m % (10 ** 9 + 7)
        self.mul[-1] = self.mul[-1] * m % (10 ** 9 + 7)

    def getIndex(self, i):
        if i >= len(self.A): return -1
        mod = 10 ** 9 + 7
        m = self.mul[-1] * pow(self.mul[i], mod - 2, mod) 
        inc = self.add[-1] - self.add[i] * m
        return (self.A[i] * m + inc) % mod
