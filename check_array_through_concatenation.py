'''
ou are given an array of distinct integers arr and an array 
of integer arrays pieces, where the integers in pieces are distinct. Your 
goal is to form arr by concatenating the arrays in pieces in any order. However, you are 
not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.
'''

import unittest

def f(a, pieces):

    i = 0
    counter = 0

    di = dict()
    for i in range(len(pieces)):
        
        first_item = pieces[i][0]
        di[first_item] = i

    #this i is used before - поэтому у меня были проблемы когда я ее заново юзал в цикле
    #print('counter i before the main loop %d' % i) # this is important! the index i will remain after you use it in another loop!!!!
    i = 0
    while i < len(a):      
        if counter < len(pieces) and a[i] in di:
            for num in pieces[di[a[i]] ]:
                if a[i] == num :
                    i+=1
                else:
                    return False
            counter+=1
        else:
            counter+=1
            i+=1
            return False
        
    return True
      
class ss1(unittest.TestCase):
    
    def test1(self):
        a = [85]
        p = [[85]]
        res = f(a,p)
        self.assertEqual(res,True)
        
    def test2(self):
        a = [15,88]
        p = [[88], [15]]
        res = f(a,p)
        self.assertEqual(res,True)
    
    def test3(self):
        a = [49,18,16]
        p = [[16,18,49]]
        
        res = f(a,p)
        self.assertEqual(res, False)
    
    def test4(self):
        a = [91,4,64,78]
        p = [[78],[4,64],[91]]
        
        res = f(a,p)
        self.assertEqual(res, True)
    
    def test5(self):
        a = [1,3,5,7]
        p = [[2,4,6,8]]
        res = f(a,p)
        self.assertEqual(res, False)
        
    def test6(self):
        a = [1,2,3]
        p = [[1,3],[2]]
        res = f(a,p)
        self.assertEqual(res, False)
        
    def test7(self):
        a = [3,4,8]
        p = [[3], [5,8]]
        res = f(a,p)
        self.assertEqual(res, False)
    

if '__main__' == __name__:

    unittest.main()


 

        
        
