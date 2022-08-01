'''
Напишите функцию multiplier, которая будет возвращать произведение всех членов массива arr.
'''

class Answer:
    def multiplier(self, arr):
        
        res = arr[0]
        
        for i in range(1, len(arr)):
            res = res* arr[i]
        return res
