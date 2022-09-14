'''
A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in three ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return

1 if the mouse wins the game,
2 if the cat wins the game, or
0 if the game is a draw.
'''

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @functools.lru_cache(maxsize=None)
        def move(mouse, cat, turn):
            if turn >= len(graph)*2: return 0
            if turn % 2:
                ans = 2
                for position in graph[mouse]:
                    if position == cat: continue
                    if position == 0: return 1
                    result = move(position, cat, turn+1)
                    if result == 1: return 1
                    if result == 0: ans=0
                return ans
            else:
                ans = 1
                for position in graph[cat]:
                    if position == 0: continue
                    if position == mouse: return 2
                    result = move(mouse, position, turn+1)
                    if result == 2: return 2
                    if result == 0: ans = 0
                return ans
        return move(1,2,1)
