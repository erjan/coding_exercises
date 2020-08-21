class LinkedNode: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.val = data 
        self.next = None

m1 = LinkedNode(4)
m2 = LinkedNode(5)
m3 = LinkedNode(7)
m4 = LinkedNode(8)
m1.next = m2
m2.next = m3
m3.next = m4

def print_list(l):
      
    while l:
        if l.next == None:
            print(l.val)
        else:
            print(l.val, end = ' -> ')
        l = l.next
        
def reverse (item, tail = None):
    print()
    print('beginning.... %d' % item.val)
    print('tail before:')
    print_list(tail)
    tmp = item.next
    item.next = tail # вот это ключевая строка здесь!
    # мы строим именно список-лист item! 
    # когда передаем item в reverse - мы передаем туда 1 нод с последним первым числом!
    
  
    print('tail after:')
    print_list(item.next)
    if tmp is None:
        print('end of list!')
        print_list(item)
        return item
    else:
        print()
        print()
        print('recursive..')
        return reverse(tmp, item) # здесь была причина непонятки - я не видел как эта переменная обновляется. туда в item передается первый нод
        
        
   print_list(m1)
   
   d = reverse(m1, None)

# берем первый элемент, отвязываем его next, но сохраняем его чтоб дальше идти по нему
# далее передаем его как финальный лист который мы "растим". когда передаем его - он уже не пустой на 2 итерации, он содержит в себе первый нод из предыдущей итерации
# и все что нам надо это дойти до конца и вернуть лист


#iterative solution

def reverseList(self, head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
