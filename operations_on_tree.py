'''
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

Lock: Locks the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked.
Unlock: Unlocks the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
Upgrade: Locks the given node for the given user and unlocks all of its descendants regardless of who locked it. You may only upgrade a node if all 3 conditions are true:
The node is unlocked,
It has at least one locked descendant (by any user), and
It does not have any locked ancestors.
Implement the LockingTree class:

LockingTree(int[] parent) initializes the data structure with the parent array.
lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, or false otherwise. If it is possible, the node num will become locked by the user with id user.
unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, or false otherwise. If it is possible, the node num will become unlocked.
upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, or false otherwise. If it is possible, the node num will be upgraded.
'''

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked_nodes = defaultdict(int)
        self.graph = defaultdict(list)
        
        for i, v in enumerate(parent):
            self.graph[v].append(i)
            
        print(self.graph)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked_nodes:
            return False
        self.locked_nodes[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked_nodes or self.locked_nodes[num] != user:
            return False
        
        del self.locked_nodes[num]
        return True
        
    def upgrade(self, num: int, user: int) -> bool:
        def check_ancestors(num):
            if num in self.locked_nodes:
                return True
            elif num == -1:
                return False
            else:
                return check_ancestors(self.parent[num])
        
        def descendants(num):
            for node in self.graph[num]:
                if node in self.locked_nodes:
                    return True
                if descendants(node):
                    return True
            return False
                
        def unlock_descendants(num):
            for node in self.graph[num]:
                if node in self.locked_nodes:
                    del self.locked_nodes[node]
                unlock_descendants(node)
            
        if num in self.locked_nodes:
            return False
        elif check_ancestors(self.parent[num]):
            return False
        elif not descendants(num):
            return False
        
        unlock_descendants(num)
        self.locked_nodes[num] = user
        
        return True
