'''

Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.
However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.

'''

The problem asked to count the number of unique path in a graph. So we can use DFS here.

The start node and end node can be any number. The number of nodes in the path is in a range of [m, n]. And any number can be the next node as long as it's not a used node and it doesn‘t cross over an unused node.
e.g. 2 is between 1 and 3. Edge (1,3), which crosses over 2, is valid only if 2 has been used.

Thus, I predifined all cross-over edges and the nodes they cross over, and set up an array usedto record all used nodes. As for [m, n] limit, I pass a variable k which records the remaining number of nodes I can used in DFS.

Besides, due to symmetry, number of unique path starting from {1,3,7,9} are the same. Number of unique path starting from {2,4,6,8} are also the same. So we just need to multiply the result by 4.


def numberOfPatterns(m, n):
	cross = collections.Counter({(1,3):2,(3,1):2,(1,7):4,(7,1):4,(3,9):6,(9,3):6,(7,9):8,(9,7):8,(1,9):5,(9,1):5,(2,8):5,(8,2):5,(3,7):5,(7,3):5,(4,6):5,(6,4):5})
	used = [True]+[False]*9
	def dfs(i, k):
		if not k: return 1
		used[i] = True
		cnt = sum(dfs(j, k-1) for j in range(1,10) if not used[j] and used[cross[i,j]])
		used[i] = False
		return cnt
	return sum(dfs(1,k)*4 + dfs(2,k)*4 + dfs(5,k) for k in range(m-1, n))



------------------------------

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def validate(prev, num, seen):
            if prev == -1:
                return True

            if prev == num:
                return False
            
            if seen[num]:
                return False

            row1, col1 = prev // 3, prev % 3
            row2, col2 = num // 3, num % 3
            
            if (row2-row1) & 1 == 0 and (col2-col1) & 1 == 0:
                row = (row2==row1)*row1+(row2!=row1) # if row2 != row1, row must be 1
                col = (col2==col1)*col1+(col2!=col1) # if col2 != col1, col must be 1
                return seen[row*3+col]
            return True

        @cache # if `seen` and `prev` are the same, the result is the same.
        def generate(prev, size, seen):
            count = 0
            if n >= size >= m:
                count += 1
                if size == n:
                    return count

            next_seen = list(seen)
            for i in range(9):
                if not validate(prev, i, seen):
                    continue

                next_seen[i] = True
                
                count += generate(i, size+1, tuple(next_seen))
                
                next_seen[i] = False
            
            return count

        return generate(-1, 0, tuple([False]*9))
