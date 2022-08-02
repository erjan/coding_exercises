'''
Вы играете в компьютерную игру, где нужно перемещаться по облакам. Но не все так просто - облака бывают двух видов:

обычные облачка
грозовые тучи
Перемещаться можно только по облачкам - наступать на грозовые тучи нельзя. Можно делать либо один шаг, либо перепрыгивать через 1.

Облака представлены в виде последовательного массива чисел. 0 - значит облако, 1 - грозовая туча
'''

class Answer:
    def jumpingOnClouds(self, clouds):
        # введите свой код ниже
        
        i = 0
        res = 0
        while i < len(clouds):
            if i < len(clouds)-2 and clouds[i+2] == 0:
                i+=2
            else:
                i+=1
            res+=1
                   

        return res -1

    
#alternative solution

class Answer:
    def jumpingOnClouds(self, clouds):       
        
        i = 0
        jumps = 0
        
        while(i < len(clouds)-1):
            if clouds[i+2] == 0: 
                jumps+=1
                i += 2
            elif clouds[i+1] == 0: 
                jumps+=1
                i += 1
        return jumps
    
#recursive

class Answer:
    def jumpingOnClouds(self, clouds):
        
        if len(clouds) == 1:
            return 0
        if len(clouds) == 2:
            if clouds[1] == 1:
                return 0
            else:
                return 1
        if clouds[2] == 1:
            return 1 + self.jumpingOnClouds(clouds[1:])
        if clouds[2] == 0:
            return 1 + self.jumpingOnClouds(clouds[2:])


