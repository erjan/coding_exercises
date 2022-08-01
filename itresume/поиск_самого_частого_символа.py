'''
Дана строка str. Необходимо написать функцию, которая принимает на вход строку и выводит кортеж из двух элементов:

Самый часто встречающийся символ
Количество его повторов
Примечание 1: Если несколько символов встречаются одинаковое количество раз, то вывести любой из кортежей.

Примечание 2: Пробел и знаки препинания тоже считаются символами.
'''

from collections import Counter

class Answer:
    def max_char(self, str1):
        
        res = dict(Counter(str1))

        maxcount = float('-inf')
        letter = 'a'

        for k, v in res.items():

            if v >= maxcount:
                maxcount = v
                letter = k
        return (letter, maxcount)
        
        
        
        
        
