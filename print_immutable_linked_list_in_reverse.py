'''
You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.
'''

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # get size of list in O(n) time
        size = 0
        temp = head
        while temp:
            temp = temp.getNext()
            size += 1
        
        # choose a size for our chunks
        optimal_size = int(sqrt(size))
        
        # store starts to sub chunks in O(n) time and O(sqrt(n)) space
        sub_heads = []
        count = 0
        while head:
            if count % optimal_size == 0:
                sub_heads.append(head)
            head = head.getNext()
            count += 1
        
        # start at last chunk and print it backwards
        # at worst we only keep sqrt(n) elements in the stack
        # so this step is also O(n) time and O(sqrt(n)) space
        stack = []
        while sub_heads:
            node = sub_heads.pop()
            i = 0
            while node and i < optimal_size:
                stack.append(node)
                node = node.getNext()
                i += 1
            while stack:
                stack.pop().printValue()
-----------------------------------------------------------------------

def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        current = head
        if current.getNext():
            self.printLinkedListInReverse(current.getNext())
        current.printValue()
--------------------------------------------------

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        _next = head.getNext()
        if _next:
            self.printLinkedListInReverse(_next)
        
        head.printValue()
----------------------------------------

class Solution:
    """Approach 1: Recursive\n
    Time    : O(N)\n
    Space   : O(N)\n
    """
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()


class Solution:
    """Approach 2: Iterative\n
    Time    : O(N)\n
    Space   : O(N)\n
    """
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        stack = []
        while head:
            stack.append(head)
            head = head.getNext()
        while stack:
            stack.pop().printValue()
------------------------------------------------------------------------

The idea is to create a parallel linked list with two pointers (one pointing to previous element and second pointing to a node from the original linked list. This saves the time spend in reversing the list if using list based approach. It would take the same time as the recursive approach
image

class mod_list:
    
    def __init__(self, next_p=None, val_p=None):
        self.next_p = next_p
        self.val_p = val_p
        
        

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        
        
        
        rev_list = []
        
        mhead = mod_list()
        
        mhead.val_p = head
        
        
        while head.getNext():
            
            
            
            mhead_cpy = mhead
            
            mhead = mod_list()
            
            mhead.next_p = mhead_cpy
            
            
            head = head.getNext()
            
            mhead.val_p = head
            
            
            
            
        
        while mhead:
            mhead.val_p.printValue()
            
            mhead = mhead.next_p
-----------------------------------------------------------------------
                                                                
                                                                # """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        curr_node = head
        if curr_node.getNext() != None:
            self.printLinkedListInReverse(curr_node.getNext())
        curr_node.printValue()
                                                                
            
        
        
                
