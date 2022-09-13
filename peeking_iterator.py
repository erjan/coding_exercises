'''
Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
int next() Returns the next element in the array and moves the pointer to the next element.
boolean hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.
'''

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.temp = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.temp

    def next(self):
        ret = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return ret

    def hasNext(self):
        return self.temp is not None
      
----------------------------------------------
class PeekingIterator:
	def __init__(self, iterator):
		self.iter = iterator
		self.helper = self.iter.next() if self.iter.hasNext() else None
		

	def peek(self):
		return self.helper
		

	def next(self):
		tmp = self.helper
		self.helper = self.iter.next() if self.iter.hasNext() else None
		return tmp
	

	def hasNext(self):
		return self.helper != None
