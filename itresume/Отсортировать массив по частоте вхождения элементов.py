'''
Дан массив целых чисел nums. Необходимо
отсортировать массив по возрастанию частоты вхождения элементов
в массив. Если несколько значений встречаются в массиве одинаковое количество раз, то необходимо
такие элементы расположить по убыванию значений.
'''


class Answer:
    def frequencySort(self, A):
        d = dict()

        for i in range(len(A)):

            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1

        res = [[k, v] for k, v in d.items()]

        res = sorted(res, key=lambda x: (x[1], -x[0]))
        res = dict(res)
        temp = []

        for k, v in res.items():
            for j in range(v):
                temp.append(k)

        return temp
      
---------------------------------------------------------
from collections import Counter
class Answer:
    def frequencySort(self, A):
        count = Counter(A)
        return sorted(A, key=lambda x: (count[x], -x))
