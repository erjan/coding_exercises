#We have an array A of integers, and an array queries of queries.

#For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

#(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

#Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

#very tricky problem - but tagged easy!!!!

i did not solve it - had to look up solution.

ef f(A, queries):
    
    even_sum = sum(list(filter(lambda num : num %2 == 0 , A)))
    print('before beginning the sum of all evens: %d' % even_sum)
    print()
    print()
    res = []
    print(A)
    for val,index in queries:
        print('------------------------------------------------------')
        
        temp = 0
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
