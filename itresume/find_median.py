'''
Вам дан набор чисел в виде списка Python. Необходимо найти медиану этого числового ряда.

Задание
Напишите функцию FindMedian, которая будет возвращать одно число - медианное значение.

Функция FindMedian принимает на вход arr - исходный список с числами.
'''

import math
class Answer:
    def FindMedian(self, arr):
        nums = arr
        if len(nums) == 0:
            return None

        nums.sort()
        if len(nums) % 2 == 0:
            res = (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
            return res
        
        else:
            return math.ceil(nums[len(nums)//2])
