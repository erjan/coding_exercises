'''
Дано целое число, состоящее только из цифр 6 и 9. Найти максимальное число, которое можно получить, заменив одну цифру на другую.
'''

class Answer:
    def maximum69Number(self, num):
        
        num = list(str(num))
        
        for i in range(len(num)):
            
            if num[i] == '6':
                num[i] = '9'
                break
                
        num = int(''.join(num))
        return (num)
