#On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

#The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

#Return the number of pawns the rook can capture in one move.


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        total = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    upper = []
                    print('checking above the rook [%d][%d] until %d' %(i,j, i))
                    for up in range(i):
                        upper.append(board[up][j])
                    lower = []                
                    print("checking below the rook [%d][%d] from %d to %d" %(i,j,i+1, 8))
                    for low in range(i+1,8):
                        lower.append(board[low][j])

                    left = []
                    print('checking to left of the rook: from %d to %d' %(0,j))
                    for left_index in range(j):
                        left.append(board[i][left_index])

                    right = []          
                    print('checking to left from the rook: from %d to %d' %(j+1, 8))
                    for right_index in range(j+1, 8):
                        right.append(board[i][right_index])

                    if len(upper) != 0:
                        if 'p' in upper:
                            if 'B' in upper:
                                b_index = upper.index('B')                                
                                for t in range(len(upper)):
                                    if upper[t] == 'p':
                                        p_index = t                                               
                                if p_index > b_index:
                                    print('p is not blocked by Bishop in upper')
                                    total+=1
                            else:
                                total+=1

                    if len(lower)!= 0:
                        if 'p' in lower:
                            if 'B' in lower:
                                b_index = lower.index('B')
                                p_index = lower.index('p')                                   
                                if p_index < b_index:
                                    print('p is not blocked by Bishop in lower')
                                    total+=1
                            else:
                                total+=1

                    if len(right)!= 0:
                        if 'p' in right:
                            if 'B' in right:
                                b_index = right.index('B')
                                p_index = right.index('p')

                                if p_index < b_index:
                                    print('p is not blocked by Bishop in right')
                                    total+=1
                            else:
                                total+=1

                    if len(left) != 0:
                        if 'p' in left:
                            if 'B' in left:
                                b_index = left.index('B')
                                for t in range(len(left)):
                                    if left[t] == 'p':
                                        p_index = t

                                if p_index > b_index:
                                    print('p is not blocked by Bishop in left')
                                    total+=1
                            else:
                                total+=1

        print('the total pawns edible: %d' % total)
        return total
