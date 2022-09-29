'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
'''


class Solution(object):
    def insertionSortList(self, head):
        p, sl = head, ListNode()  # sl is the sortedList with dummy head node.
        while p:  # traverse the input linked list until None
            q = sl  # q is the pre of current node of sortedList
            while q.next and q.next.val < p.val:  # find the insertion position sequentially
                q = q.next
            p.next, q.next, p, q = q.next, p, p.next, q.next  # insert p to q.next
        return sl.next  # Note sl is the dummy head node
