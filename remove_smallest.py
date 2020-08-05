'''
Вам дан массив a, состоящий из n положительных (больших нуля) целых чисел.

За один ход вы можете выбрать два индекса i и j (i≠j) таких, что абсолютная разность между ai и aj не превосходит единицу (|ai−aj|≤1), и удалить наименьший из этих двух элементов. Если два элемента равны, вы можете удалить любой из них (но только один).

Ваша задача — определить, возможно ли получить массив, состоящий только из одного элемента, применив несколько (возможно, ноль) таких ходов, или нет.

Вам нужно ответить на t независимых наборов тестовых данных.

Входные данные
Первая строка теста содержит одно целое число t (1≤t≤1000) — количество наборов тестовых данных. Затем следуют t наборов тестовых данных.

Первая строка набора тестовых данных содержит одно целое число n (1≤n≤50) — длину a. Вторая строка набора тестовых данных содержит n целых чисел a1,a2,…,an (1≤ai≤100), где ai — i-й элемент a.

Выходные данные
Для каждого набора тестовых данных выведите ответ на него: «YES», если возможно получить массив, состоящий только из одного элемента, применив несколько (возможно, ноль) ходов, описанных в условии задачи, или «NO» в обратном случае.
'''

def helper(a):
    if len(a) == 1:
        print('YES')
    else:    
        a.sort()
        status = True
        for i in range(1, len(a)):
            if abs(a[i] - a[i-1]) > 1:
                status = False
                break
        print('YES' if status else 'NO')
                
   
if __name__ == '__main__':
    
    big_n = int(input())
    for _ in range(big_n):
        
        l = int(input())
        row = [ int(x) for x in input().split(' ')]
        helper(row)
