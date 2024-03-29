'''
Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата. На практике, все выборщики от штата голосуют в соответствии с результами голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число голосов. Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом. Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов.

Формат ввода
Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса выборщики этого штата, затем через пробел идет количество выборщиков, отдавших голоса за этого кандидата.

Формат вывода
Выведите фамилии всех кандидатов в лексикографическом порядке, затем, через пробел, количество отданных за них голосов.
'''

import sys

if __name__ == "__main__":

    d = dict()
    lines = sys.stdin.readlines()
    for line in lines:
        i = line.split()
     
        candidate = i[0]
        votes = int(i[1])

        if candidate not in d.keys():
            d[candidate] = votes
        else:
            d[candidate] += votes

    sorted_d = sorted(d.items())
    sorted_d = list(map(list, sorted_d))
    for item in sorted_d:
        for name in item:
            print(name, end=' ')
        print()
