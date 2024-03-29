'''
Как известно, два наиболее распространённых формата записи даты — это европейский (сначала день, потом месяц, потом год) и американски (сначала месяц, потом день, потом год). Системный администратор поменял дату на одном из бэкапов и сейчас хочет вернуть дату обратно. Но он не проверил, в каком формате дата используется в системе. Может ли он обойтись без этой информации?
Иначе говоря, вам даётся запись некоторой корректной даты. Требуется выяснить, однозначно ли по этой записи определяется дата даже без дополнительной информации о формате.

Формат ввода
Первая строка входных данных содержит три целых числа — 
x
, 
y
 и 
z
 (
1
≤
x
≤
3
1
, 
1
≤
y
≤
3
1
, 
1
9
7
0
≤
z
≤
2
0
6
9
. Гарантируется, что хотя бы в одном формате запись 
x
y
z
 задаёт корректную дату.
Формат вывода
Выведите 1, если дата определяется однозначно, и 0 в противном случае.
'''

def helper(l):
    first = l[0]
    second = l[1]

    if first == second:
        return 1
    if first <= 12 and second <= 12:
        return 0
    elif first > 12 and second <= 12:
        return 1
    elif first <= 12 and second > 12:
        return 1
    else:
        return 0


if __name__ == "__main__":
    l = list(map(int, input().split()))
    result = helper(l)
    print(result)
