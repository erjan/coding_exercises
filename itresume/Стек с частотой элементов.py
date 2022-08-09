'''
Реализуйте класс FreqStack:

FreqStack() должен создавать пустой стек
push(value) добавляет значение value (типа int) в конец стека, этот метод ничего не возвращает
pop() извлекает из стека самый часто встречающийся элемент и удаляет его из стека
get() возвращает список всех элементов
'''


class FreqStack:
    def __init__(self):
        self.obj = []
        self.dict = {}
    def push(self, value):
        self.dict[value] = self.dict.get(value, 0) + 1
        self.obj.append(value)
    def pop(self):
        if self.dict == {}:
            return None
        dic_items = list(self.dict.items())
        max_frq = max([x[1] for x in dic_items])
        part_obj = []
        while self.obj:
            pop_item = self.obj.pop()
            if self.dict[pop_item] == max_frq:
                self.dict[pop_item] -= 1
                self.obj += part_obj
                return pop_item
            else:
                part_obj = [pop_item, ] + part_obj
    def get(self):
        return self.obj
