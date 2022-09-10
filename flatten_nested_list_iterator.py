'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
'''


class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [[nestedList,0]]
        
        
    
    def next(self) -> int:
        self.hasNext()
        nestedList, i = self.stack[-1]
        
        self.stack[-1][1] +=1
        return nestedList[i].getInteger()
        
    
    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nestedList,i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1]+=1
                s.append([x.getList(),0])
                
        return False
--------------------------------------------------------------------
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self.flatten(nestedList)
        
    def flatten(self, lst):
        for el in lst:
            if el.isInteger(): self.data.append(el.getInteger())
            else: self.flatten(el.getList())
    
    def hasNext(self) -> bool: return len(self.data)
    
    def next(self) -> int: return self.data.pop(0)
    
----------------------------------------------
def dfs(nested, flat):
    for elem in nested:
        if elem.isInteger():
            flat.append(elem.getInteger())
        else:
            dfs(elem.getList(), flat)

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatList, self.i = [], 0
        dfs(nestedList, self.flatList)
    
    def next(self) -> int:
        self.i += 1
        return self.flatList[self.i-1]
    
    def hasNext(self) -> bool:
        return self.i < len(self.flatList)
