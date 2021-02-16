# последнее задание из курса степик "Как добиться успеха, решая задачки на Степике" - 6 правил
import unittest
from math import modf
import sys

import fileinput


rule1 = '1. Делать только то, что хочется.'
rule2 = '2. Не делать того, что делать не хочется.'
rule3 = '3. Сразу говорить о том, что не нравится.'
rule4 = '4. Не отвечать, когда не спрашивают.'
rule5 = '5. Отвечать только на вопрос.'
rule6 = '6. Выясняя отношения, говорить только о себе.'


def print_rule(n):
    if n == 1:
        print(rule1)
    elif n == 2:
        print(rule2)
    elif n == 3:
        print(rule3)
    elif n == 4:
        print(rule4)
    elif n == 5:
        print(rule5)
    elif n == 6:
        print(rule6)


def print_all():
    print(rule1)
    print(rule2)
    print(rule3)
    print(rule4)
    print(rule5)
    print(rule6)


def get_num(s):
    try:
        saved = s
        s = int(s)

        if s == 0:
            print_all()

        elif s in [1, 2, 3, 4, 5, 6]:
            print_rule(s)
        elif s < 1 or s > 6:
            # print('just returning some ')
            print(saved)
    except ValueError:
        try:
            # print('trying float...')
            # saved = s
            s = float(s)
            if s == 0:
                print_all()
            elif s < 1 or s > 6:
                print(saved)

            else:
                s = float(s)
                s = check_float(s)
                if s == 0:
                    # print('case zero..')
                    print_all()
                elif s in [1, 2, 3, 4, 5, 6]:
                    print_rule(s)
                else:
                    print(saved)

        except ValueError:
            print(saved)


def check_float(n):
    frac, _ = modf(n)
    if frac != 0:
        return n
    else:
        return n


def test():

    d = input().strip().split()

    for item in d:
        get_num(item)

def test2():

    for line in fileinput.input():
        line = line.strip().split()

        for item in line:
            get_num(item)


if __name__ == "__main__":
    test2()

