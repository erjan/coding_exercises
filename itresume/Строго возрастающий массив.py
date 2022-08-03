
'''
Дан массив целых чисел nums. За один шаг 
можно увеличить только один элемент массива nums на единицу. Какое минимальное количество шагов необходимо сделать, чтобы массив nums стал строго возрастающим?
'''

class Answer:
    def minOperations(self, nums):
        
        minsteps = 0
        
        for i in range(len(nums)-1):
            
            cur = nums[i] 
            next = nums[i+1]
            
            if next <=cur:
                diff = abs( next - cur) + 1
                nums[i+1] += diff
                minsteps +=diff
        return minsteps
              
               
