
'''
Даны первые узлы двух односвязных списков:

headA - начальный узел списка A
headB - начальный узел списка B
В некотором узле списке пересекаются. Необходимо найти и вернуть первый узел, в котором значения списков A и B совпадут.

Если пересечений у списков нет, то вернуть NULL.
'''

#Описание класса-узла
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Answer:
    def getIntersectionNode(self, headA, headB):
        
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
        
        
        
'''
        if headA is None or headB is None:
            return None
        elif headA.val != headB.val:
            return self.getIntersectionNode(headA.next, headB.next)
        else:
            return ListNode(headA.val)
        '''
                
