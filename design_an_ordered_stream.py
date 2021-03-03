'''
There is a stream of n (idKey, value) pairs arriving in an 
arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order 
of their IDs by returning a chunk (list) of values after each insertion. The concatenation 
of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then
returns the largest possible chunk of currently inserted values that appear next in the order.
'''


class OrderedStream:

    def __init__(self, n: int):
        self.od = [None]*(n+1)
        self.counter = 1
        self.len = n+1
                
    def insert(self, idKey: int, value: str):
        self.od[idKey] = value
        if idKey != self.counter:
            return []
        
        elif idKey == self.counter:
            temp = []
            while self.len > self.counter and self.od[self.counter] is not None :
                temp.append(self.od[self.counter])
                self.counter+=1
            
            return temp
