'''
Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

 
 '''

class Solution:
    def solveEquation(self, equation):
        def evaluate(expr):
            coeff, const = 0, 0
            groups = expr.split('+')
            for group in groups:
                terms = group.split('-') if '-' in group else [group]
                negate = 1 # the first term in terms is not negated 
                for term in terms:
                    if term:
                        if term[-1] == 'x':
                            coeff += negate * (int(term[:-1]) if term[:-1] else 1)
                        else:
                            const += negate * int(term)
                    negate = -1
            return coeff, const
            
        left, right = equation.split('=')
        coeff_left, const_left = evaluate(left)
        coeff_right, const_right = evaluate(right)
        
        if coeff_left == coeff_right:
            return "Infinite solutions" if const_left == const_right else "No solution"
        return 'x=' + str((const_right - const_left) // (coeff_left - coeff_right))
