'''

Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

Implement the PhoneDirectory class:

PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
bool check(int number) Returns true if the slot number is available and false otherwise.
void release(int number) Recycles or releases the slot number.
'''

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.a = [0] * maxNumbers
        self.maxNumbers = maxNumbers

    def get(self) -> int:
        index = None
        for i in range(0,self.maxNumbers):
            if self.a[i] == 0:
                index = i
                break
        if index == None:
            return -1
        else:
            self.a[index] = 1
            return index
                
        
    def check(self, number: int) -> bool:
        try:
            x = self.a[number]
            if x == 0:
                return True
            else:
                return False
        except IndexError:
            return False

    def release(self, number: int) -> None:
        self.a[number] = 0
