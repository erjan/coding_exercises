'''
Дан текст. Выведите все слова, встречающиеся в тексте, по одному 
на каждую строку. Слова должны быть отсортированы по убыванию их количества 
появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке. 
Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по 
частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами которого 
будут кортежи из двух элементов: частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда 
стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, 
а если они равны — то по второму. Это почти то, что требуется в задаче.
'''


import sys
from collections import Counter

if __name__ == "__main__":
    input_lines = list()
    if len(sys.argv) > 1:

        input_file_name = sys.argv[1]
        with open(input_file_name, 'r') as file:
            input_lines = file.readlines()

    else:
        input_lines = sys.stdin.readlines()

    l = list()
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    l = list()
    for i in range(len(input_lines)):
        cur_list = input_lines[i].split()
        for item in range(len(cur_list)):
            l.append(cur_list[item])

    d = dict()
    for i in range(len(l)):
        word = l[i]
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1

    d2 = Counter(l)

    x = sorted(list(d2.items()))

    x = sorted(
        sorted(x, key=lambda x: x[1], reverse=True), key=lambda x: x[1], reverse=True)

    for item in x:

        print(item[0])
