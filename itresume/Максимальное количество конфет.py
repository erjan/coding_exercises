'''
Дан массив costs, где на i 
месте стоит стоимость i конфеты. У мальчика есть coins монет, и он хочет 
купить как можно больше конфет. Какое максимальное число конфет мальчик может купить?
'''

class Answer:
    def maxCandies(self, costs, coins):
        
        costs.sort()

        i = 0
        while coins >= 0:
            if costs[i] <= coins:
                coins = coins - costs[i]
            elif costs[i] > coins:
                break
            i += 1
    
        return i
        
