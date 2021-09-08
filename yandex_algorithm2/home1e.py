'''
На координатной плоскости расположены равнобедренный прямоугольный треугольник ABC с длиной катета d и точка X. Катеты треугольника лежат на осях координат, а вершины расположены в точках: A (0,0), B (d,0), C (0,d).

Напишите программу, которая определяет взаимное расположение точки X и треугольника. Если точка X расположена внутри или на сторонах треугольника, выведите 0. Если же точка находится вне треугольника, выведите номер ближайшей к ней вершины.

Формат ввода
Сначала вводится натуральное число d (не превосходящее 1000), а затем координаты точки X – два целых числа из диапазона от ­–1000 до 1000.

Формат вывода
Если точка лежит внутри, на стороне треугольника или совпадает с одной из вершин, то выведите число 0. Если точка лежит вне треугольника, то выведите номер вершины треугольника, к которой она расположена ближе всего (1 – к вершине A, 2 – к B, 3 – к C). Если точка расположена на одинаковом расстоянии от двух вершин, выведите ту вершину, номер которой меньше.
'''
def distance_btw_points(x1, y1, x, y):
    return ((x1-x)**2 + (y1-y)**2)**0.5


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))/2.0)


def isInside(x1, y1, x2, y2, x3, y3, x, y):

    # Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    A1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    A2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    A3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False


if __name__ == "__main__":
    d = int(input())
    X = list(map(int, input().split()))
    x = X[0]
    y = X[1]

    # vertices check
    if x == 0 and y == 0:
        print('its origin A')
        print(0)
    elif x == 0 and y == d:
        #print('its the top C')
        print(0)
    elif y == 0 and x == d:
        print('its the top B')
        print(0)

    # check if point is on edges:

    elif x == 0 and y < d and d > 0:  # side ac
        print(0)
    elif y == 0 and x < d and d > 0:  # side ab
        print(0)

    # check if x is inside
    elif isInside(0, 0, 0, d, d, 0, x, y):
        print(0)
    else:
        a_to_p = distance_btw_points(0, 0, x, y)
        b_to_p = distance_btw_points(d, 0, x, y)
        c_to_p = distance_btw_points(0, d, x, y)

        if a_to_p < b_to_p and a_to_p < c_to_p:
            print(1)
        elif b_to_p < a_to_p and b_to_p < c_to_p:
            print(2)
        elif c_to_p < a_to_p and c_to_p < b_to_p:
            print(3)

        # when point X is right on middle of hypotenuse
        # elif c_to_p == b_to_p and b_to_p and a_to_p == b_to_p:
         #   print(1)

        # when point X is above but equidistant from B and C - return 2, cuz B = 2, C = 3
        elif c_to_p == b_to_p and c_to_p != a_to_p:
            print(2)
        elif a_to_p == b_to_p and a_to_p != c_to_p:
            print(1)
        elif a_to_p == c_to_p and a_to_p != b_to_p:
            print(1)
