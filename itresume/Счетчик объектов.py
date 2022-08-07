
'''
Создайте класс MyClass, в котором будет
определен метод count, возвращающий количество созданных 
экземпляров данного класса. Должна быть предусмотрена возможность
вызывать метод без создания экземпляра класса.
'''

class MyClass():
    total = 0
    def __init__(self):
        MyClass.total+=1
    @classmethod
    def count(cls):
        return cls.total
        
