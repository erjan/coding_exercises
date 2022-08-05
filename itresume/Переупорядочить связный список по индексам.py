
'''
Дан односвязный список с начальным 
узлом head. Необходимо переупорядочить этот список таким образом, что 
сначала будут идти все узлы с нечетными индексами из начального списка, а затем все с 
четными индексами.
'''

#Описание класса-узла
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next


class Answer:
    def oddEvenList(self, head):

        if(not head): return head
        odd = head
        even = head.next
        evenHead = even
        while(even and odd and even.next and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
