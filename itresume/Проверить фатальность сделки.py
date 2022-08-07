'''
Создайте класс Organization.
В классе опишите атрибут is_opened, который по умолчанию будет равен True, т.е. компания работает.
Создайте метод makeDeal, который принимает на вход параметр isFatal - фатальная сделка или нет. По умолчанию должно быть False.
Внутри метода реализуйте проверку: если isFatal принимает значение True, то атрибут is_opened должен поменяться на False у всех объектов одновременно.
'''

class Organization: 
    is_opened = True
    def makeDeal(self, isFatal=False):
        
        if isFatal:
            Organization.is_opened= False
            
