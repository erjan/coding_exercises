'''
this is from https://stepik.org/lesson/727588/step/1?thread=solutions&unit=728924

course Добрый, добрый Python ООП - обучающий курс от Сергея Балакирева
'''

size = 10
from random import randint
import random

class Ship:
    def __init__(self, length, tp= None, x=None,y=None):
        self._length = length        
        self._tp = 1 if tp is None else tp
        self._x = x
        self._y = y
        self._is_move=True
        self._cells = [1]*self.length
        
    @property
    def is_sunk(self):
        # What condition using self.cells would tell us the ship is destroyed?
        return all(x == 2 for x in self.cells)
            
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,val):
        self._x = val        
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,val):
        self._y = val     
    @property
    def length(self):
        return self._length
    @property
    def tp(self):
        return self._tp    
    @property
    def is_move(self):
        return self._is_move    
    @property
    def cells(self):
        return self._cells
        
    def __getitem__(self,ind):
        return self.cells[ind]
    def __setitem__(self,ind,val):
        self.cells[ind] = val
          
    def is_out_pole(self,size):
        
        if self.tp == 1: #horiz
            
            lasty = self.y + self.length-1
            lastx = self.x
            
        elif self.tp == 2:#vertic   
            lastx = self.x + self.length-1
            lasty = self.y
            
        return not ((0<=self.x<size) and (0<=self.y<size) and (0<=lastx<size) and(0<=lasty<size))
        
    def get_ship_coords(self):
        coords = []
        if self.tp == 1:
            for j in range(self.y, self.y + self.length):
                coords.append( [self.x,j])

        elif self.tp == 2:
            for i in range(self.x, self.x + self.length):
                coords.append([i, self.y])
        return coords                
                                               
    def is_collide(self,ship):
        s1 = self.get_ship_coords()
        s2 = ship.get_ship_coords()
        
        for x1,y1 in s1:
            for x2,y2 in s2:
                if abs(x1-x2)<=1 and abs(y2-y1)<=1:
                    return True
        return False                

    def can_move(self,go):
        if self._is_move:
            if self.tp == 1:
                oldx = self.x
                self.x = self.x + go

                if self.is_out_pole(size):
                    self.x = oldx
                    return False
                self.x = oldx
                return True
                                
            elif self.tp == 2:
                oldy = self.y
                self.y = self.y + go
                if self.is_out_pole(size):
                    self.y = oldy
                    return False                       
                self.y = oldy
                return True
            
        else:
            return False

    def move(self,go):
        if self.tp == 1:
            self.y += go
        else:
            self.x += go
   
    def set_start_coords(self,x,y):
        self.x = x
        self.y = y
                   
    def get_start_coords(self):
        return tuple([self.x,self.y])
                                 
class GamePole:
    symbols = {
            0: "🟦",  # Пустая вода (синий квадрат)
            1: "\U0001F6A2",  # 1-палубный (белый)
            2: "🟩",  # 2-палубный (зеленый)
            3: "🟨",  # 3-палубный (желтый)
            4: "🟥",  # 4-палубный (красный)
            "hit": "💥", # Попадание
            "miss": "⚪", # Промах
            'dead': '💀'
    }

    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self.field = [ [0 for _ in range(self.size)]for _ in range(self.size)]

    @property
    def size(self):
        return self._size 
           
    @property
    def ships(self):
        return self._ships
    
    @ships.setter
    def ships(self,newval):
        self._ships = newval

    def init(self):
        lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.ships = [Ship(L, tp = randint(1,2)) for L in lengths]
                            
        placed_ships = []
        for ship in self.ships:
            it_placed = False
            while not it_placed:
                x= randint(0,self.size-1)
                y= randint(0,self.size-1)
                ship.set_start_coords(x,y)
                
                if not ship.is_out_pole(self.size) and all( not ship.is_collide(s) for s in placed_ships):
                    it_placed=True
                    placed_ships.append(ship)
                    break
                                
    def show(self):
        view_field = [ row[:] for row in self.field]

        for ship in self.ships:
            c = ship.get_ship_coords()
            for x,y in c:
                idx = c.index([x,y])                
                if ship.cells[idx] == 2:
                    view_field[x][y] = 'hit'
                    if ship.is_sunk:
                        for a,b in c:
                            view_field[a][b] = 'dead'

                
            
        for i in range(self.size):
            for j in range(self.size):
                print(GamePole.symbols[view_field[i][j]], end = ' ')
            print()
        
        print()
                    
    def get_pole(self):
        return tuple( tuple(row) for row in self.field)

    def get_ships(self):
        return self.ships
    
    def move_ships(self):
        for ship in self.ships:
            step = random.choice([-1,1])
            
            oldx ,oldy = ship.x, ship.y
            if ship.can_move(step):
                ship.move(step)
                if any(ship.is_collide(s) for s in self.ships if s is not ship):
                    ship.x ,ship.y = oldx, oldy
                    continue

            if ship.can_move(-step):
                ship.move(-step)
                if any(ship.is_collide(s) for s in self.ships if s is not ship):
                    ship.x ,ship.y = oldx, oldy


    def hit(self,x,y):
        for ship in self.get_ships():
            c = ship.get_ship_coords()

            if [x,y] in c:

                idx = c.index([x,y])
                ship[idx] = 2
                
                print('ship hit!')
                print(ship.cells)
                ship._is_move = False
                self.field[x][y] = 'hit'
                return True
            
        print('miss!')
        self.field[x][y] = 'miss'
        return False

    def is_all_ships_sunk(self):
        return all ( ship.is_sunk for ship in self.get_ships())            

class SeaBattle:

    def __init__(self):
        self.ai_field = GamePole(10)
        self.human_field = GamePole(10)
        self.ai_field.init()
        self.human_field.init()

    def check_game_state(self):
        ai_alive = not self.ai_field.is_all_ships_sunk() 
        human_alive = not self.human_field.is_all_ships_sunk()
        return ai_alive and human_alive

            
    

    def game(self):

        while self.check_game_state():

            print('-------------------------------------------')
            print('human go:')
            a = input('enter coords: x,y: ')
            x,y = list(map(int, a.split()))

            self.ai_field.hit(x,y)
            self.ai_field.show()

            computer_x = randint(0,self.ai_field.size-1)
            computer_y = randint(0,self.ai_field.size-1)

            print('AI GO:')
            print(f'ai fire at {computer_x} {computer_y}')

            self.human_field.hit(computer_x,computer_y)
            self.human_field.show()

            

        if self.ai_field.is_all_ships_sunk():
            print('i human win')
        else:
            print('ai win')

        print('game over!')


q = SeaBattle()

q.game()
