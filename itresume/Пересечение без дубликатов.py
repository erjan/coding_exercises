'''
Вам дано 2 набора чисел arr1 и arr2 в виде списка Python. Необходимо вернуть список, состоящий из элементов пересечения. Дубликаты необходимо удалить.
'''


class Answer:
    def PureIntersection(self, arr1, arr2):
        return list(set(arr1).intersection(set(arr2)))
