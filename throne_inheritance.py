'''
A kingdom consists of a king, his children, his grandchildren, and so on. Every once in a while, someone in the family dies or a child is born.

The kingdom has a well-defined order of inheritance that consists of the king as the first member. Let's define the recursive function Successor(x, curOrder), which given a person x and the inheritance order so far, returns who should be the next person after x in the order of inheritance.

Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
For example, assume we have a kingdom that consists of the king, his children Alice and Bob (Alice is older than Bob), and finally Alice's son Jack.

In the beginning, curOrder will be ["king"].
Calling Successor(king, curOrder) will return Alice, so we append to curOrder to get ["king", "Alice"].
Calling Successor(Alice, curOrder) will return Jack, so we append to curOrder to get ["king", "Alice", "Jack"].
Calling Successor(Jack, curOrder) will return Bob, so we append to curOrder to get ["king", "Alice", "Jack", "Bob"].
Calling Successor(Bob, curOrder) will return null. Thus the order of inheritance will be ["king", "Alice", "Jack", "Bob"].
Using the above function, we can always obtain a unique order of inheritance.

Implement the ThroneInheritance class:

ThroneInheritance(string kingName) Initializes an object of the ThroneInheritance class. The name of the king is given as part of the constructor.
void birth(string parentName, string childName) Indicates that parentName gave birth to childName.
void death(string name) Indicates the death of name. The death of the person doesn't affect the Successor function nor the current inheritance order. You can treat it as just marking the person as dead.
string[] getInheritanceOrder() Returns a list representing the current order of inheritance excluding dead people.
 
 '''

class ThroneInheritance:

    def __init__(self, kingName: str):
        # Taking kingName as root
        self.root = kingName

        # notDead will hold all the people who are alive and their level number
        self.alive = {}
        self.alive[kingName] = 0
        
        # hold edges existing in our graph
        self.edges = {self.root:[]}
    
    def birth(self, parentName: str, childName: str) -> None:
        # birth --> new child so update alive
        self.alive[childName] = self.alive[parentName]+1
        
        # add parent to child edges in the edges dictionary
        if parentName in self.edges:
            self.edges[parentName].append(childName)
            if childName not in self.edges:
                self.edges[childName] = []
        else:
            if childName not in self.edges:
                self.edges[childName] = []
            self.edges[parentName] = [childName]
            
    
    def death(self, name: str) -> None:
        # removing the dead people from alive map
        del self.alive[name]
        
    def getInheritanceOrder(self) -> List[str]:
        
        hierarchy = []
        def dfs(cur,parent=-1):
            nonlocal hierarchy
            
            # current person available in alive then only add in hierarchy
            if cur in self.alive:
                hierarchy.append(cur)
            
            # traverse all the children of current node
            for i in self.edges[cur]:
                if i!=parent:
                    dfs(i,cur)
        dfs(self.root)
        return hierarchy
------------------------------------------------------------
class Node:
    def __init__(self, name):
        self.name = name 
        self.alive = True
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.d = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        self.d[childName] = Node(childName)
        self.d[parentName].addChild(self.d[childName])
        
    def death(self, name: str) -> None:
        self.d[name].alive = False 

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            ans = [node.name]*node.alive
            for x in node.childs:
                ans.extend(dfs(x))
            return ans 
        
        return dfs(self.king)
      
