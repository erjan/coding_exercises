'''
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. 
Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

Формат ввода
Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август. 
Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами. После каждой строки с вопросом идет ответ Августа: YES или NO. Наконец, последняя строка входных данных содержит одно слово HELP.

Формат вывода
Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.
'''


import sys


def read_input(n):
    all_lines = list()
    n = 0
    if len(sys.argv) > 1:

        input_file_name = sys.argv[1]
        with open(input_file_name, 'r') as file:
            n = file.readline()
            n = int(n)
            s = set(i for i in range(1, n+1))

            all_lines = file.readlines()
            for i in range(len(all_lines)):
                all_lines[i] = all_lines[i].strip()
    else:

        all_lines = sys.stdin.readlines()
        n = all_lines[0]
        s = set(i for i in range(1, n+1))

        all_lines = all_lines[1:]
        for line in all_lines:
            print(line)


def solve(all_lines, s):
    for i in range(len(all_lines)):
        cur_item = all_lines[i]
        if cur_item == 'HELP':
            break
        elif cur_item not in ('YES', 'NO'):
            beatris = set(map(int, cur_item.split()))
        elif cur_item == 'YES':
            s.intersection_update(beatris)
        elif cur_item == 'NO':
            for i in beatris:
                if i in s:
                    s.remove(i)

    s = sorted(s)
    s = [str(i) for i in s]
    print(' '.join(s))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        #print('reading from file - cuz arg is given')

        input_file_name = sys.argv[1]
        with open(input_file_name, 'r') as file:
            n = file.readline()
            n = int(n)
            s = set(i for i in range(1, n+1))

            all_lines = file.readlines()
            for i in range(len(all_lines)):
                all_lines[i] = all_lines[i].strip()
        #print('all input')
        # print(all_lines)

    else:
        #print(' no file given - reading from std input')

        n = int(sys.stdin.readline())
        #n = int(all_lines[0])
        s = set(i for i in range(1, n+1))

        all_lines = sys.stdin.readlines()
        for i in range(len(all_lines)):
            all_lines[i] = all_lines[i].strip()

    solve(all_lines, s)
