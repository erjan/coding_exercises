'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.
'''

class Solution:         # States for the dominoes:
                        #   • Any triplet that reaches the state 'R.L' remains
                        #     that state permanently.
                        #  
                        #   • These changes occur to pairs that are not part of an 'R.L':
                        #     'R.' --> 'RR', .L' --> 'LL'

                        #  Here's the plan:
                        #    1) To avoid the problem with the 'R.L' state when we  address the 
						#       'R.' --> 'RR' and  '.L' --> 'LL' changes, we replace each 'R.L' 
						#.       with a dummy string (say, 'xxx').
                        #       
                        #    2) We perform the 'R.' --> 'RR', .L' --> 'LL' replacements.

                        #    3) Once the actions described in 1) and 2) are completed, we repeat 
                        #       until no changes occur. We replace the dummy string with 'R.L'. 
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return  dominoes.replace('xxx', 'R.L')              # <-- 3)
