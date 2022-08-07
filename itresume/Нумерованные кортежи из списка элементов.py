'''
Дан список arr с произвольным 
количеством элементов. Необходимо написать функцию tuple_creator, которая 
вернет список кортежей, каждый из которых будет содержать порядковый номер и элемент 
списка arr. При этом нумерацию нужно начинать не с нуля, а с некоторого заданного числа n.

'''


class Answer:
    def tuple_creator(self, arr, n):
        l = [i for i in range(n, len(arr)+n)]

        res = list(zip(l, arr))
        return res
--------------------------------------------------------
class Answer:
  def tuple_creator(self, arr, n):
    return list(enumerate(arr, start = n))      
        
