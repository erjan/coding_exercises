'''
Дано два списка: A и B. Список A содержит в себе 
целочисленный номер, а список B - строки произвольной длины. Необходимо написать функцию
pairs, которая будет возвращать список, состоящий из кортежей с двумя элементами: номер из списка A и строка из списка B.
'''


from itertools import zip_longest

class Answer:
    def pairs(self, a, b):
        l = list(zip_longest(a, b))
        for i in range(len(l)):
            l[i] = list(l[i])

        for i in range(len(l)):
            item = l[i]
            if l[i][1] is None:
                l[i][1] = 0
        
        for i in range(len(l)):
            l[i] = tuple(l[i])
        return l
        
        
