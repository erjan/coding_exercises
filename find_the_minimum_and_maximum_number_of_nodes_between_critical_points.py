'''
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [float('inf'), -float('inf')]
        curr = head.next
        prev = head
        i = 1
        pos = []
        while(curr.next):
            if(prev.val < curr.val > curr.next.val):
                pos.append(i)
            elif(prev.val > curr.val < curr.next.val):
                pos.append(i)
            i += 1
            prev, curr = curr, curr.next
        if(len(pos) < 2):
            return -1, -1
        for i in range(1, len(pos)):
            ans[0] = min(ans[0], pos[i]-pos[i-1])
        ans[1] = pos[-1]-pos[0]
        return ans
