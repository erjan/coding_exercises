'''
Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 
10000 чисел (не считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

Числа, следующие за числом 0, считывать не нужно.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).

Формат вывода
Выведите ответ на задачу.
'''


if __name__ == "__main__":

    l = list()

    while True:
        x = int(input())
        if x == 0:
            break
        else:
            l.append(x)

    maxi = max(l)
    count = 0
    for i in range(len(l)):
        if l[i] == maxi:
            count += 1
    print(count)
