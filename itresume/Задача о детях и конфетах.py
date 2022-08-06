'''
Дан массив целых чисел candies, на i месте в котором находится количество конфет у i ребенка. Также дано целое число extraCandies. Необходимо для каждого ребенка проверить: если дать ему extraCandies, будет ли у него больше всего конфет?

Примечание: Одновременно может быть несколько детей с одинаково большим количеством конфет.
'''


class Answer:
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        
        diff = m - extraCandies
        res = list()
        for c in candies:
            if extraCandies + c >=m:
                res.append(True)
            else:
                res.append(False)
        return res
