'''
Enter a positive integer 'N'. You need to return a list of strings as shown in the Example.
'''


class Solution:
    """
    @param n: An integer.
    @return: A string list.
    """
    def print_x(self, n: int) -> List[str]:

        A = [[''] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j or i == n-j-1:
                    A[i][j] = 'X'
                else:
                    A[i][j] = ' '
        return [''.join(i) for i in A]
