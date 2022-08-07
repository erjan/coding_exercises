
'''
Дан массив целых чисел nums. Нужно проверить: можно ли сделать из nums неубывающий массив, изменив не более одного элемента.

Примечание: Неубывающий массив - массив, у которого каждый следующий элемент больше или равен предыдущему.
'''

class Answer:
    def checkPossibility(self, nums):
        
        counter = 0
        for i in range(len(nums)-1):
            
            if nums[i] >=nums[i+1]:
                counter+=1
        if counter > 1:
            return False
        return True
            

        
-------------------------------
#official solution

class Answer:
    def checkPossibility(self, nums):
        num_violations = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if num_violations == 1:
                    return False
                num_violations += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True
