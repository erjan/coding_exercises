'''
Дан массив целых чисел nums размерности 2n. Элементы 
массива расположены в следующем порядке: [x1,x2,...,xn,y1,y2,...,yn]. Необходимо 
преобразовать массив к виду [x1,y1,x2,y2,...,xn,yn].
'''


class Answer:
    def shuffle(self, nums, n):
        res = list()

        for i in range(len(nums)-n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
        
-----------------------------------------------------------------------
class Answer:
    def shuffle(self, nums, n):
            res = []
            for i, j in zip(nums[:n],nums[n:]):
                res += [i,j]
            return res
