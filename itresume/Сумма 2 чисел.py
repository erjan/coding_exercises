'''
Дан массив целых чисел nums и целое
число target. Вернуть индексы 2 чисел из массива nums, которые в сумме дают 
число target. Если target можно получить несколькими способами, то в качестве результата вернуть только один.
'''


class Answer:
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            
            x = nums[i]
            y = target -x
            
            for j in range(len(nums)):
                if nums[j] == y:
                    return [i,j]
        
        
