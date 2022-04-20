'''
Given the head of a singly linked list and two integers left and 
right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

'''


The idea is simple and intuitive: find linkedlist [m, n], reverse it, then connect m with n+1, connect n with m-1

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
-------------------------------------------------

For List with [1, 2, 3, 4, 5], supposed m == 2 and n == 4

Step1:
The part I need to reversed is node 2 to node 4, which has n - m + 1 = 3 nodes.
Therefore, I would like to maintain a window with n - m + 1 nodes with the window's head whead and window's tail wtail, then if whead is head, wtail would be the next n-m node from head.

[123]45 => whead is 1 and wtail is 3
Step2:
And to get to the right reversed portion we want, we need to shift the window m-1 times

1[234]5 => whead is 2 and wtail is 4
Step3: Isolate the nodes inside the window, reverse the window as Reverse Linked List

Step4: combine the outside node with reversed node.
To do so, I need to record the head outside the window ohead, and the tail outside the window otail

ohead is 1, otail is 5
1-[432]-5
Implementation detail: Since in step 4, you need to let ohead.next = reversed_headIf you create a dummy node, you can save some lines for m == 1 cases, where ohead would be None and ohead.next would fail the program.

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m >= n:
            return head
        #Step 1#    
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n-m):
            wtail = wtail.next
        #Step 2#  
        for i in range(m-1):
            ohead, whead, wtail = whead, whead.next, wtail.next
        #Step 3#  
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        #Step 4#  
        ohead.next, revtail.next = revhead, otail
        return dummy.next
            
    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail
---------------------------------------------

def reverseBetween(self, head, m, n):
    dummy = pre = ListNode(0)
    dummy.next = head
    for _ in xrange(m-1):
        pre = pre.next
    cur= pre.next
    # reverse the defined part 
    node = None
    for _ in xrange(n-m+1):
        nxt = cur.next
        cur.next = node
        node = cur
        cur= nxt
    # connect three parts
    pre.next.next = cur
    pre.next = node
    return dummy.next
--------------------------------------------

def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    
    # Comparing with Problem 206: just need to find the start position 
    # then reverse (same as 206)
    
    dummy = ListNode(0)
    dummy.next = head
    
    pre = dummy
    cur = dummy.next
    
    # find the position
    for i in range(1,m):
        cur = cur.next
        pre = pre.next
    
    
    # reverse
    for i in range(n-m):
        temp = cur.next
        cur.next = temp.next
        temp.next  = pre.next
        pre.next = temp
    
    return dummy.next
--------------------------

Method 1: Intuitive Approach.

Step1: Find the node with at position = left and the node with position = right.
Step2: Split the linkedlist into three linked list like nodeL = [1, left-1], nodeM = [left, right] and nodeR = [right, n], where n = length of the linkedlist.
Step3: Reverse the nodeM linkedlist.
Step4: Merge the linkedlists as nodeL + nodeM(reversed) + nodeR.
image

Full code for intuitive approach:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        # a standard template code to reverse a linkedlist
        def reverse(head):
            if head is None or head.next is None:
                return head
            rest = reverse(head.next)
            head.next.next = head
            head.next = None
            return rest
        
        nodeL, nodeM, nodeR = None, None, None
        
        # if both left and right points to the same element, then there is no point of reversing
        if left == right:
            return head
        
        # Split the list into left, middle, and right part, 
        # such that the middle part needs to be reversed.
        temp = ListNode()
        temp.next = head
        nodeL = temp
        
        i = 0
        while i < right:
            if i + 1 == left:
                nodeM = temp.next
                temp.next = None
                temp = nodeM
            elif i + 1 == right:
                nodeR = temp.next
                temp.next = None
                temp = nodeR
                break
            temp = temp.next
            i += 1
        
        nodeL = nodeL.next
        
        # reverse the middle part
        nodeM = reverse(nodeM)
        
        # if left part exists then add middle part to the end of left part
        if nodeL:
            temp = nodeL
            while temp.next:
                temp = temp.next
            temp.next = nodeM
        else:
            nodeL = nodeM
        
        # add right part to the end of middle part
        temp = nodeM
        while temp.next:
            temp = temp.next
        temp.next = nodeR
        
        return nodeL
Time = O(n) as we need to traverse through the whole linked list(atleast upto right).
Space = O(n) as we are using the recursive approach to reverse the linked list, so stack space = O(right - left) which is O(n).
But this can be reduced to constant space by changing the recursive method of reversing linkedlist to iterative method.
Iterative method to reverse linkedlist:

		def reverse(head):
            prev = None
            current = head
            while(current is not None):
                next = current.next
                current.next = prev
                prev = current
                current = next
            head = prev
            return head
Thus, Space = O(1).

But the challenge is can we do it in one pass? -> Yes.

Method 2: One - pass solution
Note: It is not much efficient than the above intuitive method as a lots of swaps are happening, also the above method take much lesser time than this one in actual implementation. Try executing both and see the actual runtimes.
Approach: Find the node previous of left, then swap left and left+1 along with previous next at the same time.

Read the code, then look into the picture given below and try to map the idea, it's simple.

One pass code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        if left == right:
            return head
        
        node = temp = ListNode()
        node.next = head
        
        i = 1
        while i < left:
            temp = temp.next
            i += 1
        
        
        current = temp.next
        while left < right:
            t = current.next
            current.next = t.next
            t.next = temp.next
            temp.next = t
            left += 1
            print(node.next)
        
        return node.next
      
Now you guys might be wondering how is it one pass solution, as there are two loops.
See, the first loop is going from start to left and second loop is going from left to right, so overall we are going from start to right once, hence it is one-pass.

Try doing it in a pen and paper, you will easily understand how the node-links are changing.
Try for [1,2,3,4,5,6] with left = 3 and right= 5.

image

Time = O(n)
Space = O(1).

---------------------------------------------------------------
  
  
      
      
