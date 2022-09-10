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
