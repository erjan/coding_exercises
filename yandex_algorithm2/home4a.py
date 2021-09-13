'''
Толя-Карп запросил для себя n посылок с «Аллигатор-экспресс».

Посылка представляет из себя ящик. Внутри ящика лежит целое число ai. Номер на ящике di указывает на цвет числа, лежащего внутри.

Толю-Карпа интересует, чему будут равны значения чисел, если сложить между собой все те, что имеют одинаковый цвет. Напишите, пожалуйста, программу, которая выводит результат.
'''


if __name__ == "__main__":
    n = int(input())

    d = dict()
    for _ in range(n):
        current = list(map(int, input().split()))
        color_num = current[0]
        cur = current[1]

        if color_num not in d.keys():
            d[color_num] = cur
        else:
            d[color_num] += cur

    d = d.items()
    sorted_d = list(sorted(d))
    for item in sorted_d:
        for j in item:
            print(j, end=' ')
        print()
