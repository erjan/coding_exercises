'''
We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.

For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
Given a run-length encoded array, design an iterator that iterates through it.
'''


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding

    def next(self, n: int) -> int:
        
        if self.encoding:
            
            count = self.encoding[0]
            
            if count >= n:
				# Partially exhaust and return the current value.
                self.encoding[0] -= n
                return self.encoding[1]
            
            # Exhaust all of current value and continue.
            self.encoding = self.encoding[2:]
            return self.next(n - count)
            
        return -1
