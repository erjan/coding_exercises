'''

Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in
'''

class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.i4 = 0
        self.n4 = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4 = 0
                self.n4 = read4(self.buf4)
                if self.n4 == 0:
                    break
            buf[i] = self.buf4[self.i4]
            self.i4 += 1
            i += 1
        return i
