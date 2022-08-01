'''
Дана строка s, состоящая только из букв английского алфавита в нижнем регистре. Необходимо полностью удалить все соседние повторяющиеся буквы и вернуть результирующю строку.

Примечание. После удаления дубликатов могут возникнуть новые. Удалять дубликаты необходимо до тех пор, пока не будут удалены все повторяющиеся соседние буквы.
'''

class Answer:
    def removeDuplicates(self, S):
        s = S
        s = list(s)
        stack = []

        for c in s:

                # if the prev charac is same as before, we need to pop it, the current same char is iterated over as usual
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        res = ''.join(stack)
        print(res)
        return res
