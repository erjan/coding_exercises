'''
Создать декоратор SedativeDecorator, который будет запускать задекорированную функцию и выполнять одно из действий:

Если функция выполнилась без ошибок, то возвращать строку "Все ок"
Если во время выполнения фукнции возникла ошибка, то возвращать строковое представление ошибки
'''


class Answer:
    def SedativeDecorator(self,func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                return 'Все ок'
                    
            except Exception as exc:
                
                return repr(exc)
        return wrapper
                
                    
            
            
            
            
        return wrapper
