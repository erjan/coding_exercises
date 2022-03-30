'''

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false

'''



class TwoSum:

    def __init__(self):
        self.l = []

    def add(self, number: int) -> None:
        self.l.append(number)

    def find(self, value: int) -> bool:
        
        nums = self.l
        target = value
        
        
        seen = {}
        for i, k in enumerate(nums): 

            remaining = target - nums[i]  

            if remaining in seen:  
                return True  
            else:
                seen[k] = i  
        return False
                


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
