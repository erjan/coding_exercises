'''
На вход подается массив целых чисел arr. Написать
функцию even, которая возвращает список значений из исходного списка arr, у которых четные индексы (индексацию считать с единицы).
'''


class Answer:
    def even(self, arr):
        
        res = list()
        
        for i in range(len(arr)):
            
            if (i+1) %2 ==0:
                res.append(arr[i])
        return res
