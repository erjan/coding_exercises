'''
Написать декоратор printing, который будет выводить на экран название функции, к которой он применяется, во время ее вызова.
'''

class Answer:
    def printing(self, func):
        def wrapper():
            print(func.__name__)
            func()
        return wrapper
    
