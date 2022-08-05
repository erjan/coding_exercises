
'''

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
'''


class Solution:

    def printList(self, l):

        while l:
            if l.next is None:
                print(l.val)
            else:
                print(l.val, end='-')
            l = l.next
        print()

    def mergeInBetween(self, list1, list2, a, b):

        head = list1
        beforea = list1
        beforeb = list1

        for i in range(a-1):
            print(beforea.val)
            beforea = beforea.next

        for i in range(b+1):
            print(beforeb.val)
            beforeb = beforeb.next

        beforea.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = beforeb

        print('head')
        self.printList(head)
        return head
