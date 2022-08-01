'''
Каждый из датафреймов содержит полностью идентичные названия и типы столбцов - просто в каждом из них содержится информация за разный промежуток времени.
'''

import pandas as pd

df1 = [
    {'page1': 1, 'page2': 25, 'page3': 3}, 
    {'page1': 4, 'page2': 58, 'page3': 1}, 
    {'page1': 1.5, 'page2': 8, 'page3': 0.5}
    ]

df2 = [
     {'page1': 2, 'page2': 11, 'page3': None}, 
     {'page1': 5, 'page2': 21, 'page3': 5}, 
     {'page1': 0.1, 'page2': 38, 'page3': 15}
     ]

df3 = [
     {'page1': 2, 'page2': 11, 'page3': 40}, 
     {'page1': 5, 'page2': 15, 'page3': None}, 
     {'page1': 4, 'page2': 21, 'page3': 13}
     ]

df1, df2, df3 = [pd.DataFrame(df) for df in [df1, df2, df3]]

class Answer:
    def calcMean(self, df1, df2, df3):
        main_df = df1.append(df2)
        main_df = main_df.append(df3)

        main_df = main_df.dropna(axis=0, subset=['page3'])
        main_df.loc['Mean'] = main_df.mean()
        return main_df

        
