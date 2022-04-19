'''
Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dict_t = collections.defaultdict(int)
        curr = head
        while (curr):
            dict_t[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while head:
            if dict_t[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next          
            head = head.next
        return dummy.next
      
---------------------------------------

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        d = {}
        p = head
        while p:
            d[p.val] = d.get(p.val, 0) + 1
            p = p.next
        p = prehead = ListNode(0, head)
        while p.next:
            if d[p.next.val] > 1:
                p.next = p.next.next
            else:
                p = p.next
        return prehead.next
---------------------------------------------

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        seen = set()
        dups = set()
        
        node = head
        while node:
            if node.val in seen:
                dups.add(node.val)
            else:
                seen.add(node.val)
            node = node.next
                
        head_pointer = ListNode(0, head)
        node = head_pointer
        while node.next:
            if node.next.val in dups:
                node.next = node.next.next
            else:
                node = node.next
        
        return head_pointer.next
-----------------------------------------------------

Using the same deletion technique on different linkedlist questions:

https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1829827/19.-PYTHON-Linked-list-explanation
https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/1829834/83.-PYTHON-Linked-list-explanation
https://leetcode.com/problems/remove-linked-list-elements/discuss/1829825/203.-PYTHON-Linked-list-explanation
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/discuss/1829829/2095.-PYTHON-Linked-list-explanation
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1832762/82-python-linked-list-deletion-explanation
class Solution:
def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

    seen = set()
    toDelete = set()
    
    sentinel = ListNode(0, head) #Make dummy node
    sentinel.next = head #Connect sentinel to head
    prev = sentinel #Prev set at sentinel
    
    curr = head
    
    #First Pass
    while curr:
        
        #add see node to hashset
        if curr.val not in seen:
            seen.add(curr.val)
            
        elif curr.val in seen:
            toDelete.add(curr.val)
        
            
        curr = curr.next #Move along

    #Second Pass    
    curr2 = head
    
    while curr2:
        
        if curr2.val in toDelete: #Duplicate
            
            prev.next = curr2.next  #Deletion here
            curr2 = curr2.next #Move along
        
        else:
            
            prev = prev.next   #Move along
            curr2 = curr2.next #Move along
            
    return sentinel.next
    
    #Time: O(N)
    #Space: O(N)
--------------------------------------------------------------------

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        dic = defaultdict(int)

        while head:
            dic[head.val] += 1
            head = head.next

        a = [key for key,value in dic.items() if value == 1]
        
        dummy = ans = ListNode()
        
        for i in range(len(a)):
            ans.next = ListNode(a[i])
            ans = ans.next
            
        return dummy.next
-------------------------------------------------------------------------      
      
    
      
      
