'''
Implement a data structure with the following methods:

add(int val) adds the value val to the data structure
find(int val) returns whether there are two elements whose sum equals to val
Constraints

n ≤ 10,000 where n is the number of times add will be called
m ≤ 1,000 where m is the number of times find will be called
'''



class TwoSum:
    def __init__(self):
        self.main = list()
        

    def add(self, val):
        self.main.append(val)
        

    def find(self, val):
        map = {}
        target = val
        num = self.main
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return True

        return False
      
--------------------------------------------------------------------------
class TwoSum:
    def __init__(self):
        self.dictionary = defaultdict(int)

    def add(self, val):
        self.dictionary[val] += 1

    def find(self, val):
        ls = self.dictionary.keys()
        for i in ls:
            to_find = val - i
            if to_find == i:
                if self.dictionary[i] > 1:
                    return True
            elif to_find in ls:
                return True
        return False
    
----------------------------------------------------------------------
class TwoSum:
    def __init__(self):

        self.d = defaultdict(int)
        

    def add(self, val):
        self.d[val]+=1
        

    def find(self, val):

        keys = self.d.keys()

        for k in keys:
            toFind = val - k

            if toFind == k:
                if self.d[k] > 1:
                    return True
            elif toFind in keys:
                return True
        return False
    
-----------------------------------------------------------------------------------------
class TwoSum:
    def __init__(self):
        self.cache = defaultdict(int)

    def add(self, val):
        self.cache[val] += 1

    def find(self, val):
        for key in self.cache:
            target = val - key
            if target == key and self.cache[key] > 1:
                return True
            elif target != key and target in self.cache:
                return True
        return False
        
