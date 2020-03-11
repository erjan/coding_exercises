#We have an array A of integers, and an array queries of queries.

#For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

#(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

#Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

#very tricky problem - but tagged easy!!!!

#i did not solve it - had to look up solution.


def f(A, queries):
    
    even_sum = sum(list(filter(lambda num : num %2 == 0 , A)))
    print('before beginning the sum of all evens: %d' % even_sum)
    print()
    print()
    res = []
    print(A)
    print('even sum %d ' % even_sum)
    for val,index in queries:
        print('------------------------------------------------------')
        
        #if A[index] %2 ==0:
         #   even_sum -= A[index]
            
        # сверху 2 строчки - если их не поставить то будет такая проблема:
        # мы забываем убрать это значение - потому что не знаем какое получитца вместо него!
        # если вместо него мы получим четное - мы добавим его в общую сумму, елси - нет прсто пройдем дальше по циклу менять массив!
        # внизу я оставил пример что вылазиет когда нет этих 2 строк кода
        A[index]+= val
        
        if A[index] %2 == 0:
            even_sum += A[index]
        print('sum of all evens %d ' % even_sum)
        res.append(even_sum)
        print('the A array is: ', end = '')
        print(A)
    print()
    
    print('end result array is :')
    print(res)
    
a = [1,2,3,4]
queries = [[1,2], [2,0], [1,1], [2,0], [-3,1], [2,0],[1,1], [2,3] ]

#f(a, queries)


A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
f(A, queries)


before beginning the sum of all evens: 6

'''
[1, 2, 3, 4]
even sum 6 
------------------------------------------------------
about to add at A[0] value : 1

the A array is: [2, 2, 3, 4]
after adding sum of evens: 8 
------------------------------------------------------
about to add at A[1] value : -3

the A array is: [2, -1, 3, 4]
after adding sum of evens: 8 
------------------------------------------------------
about to add at A[0] value : -4

the A array is: [-2, -1, 3, 4]
after adding sum of evens: 6 
------------------------------------------------------
about to add at A[3] value : 2

the A array is: [-2, -1, 3, 6]
after adding sum of evens: 12 

end result array is :
[8, 8, 6, 12]
end of even sum 12 
'''
