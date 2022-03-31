'''

You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend 
take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string currentState after one valid move. You may 
return the answer in any order. If there is no valid move, return an empty list [].
'''


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        s = list(currentState)
        moves = list()
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1] == '+':
                s[i] = s[i+1] = '-'
                moves.append(''.join(s))
                s[i] = s[i+1] = '+'
            i += 1
        print(moves)
        return moves
