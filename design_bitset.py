'''
A Bitset is a data structure that compactly stores bits.

Implement the Bitset class:

Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.
void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.
void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.
boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
int count() Returns the total number of bits in the Bitset which have value 1.
String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.
'''

class Bitset:

    def __init__(self, size: int):
        self.a=[0]*size
        self.on=0;
        self.n = size;
        self.flipped=False

    
    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.a[idx]==1:
                self.on+=1
                self.a[idx]=0
        else:
            if self.a[idx]==0:
                self.on+=1
                self.a[idx]=1

    
    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.a[idx]==0:
                self.on-=1
                self.a[idx]=1
        else:
            if self.a[idx]==1:
                self.on-=1
                self.a[idx]=0

    
    def flip(self) -> None:
        if self.flipped:
            self.flipped=False
        else:
            self.flipped=True
        self.on = self.n-self.on
    
    
    def all(self) -> bool:
        if self.n==self.on:
            return True
        return False

    
    def one(self) -> bool:
        if self.on>0:
            return True
        return False

    
    def count(self) -> int:
        return self.on
        
        
    def toString(self) -> str:
        s=""
        if self.flipped:
            for i in self.a:
                if i:
                    s+="0"
                else:
                    s+="1"
            return s
        for i in self.a:
            if i:
                s+="1"
            else:
                s+="0"
        return s
