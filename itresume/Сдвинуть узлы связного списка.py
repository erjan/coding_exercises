'''
Дан односвязный список с начальным узлом head. Необходимо сдвинуть узлы на заданное число k.
'''

#Описание класса-узла
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next


class Answer:
    def rotateRight(self, head, k):
        if not head:
            return head

        len = 0
        tail = head
        temp = head

        while temp:
            temp = temp.next
            len += 1
        print('len is %d' % len)

        k = k % len
        if k == 0:
            return head
        
        cur = head
        for i in range(len - k -1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead
