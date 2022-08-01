'''
На вход подается массив arr состоящий из 
произвольного количества кортежей, в каждом из которых 
также содержится произвольное количество элементов. Необходимо написать фукнцию flat, которая будет возвращать список из всех элементов, входящих в состав каждого кортежа.
'''


import itertools

class Answer:
    def flat(self, arr):
        
        return list(itertools.chain(*arr))
      
---------------------------------

class Answer:
    def flat(self, arr):
        
        new_foods = []
        for sublist in arr:
	        for food in sublist:
		        new_foods.append(food)

        return (new_foods)
      
--------------------------------------------
class Answer:
    def flat(self, arr):
        
        new_foods = [food for sublist in arr for food in sublist]
        return (new_foods)
