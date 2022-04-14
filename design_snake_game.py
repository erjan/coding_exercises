'''
Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

Implement the SnakeGame class:

SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.
'''

Used list as a queue to store all the positions of the snake.
Edge cases:

Snake head tries to move in a position which is occupied by it's body. If this position is tail's position, then ok, otherwise game over
Snake goes out of screen boundary
If it's not a game over, then the position is correct. Insert it in the front of the queue.

If this position has food, then lenghth of the snake increases. So don't remove the tail position
If no food in this position, then snake moves to this position and the tail leaves it's position by using pop()
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.positions:List[List[int]] = [[0,0]] #this will act like a queue for the snake body. It always starts from 0,0        
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.positions[0]        #We find the next position where head of the snake moves. Head is always first in the queue
        
        if direction == 'U':            
            newHead = [head[0] - 1, head[1]]
        elif direction == 'D':
            newHead = [head[0] + 1, head[1]]
        elif direction == 'L':
            newHead = [head[0], head[1] - 1]
        elif direction == 'R':
            newHead = [head[0], head[1] + 1]
                
        if self.positions and newHead in self.positions:    #If next location is already occupied by its body and that part is before tail, then it bites itself and it's a game over
            if self.positions[-1] != newHead:
                return -1
        
        if newHead[0] == -1 or newHead[0] == self.height or newHead[1] == -1 or newHead[1] == self.width:
            return -1                                   #If snake head crosses the screen boundary, game over
        
        self.positions.insert(0, newHead)               #If snake didn't kill itself, then it's good to move to new location
        if self.food and newHead == self.food[0]:       #Now check if the new position is where food is found
            self.food.pop(0)                            #If food is found, remove the food from the positions
            self.score += 1
        else:        
            self.positions.pop()                        #If food not found, then the length of snake didn't increase and hence tail will move forward
        
        return self.score
      
      ------------------------------------------------------------
      class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.foodIndex=0
        self.snake=collections.deque() #A queue as the snake
        self.snake.append((0,0))
        self.body={(0,0)} #A set to keep all positions of the snake
        self.foods=food
        self.width=width
        self.height=height
        self.moves={'U':(0,-1),'L':(-1,0),'R':(1,0),'D':(0,1)}


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        tail=self.snake.popleft() #pop out the tail
        self.body.remove(tail)
        if not self.snake:
            head=tail
        else:
            head=self.snake[-1]
        xm,ym=self.moves[direction]
        nx,ny=head[0]+xm,head[1]+ym
        if (nx,ny) in self.body or nx<0 or nx>=self.width or ny<0 or ny>=self.height:
            return -1
        self.snake.append((nx,ny)) #append the new head
        self.body.add((nx,ny))
        if self.foodIndex<len(self.foods) and nx==self.foods[self.foodIndex][1] and ny==self.foods[self.foodIndex][0]:
            self.foodIndex+=1
            self.snake.appendleft(tail)
            self.body.add(tail)
        #Add back the tail if the snake eat a food
        return len(self.snake)-1
