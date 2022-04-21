'''
A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

Each node has three attributes:

coefficient: an integer representing the number multiplier of the term. The coefficient of the term 9x4 is 9.
power: an integer representing the exponent. The power of the term 9x4 is 4.
next: a pointer to the next node in the list, or null if it is the last node of the list.
For example, the polynomial 5x3 + 4x - 7 is represented by the polynomial linked list illustrated below:



The polynomial linked list must be in its standard form: the polynomial must be in strictly descending order by its power value. Also, terms with a coefficient of 0 are omitted.

Given two polynomial linked list heads, poly1 and poly2, add the polynomials together and return the head of the sum of the polynomials.

PolyNode format:

The input/output format is as a list of n nodes, where each node is represented as its [coefficient, power]. For example, the polynomial 5x3 + 4x - 7 would be represented as: [[5,3],[4,1],[-7,0]].
'''

Algo
Similar to that of 21. Merge Two Sorted Lists.

Implementation

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = node = PolyNode() 
        while poly1 and poly2: 
            if poly1.power > poly2.power: 
                node.next = node = poly1
                poly1 = poly1.next 
            elif poly1.power < poly2.power: 
                node.next = node = poly2
                poly2 = poly2.next 
            else: 
                coef = poly1.coefficient + poly2.coefficient
                if coef: node.next = node = PolyNode(coef, poly1.power)
                poly1 = poly1.next 
                poly2 = poly2.next 
        node.next = poly1 or poly2
        return dummy.next 
Alternative implementation

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = node = PolyNode()
        while poly1 and poly2: 
            temp = PolyNode(y=max(poly1.power, poly2.power))
            if poly1.power == temp.power: 
                temp.coefficient += poly1.coefficient
                poly1 = poly1.next 
            if poly2.power == temp.power: 
                temp.coefficient += poly2.coefficient 
                poly2 = poly2.next 
            if temp.coefficient: node.next = node = temp 
        node.next = poly1 or poly2
        return dummy.next 
-----------------------------------------------------------------------------------------

Approach #1. Hashmap + Sort
Create a map/dictionary, set power as key and coefficient as value
Iterate over two linkedlist and combine the coefficient
Use reversed sort to return descending order node
Time: O( (M+N) lg (M+N) )
Space: O(M+N)

  
  class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        d = collections.defaultdict(int)
        cur = poly1
        while cur:
            d[cur.power] += cur.coefficient
            cur = cur.next 
        cur = poly2
        while cur:
            d[cur.power] += cur.coefficient
            cur = cur.next 
        dummy = cur = PolyNode()
        for power in sorted(d.keys(), reverse=True):
            if not d[power]: continue
            cur.next = PolyNode(d[power], power)
            cur = cur.next 
        return dummy.next      
        
--------------------------------------------------

Approach #2. Two pointers + Greedy
Since both linkedlist have already sorted by power, use two pointer compare all the situations
From poly1 and poly2, get the coefficient with larger power as cur.next
If poly1.power == poly2.power, add their coefficient together
if the sum of coefficient is 0, then skip (i.e. 0*X^power will always be just 0, doesn't make sense to create a node)
Finally, check if there is any left over in either node
Time: O(M+N)
Space: O(1)
                                           
                                           
class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = cur = PolyNode()
        while poly1 and poly2:
            if poly1.power == poly2.power:
                if (s:=poly1.coefficient + poly2.coefficient) == 0: 
                    poly1, poly2 = poly1.next, poly2.next 
                    continue
                cur.next = PolyNode(s, poly2.power)
                cur, poly1, poly2 = cur.next, poly1.next, poly2.next 
            elif poly1.power > poly2.power:    
                cur.next = PolyNode(poly1.coefficient, poly1.power)
                cur, poly1 = cur.next, poly1.next 
            else:    
                cur.next = PolyNode(poly2.coefficient, poly2.power)
                cur, poly2 = cur.next, poly2.next 
        while poly1:
            cur.next = PolyNode(poly1.coefficient, poly1.power)
            cur, poly1 = cur.next, poly1.next 
        while poly2:
            cur.next = PolyNode(poly2.coefficient, poly2.power)
            cur, poly2 = cur.next, poly2.next 
        return dummy.next
                                           
-----------------------------------------------------------------------------------------------------------------
                                           # Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        poly = None
        curr = None
        
        # If any of the polynomial exists
        while poly1 or poly2:
            
            coff = 0
            power = 0
            
            # For both polynomial
            if poly1 and poly2:
                # Polynomail with higher power will be
                # given preference to form node. If they
                # have same power at a particual point they
                # both are considered to form a node.
                if poly1.power > poly2.power:
                    coff = poly1.coefficient
                    power = poly1.power
                    poly1 = poly1.next
                elif poly2.power > poly1.power:
                    coff = poly2.coefficient
                    power = poly2.power
                    poly2 = poly2.next
                else:
                    coff = poly1.coefficient + poly2.coefficient
                    power = poly1.power
                    poly1 = poly1.next
                    poly2 = poly2.next
            elif poly1: # if only first polynomial 
                    coff = poly1.coefficient
                    power = poly1.power
                    poly1 = poly1.next
            elif poly2: # if only second polynomial
                    coff = poly2.coefficient
                    power = poly2.power
                    poly2 = poly2.next
            else: # no reason to continue 
                break
            
            # If coefficient after addition is
            # greater than 0, then only consider
            # curretn coefficient and power
            # to make a node
            if coff:
                pnode = PolyNode(coff, power)
                if not poly:
                    poly = pnode
                    curr = poly
                else:
                    curr.next = pnode
                    curr = curr.next
                    
        return poly
-----------------------------------------------------------------------------------------------
                                           class Solution:
    
    def _update_head_with_node(self, h, n):
        h.next = PolyNode(n.coefficient, n.power)
        n = n.next
        h = h.next
        return h, n
    
    def _combine_nodes(self, h, n1, n2):
        final_coeff = n1.coefficient + n2.coefficient
        if final_coeff != 0:
            h.next = PolyNode(x=final_coeff, y=n1.power)
            h = h.next
        n1 = n1.next
        n2 = n2.next
        return h, n1, n2
    
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        dummy = head = PolyNode()
        
        p1 = poly1
        p2 = poly2

        
        while p1 or p2:
            if not p1:
                head, p2 = self._update_head_with_node(head, p2)
                continue

            if not p2:
                head, p1 = self._update_head_with_node(head, p1)
                continue
            
            if p1.power == p2.power:
                head, p1, p2 = self._combine_nodes(head, p1, p2)
            elif p1.power < p2.power:
                head, p2 = self._update_head_with_node(head, p2)
            else:
                head, p1 = self._update_head_with_node(head, p1)        
        
        return dummy.next
                                           
                                           
        
      
