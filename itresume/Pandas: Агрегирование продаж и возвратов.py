'''
Руководитель просит подбить итоги в разрезе каждого сотрудника в каждом отдельном магазине:

Сколько возвратов и сколько продаж было?
Какая сумма продаж и возвратов?
Какая средняя сумма продажи и возврата?
'''



import pandas as pd

l = [
    {'Shop': "Yakimanka", 'Employee': "Anna", 'Type': 1, 'Sum': 528},
    {'Shop': "Yakimanka", 'Employee': "Fedor", 'Type': 2, 'Sum': 632},
    {'Shop': "Butovo", 'Employee': "Peter", 'Type': 1, 'Sum': 115},
    {'Shop': "Yakimanka", 'Employee': "Anna", 'Type': 1, 'Sum': 1024},
    {'Shop': "Butovo", 'Employee': "Peter", 'Type': 1, 'Sum': 1754},
    {'Shop': "Butovo", 'Employee': "Peter", 'Type': 1, 'Sum': 111},
    {'Shop': "Kamenka", 'Employee': "Max", 'Type': 1, 'Sum': 499},
    {'Shop': "Kamenka", 'Employee': "Max", 'Type': 2, 'Sum': 23},
    {'Shop': "Butovo", 'Employee': "Jugen", 'Type': 1, 'Sum': 214},
    {'Shop': "Kamenka", 'Employee': "Max", 'Type': 1, 'Sum': 964},
    {'Shop': "Yakimanka", 'Employee': "Fedor", 'Type': 2, 'Sum': 100},
    {'Shop': "Butovo", 'Employee': "Jugen", 'Type': 1, 'Sum': 10000}
]

df = pd.DataFrame(l)

class Answer:
    def grouping(self, df):
        df = df.groupby([  'Shop','Employee', 'Type']).agg(Amount = ('Sum', 'count'), Sum=('Sum', sum), Avg=('Sum', 'mean')).reset_index()
        

        
        return df
