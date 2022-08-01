from time import time


class Answer:
    def TimeDecorator(self,func):
 
        
        def wrapper(*args,**kwargs):
            start = time()

            result = func(*args, **kwargs)                      
            
            end = time()
            
            print(f'Затрачено {(end-start):.1f} секунд')

            print('Я закончила работать!')
            return result
        
        
        return wrapper
        
'''
   def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j
            
print(Answer().TimeDecorator(long_time))
       
        
'''

  
