'''
You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.
'''


class Solution:
    def cleanRoom(self, robot):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cleaned = set()
        def dfs(robot, x, y, direction):
            if (x, y) in cleaned:
                return
            robot.clean()
            cleaned.add((x, y))
            for i, (dx, dy) in enumerate(directions[direction:] + directions[:direction]):
                nx = x + dx
                ny = y + dy
                if robot.move():
                    dfs(robot, nx, ny, (direction + i) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                else:    
                    robot.turnRight()
        dfs(robot, 0, 0, 0) 
        
---------------------------------------------------------------------

I let the robot always facing the north, and wrote 4 functions to make it move to upward, left, right, and downward, yet still facing the north. (I know, I was just trying to save my brain)

And, then it became a pretty normal DFS problem, I named the start point as (0, 0), and everything becomes clear.

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.robot.clean()
        self.visited = [(0,0)]
        self.dfs(0, 0)
    
    def dfs(self, x, y):
        if (x-1, y) not in self.visited and self.up():
            self.robot.clean()
            self.visited.append((x-1, y))
            self.dfs(x-1, y)
            self.down()
        if (x, y-1) not in self.visited and self.left():
            self.robot.clean()
            self.visited.append((x, y-1))
            self.dfs(x, y-1)
            self.right()
        if (x+1, y) not in self.visited and self.down():
            self.robot.clean()
            self.visited.append((x+1, y))
            self.dfs(x+1, y)
            self.up()
        if (x, y+1) not in self.visited and self.right():
            self.robot.clean()
            self.visited.append((x, y+1))
            self.dfs(x, y+1)
            self.left()
        
    
    def up(self):
        return self.robot.move()
        
    def left(self):
        self.robot.turnLeft()
        result = self.robot.move()
        self.robot.turnRight()
        return result
        
    def right(self):
        self.robot.turnRight()
        result = self.robot.move()
        self.robot.turnLeft()
        return result
        
    def down(self):
        self.robot.turnLeft()
        self.robot.turnLeft()
        result = self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
        return result
---------------------------------------------------------------------


import enum
from collections import defaultdict
from functools import lru_cache
from typing import List, Optional, Tuple
from collections import deque
from itertools import cycle, tee


class Direction(enum.Enum):
    Up = (-1, 0)
    Right = (0, 1)
    Down = (1, 0)
    Left = (0, -1)

    @lru_cache(maxsize=None)
    def num_right_rotations(self, other: 'Direction') -> int:
        if self == other:
            return 0

        it = iter(cycle(Direction))
        while True:
            if self == next(it):
                break

        for (i, direction) in enumerate(it, 1):
            if direction == other:
                return i

        raise ValueError(f'{other} is not a valid direction')

    @lru_cache(maxsize=None)
    def num_left_rotations(self, other: 'Direction') -> int:
        if self == other:
            return 0
        return 4 - self.num_right_rotations(other)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



class Status:
    Unknown = 0
    Visited = 1
    Cleaned = 2
    Blocked = 3


class Solution:
    def __init__(self):
        self.graph = defaultdict(set)
        self.row = 0
        self.col = 0
        self.direction = Direction.Up
        self.robot: 'Optional[Robot]' = None
        self.statuses = defaultdict(lambda: Status.Unknown)
        self.unreachable = set([])

    def add_surroundings(self):
        current_position = (self.row, self.col)
        if current_position not in self.statuses:
            self.statuses[current_position] = Status.Unknown

        for direction in Direction:
            neighbor = (current_position[0] + direction.value[0], current_position[1] + direction.value[1])

            if neighbor not in self.statuses:
                self.statuses[neighbor] = Status.Unknown
            elif self.statuses[neighbor] == Status.Blocked:
                continue

            self.graph[current_position].add(neighbor)
            self.graph[neighbor].add(current_position)

    def clean_cell(self):
        self.robot.clean()
        self.statuses[(self.row, self.col)] = Status.Cleaned

    def go(self, direction: Direction):
        self.orient(direction)

        has_moved = self.robot.move()
        row, col = self.row + direction.value[0], self.col + direction.value[1]
        if has_moved:
            self.row, self.col = row, col
            self.statuses[(self.row, self.col)] = Status.Visited
        return has_moved, (row, col)

    def orient(self, direction: Direction):
        if direction == self.direction:
            return

        num_left_rotations = self.direction.num_left_rotations(direction)
        num_right_rotations = self.direction.num_right_rotations(direction)

        if num_left_rotations < num_right_rotations:
            for _ in range(num_left_rotations):
                self.robot.turnLeft()
        else:
            for _ in range(num_right_rotations):
                self.robot.turnRight()

        self.direction = direction

    def find_path_to_closest_unknown(self, src):
        queue = deque([src])
        visited = {src}

        edge_to = {}

        dst = None

        while queue:
            vertex = queue.popleft()

            if self.statuses[vertex] == Status.Unknown:
                dst = vertex
                break

            # we sort the neighbors by the visited status, we need them first
            for neighbor in sorted(self.graph[vertex], key=lambda x: (self.statuses[x], x)):
                if neighbor in visited:
                    continue

                if self.statuses[neighbor] == Status.Blocked:
                    continue

                edge_to[neighbor] = vertex
                visited.add(neighbor)
                queue.append(neighbor)

        if dst is None:
            return None

        path = []
        current = dst
        while current != src:
            path.append(current)
            current = edge_to[current]

        path.append(src)

        return list(reversed(path))

    @staticmethod
    def translate_path_to_directions(path: List[Tuple[int, int]]) -> List[Direction]:
        if len(path) <= 1:
            yield None
            return

        for prev, nxt in prev_next(path):
            if prev == nxt:
                yield None
                continue

            diff = (nxt[0] - prev[0], nxt[1] - prev[1])
            yield Direction(diff)

    def remove_blocked(self, vertex: Tuple[int, int]):
        del self.graph[vertex]
        self.statuses[vertex] = Status.Blocked

    def cleanRoom(self, robot: 'Robot'):
        self.robot = robot

        while path := self.find_path_to_closest_unknown((self.row, self.col)):
            directions = self.translate_path_to_directions(path)
            # print(f'Position: ({self.row}, {self.col}), path: {path}, directions: {directions}')

            for direction in directions:
                if self.statuses[(self.row, self.col)] != Status.Cleaned:
                    self.clean_cell()

                if direction is not None:
                    has_moved, next_coord = self.go(direction)
                    if not has_moved:
                        self.remove_blocked(next_coord)
                        break

                self.add_surroundings()


def prev_next(t):
    cur, nxt = tee(t)
    next(nxt)
    return zip(cur, nxt)
Robot API implementation for testing purposes with render decorator

def render(method):
    cleaned = ' '
    dirty = '·'
    wall = '█'

    import os
    from time import sleep

    def wrapper(*args, **kwargs):
        operation = method.__name__
        self = args[0]

        def render_top_line():
            print(' ', end='')
            for r in range(self.num_cols):
                print('▁', end='')
            print()

        def render_bottom_line():
            print(' ', end='')
            for r in range(self.num_cols):
                print('▔', end='')
            print()

        def get_direction():
            match self.direction:
                case Direction.Up:
                    return '▲'
                case Direction.Right:
                    return '▶'
                case Direction.Down:
                    return '▼'
                case Direction.Left:
                    return '◀'

        def render_matrix():
            for row in range(self.num_rows):
                print('▕', end='')
                for col in range(self.num_cols):
                    element = dirty
                    if self.cleaned_matrix[row][col]:
                        element = cleaned

                    if self.room[row][col] == 0:
                        element = wall

                    if col == self.col and row == self.row:
                        element = get_direction()

                    print(element, end='')

                print('▏', end='\n')

        def render_num_operations():
            print(f'{self.num_operations}'.ljust(4), f'{operation}'.ljust(20))
            self.num_operations += 1

        result = method(*args, **kwargs)

        os.system('clear')

        render_num_operations()
        render_top_line()
        render_matrix()
        render_bottom_line()

        print()

        sleep(0.1)

        return result

    return wrapper


class Robot:
    def __init__(self, room: 'List[List[int]]', row: int, col: int) -> None:
        self.room = room
        self.row = row
        self.col = col
        self.direction = Direction.Up

        self.num_rows = len(room)
        self.num_cols = len(room[0])

        self.num_operations = 0

        self.cleaned_matrix = [
            [True for _ in range(self.num_cols)]
            for _ in range(self.num_rows)
        ]

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if room[r][c] == 1:
                    self.cleaned_matrix[r][c] = False

    @render
    def move(self) -> bool:
        dr, dc = self.direction.value
        row, col = self.row + dr, self.col + dc
        if row >= self.num_rows or row < 0 or col >= self.num_cols or col < 0:
            return False

        if self.room[row][col] == 0:
            return False

        self.row, self.col = row, col
        return True

    @render
    def turnLeft(self):
        self.direction = Direction((-self.direction.value[1], self.direction.value[0]))

    @render
    def turnRight(self):
        self.direction = Direction((self.direction.value[1], -self.direction.value[0]))

    @render
    def clean(self):
        self.cleaned_matrix[self.row][self.col] = True
        
-----------------------------------------------------

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        loc = 0,0
        v = set()
        direct = 0 # 0: up 1: right 2: down 3: left
        movement = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def back(robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def helper(loc: tuple, v: Set[tuple], direct: int, robot):
            robot.clean()
            v.add(loc)
            for i in range(4):
                new_direct = (direct+i)%4
                new_loc = loc[0]+movement[new_direct][0], loc[1]+movement[new_direct][1]
                if new_loc not in v and robot.move():
                    helper(new_loc, v, new_direct, robot)
                    back(robot)
                else:
                    v.add(new_loc)
                robot.turnRight()
            
        helper(loc, v, direct, robot)
----------------------------------------------------------------

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def dfs(i, j, di, dj):
            visited.add((i,j))
            robot.clean()
            for _ in range(4):
                x, y = i + di, j + dj
                if (x, y) not in visited:
                    canMove = robot.move()
                    if not canMove:
                        visited.add((x, y))
                    else:
                        dfs(x, y, di, dj)
                        robot.turnRight()
                        robot.turnRight()
                        robot.move()
                        robot.turnLeft()
                        robot.turnLeft()
                di, dj = dj, -di
                robot.turnRight()
            
        visited = set()
        dfs(0, 0, 0, 1)
--------------------------------------------------------------

Without the Robot API settings, it's a kind of regular DFS problem. So we can build our solution based on DFS.
The tricky things are, how to we make our robot object search all four directions without missing, and get back to original place after our recursive call. We can't just input a coordinate (i, j) to our robot. We need to manually set the direction for it and move one step a time.

An idea is search left side once first, and then search right side three times. In such way, after a DFS, robot will search all four directions and heads to the opposite direction against where it came from. Then, we have it move extra one unit and it can go back to where it came from, like a recursive DFS return.

And we also need to pass current direction down to next DFS so we can calculate the direction sequence in next DFS. It's like (d+k) % 4 for k in (3,0,1,2) where d is original direction and k is the turn. k iterates as (3,0,1,2) because we turn left first and then turn right 3 times.

Another thing should be taken care is that after we DFS one path and get back to original place, we need to continue our DFS in current place. And since our direction has been reversed, we should turn left instead of right otherwise two direction would be missed.
E.g. Robot reaches point X and heads N (so it comes from S). In current DFS, it turns left first and heads W to DFS. After that sub DFS, it gets back to X and heads E (not W). If it turns right, it will return to S and N and E will be missed. So it should turn left to visit N, then E and return to S.

	N
	
W   X   E

	S
It will be clearer if you make a draft.
So each time we have done a sub DFS, we reset the "turn left once first and then turn right" pattern.

def cleanRoom(robot):
	def dfs(robot, i, j, d, cleaned):
		robot.clean()
		cleaned.add((i,j))
		left = True
		for nd in ((d+k) % 4 for k in (3,0,1,2)):
			robot.turnLeft() if left else robot.turnRight()
			di, dj = ((-1,0),(0,1),(1,0),(0,-1))[nd]
			if (i+di, j+dj) not in cleaned and robot.move():
				dfs(robot, i+di, j+dj, nd, cleaned)
				robot.move()
				left = True
			else:
				left = False
	dfs(robot, 0, 0, 0, set())
  
      
