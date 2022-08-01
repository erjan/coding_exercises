'''
Дан кортеж init, целое число ind 
и кортеж add. Необходимо написать функцию tuplex, которая позволит 
вставить элементы кортежа add в кортеж init, начиная с позиции ind и вывести получившийся кортеж.
'''

class Answer:
    def tuplex(self, init, ind, add):
        init = list(init)

        for i in range(len(init)):

            if i == ind:
                cur = i
                for j in range(len(add)):
                    init.insert(cur, add[j])
                cur += 1
    
        init = tuple(init)
        return init
