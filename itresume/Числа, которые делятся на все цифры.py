'''
Вам задана левая и 
правая граница числовой последовательности. Найти 
все числа, которые делятся без остатка на каждую цифру, из которых 
это число состоит. Само собой, в записи числа не должно быть нулей.
'''

class Answer:
    def selfDividingNumbers(self, left, right):
        res = list()
        for i in range(left, right+1):
            print('checking number %d' % i)
            print()
            s = str(i)
            if '0' in s:
                print('no div by zero! ' + s)
                print
                continue
            else:
                print('******************')
                print('check every digit in %s' % s)
                num = int(s)
                div = True
                for i in range(len(s)):
                    print('cur digit %d' % int(s[i]))
                    if num % int(s[i]) != 0:
                        print('num %d is not div by %d' % (num, int(s[i])))
                        div = False
                if div:
                    print('number %d added ' % num)
                    res.append(num)

        print('final result:')
        print(res)
        return res
        
-------------------------------------------------------------------------------------------------
def f(left, right):
    res = list()
    for i in range(left, right+1):
        s = str(i)
        if '0' in s:
            
            continue
        else:
            num = int(s)
            div = True
            for i in range(len(s)):
                if num % int(s[i]) != 0:
                    div = False
            if div:
                res.append(num)

    return res
