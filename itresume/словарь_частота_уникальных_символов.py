'''
На вход подается строка str. Необходимо 
написать функцию magic_dict, которая будет составлять словарь, в котором ключами 
будут уникальные символы из str, а значениями - количество вхождений этих 
символов в строку str. При этом расположены элементы словаря должны быть в порядке лексикографического возрастания ключей.
'''

from collections import Counter

class Answer:
    def magic_dict(self, str):
        
        res = Counter(str)

        res = [[k, v] for k, v in res.items()]

        res.sort(key=lambda x: x[0])

        res = dict(res)
        return res
        
        
        
