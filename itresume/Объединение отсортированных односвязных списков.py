'''
Даны два отсортированных односвязных списка. Необходимо объединить их и вернуть итоговый отсортированный односвязный список.
'''

class Answer:
       def mergeTwoLists(self, a, b):
            if a and b:
                if a.val > b.val:
                    a, b = b, a
                a.next = self.mergeTwoLists(a.next, b)
            return a or b
