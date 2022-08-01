'''
Дан список чисел arr. Написать функцию perms, которая возвращает список из кортежей со всеми возможными перестановками из исходных чисел.
'''

import itertools

class Answer:
    def perms(self, arr): 
        
        return list(itertools.permutations(arr))

