'''
Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

Implement the StringIterator class:

next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
'''

class StringIterator:
    def __init__(self, compressedString: str):
        self.data = []
        self.n = 0 # This to track total no of char available 
        
        i = 0
        '''Parse letters as char and freqency of it as value'''
        while i < len(compressedString):
            key = compressedString[i]
            i+= 1
            value = ""
            while True:
                if i < len(compressedString) and 48 <= ord(compressedString[i]) <= 57:
                    value += compressedString[i]
                    i += 1
                else :
                    break
        
            value = int(value)
            self.data.append((key, value))
            self.n += value
            
    def next(self) -> str:
        if self.hasNext():
            top_element = self.data[0]
            k,v = top_element[0], top_element[1]
            if v == 0:                       
                self.data.pop(0)        
                k,v = self.data[0]
            
            self.data[0] = (k, v-1)
            self.n -= 1               # Proceseed one element so subtracting it from total
            return k                  # This key item processed now
           
        else :
            return " "

    def hasNext(self) -> bool:
        if self.n > 0:
            return True
        else :
            return False
