'''
Напишите декоратор RepeatDecorator, который 
проверяет, запускалась ли ранее обернутая функция с заданными
позиционными аргументами. Если такие аргументы уже подавались на вход данной функции, то нужно 
вывести на экран сообщение: «Функция с такими аргументами уже запускалась!».
'''


class Answer:
    def RepeatDecorator(self, func):
        storage = set()
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key not in storage:
                storage.add(key)
                return func(*args, *kwargs)
            print("func with this args was already called, do nothing")                                        
        return wrapper
