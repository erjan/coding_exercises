'''
Создайте класс MyInt, который
будет наследоваться от стандартных целых чисел Python. Единственное отличие 
этого класса должно заключаться в том, что при вызове функции print будет выводиться 
не просто значение числа, а строка:
'''

class MyInt(int):
    
    def __repr__(self):
        return "Значение: %d" % int(self)
    
