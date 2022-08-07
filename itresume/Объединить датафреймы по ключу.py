
'''
Реализуйте аналог Excel-функции VLOOKUP (или ВПР): необходимо написать 
функцию vlookup, которая принимает на вход 2 исходных датафрейма, а возвращает новый датафрейм вида:
'''


import pandas as pd

sales = [
    {'ProductID': 1, 'Amount': 5, 'Sum': 528},
    {'ProductID': 2, 'Amount': 2, 'Sum': 624}, 
    {'ProductID': 2, 'Amount': 1, 'Sum': 312}, 
    {'ProductID': 3, 'Amount': 1, 'Sum': 10}, 
    {'ProductID': 4, 'Amount': 8, 'Sum': 10842}, 
    {'ProductID': 4, 'Amount': 3, 'Sum': 4065}, 
    {'ProductID': 5, 'Amount': 1, 'Sum': 1024}
]


products = [
    {'ProductID': 1, 'ProductName': 'Apple'},
    {'ProductID': 2, 'ProductName': 'Mango'}, 
    {'ProductID': 3, 'ProductName': 'Banana'}, 
    {'ProductID': 4, 'ProductName': 'Orange'}
]

sales, products = pd.DataFrame(sales), pd.DataFrame(products)


class Answer:
    def vlookup(self, sales, products):
        
        leftjoin = pd.merge(sales, 
                     products, 
                     on ='ProductID', 
                     how ='left')
        
        return leftjoin
