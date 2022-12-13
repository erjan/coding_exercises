'''
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].
'''

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)-1
        self.board = [[int(_) if _.isdigit() else _ for _ in x] for x in board]
        self.board[n][n] = 0
        self.board[0][0] = 0
        self.scores = [[0 for _ in range(n+2)] for x in range(n+2)]
        self.counts = [[0 for _ in range(n+2)] for x in range(n+2)]
        self.counts[n][n] = 1
        for i in range(n, -1, -1):
            for j in range(n, -1, -1):
                if self.board[i][j] == 'X':
                    continue
                highest_score = max(self.scores[i+1][j],
                            self.scores[i+1][j+1],
                            self.scores[i][j+1])
                score = highest_score + self.board[i][j]
                self.scores[i][j] = score
                
                for i_x, j_x in [[i+1, j], [i+1, j+1], [i, j+1]]:
                    if self.scores[i_x][j_x] == highest_score:
                        self.counts[i][j] += self.counts[i_x][j_x]
        
        if self.counts[0][0] == 0:
            return [0, 0]
        else:
            return [self.scores[0][0], self.counts[0][0] % (10**9+7)]
          
          
