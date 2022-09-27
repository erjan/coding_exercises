'''
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.
'''

class Solution:
    def evaluate(self, expression: str) -> int:
        stack = []
        parenEnd = {}
        
        # Get the end parenthesis location 
        for idx, ch in enumerate(expression):
            if ch == '(':
                stack.append(idx)
            if ch == ')':
                parenEnd[stack.pop()] = idx

        # Parses the expression into a list, each new sublist is a set of parenthesis
        # Example: 
        # Input: "(let x 2 (mult x (let x 3 y 4 (add x y))))"
        # Output: ['let', 'x', '2', ['mult', 'x', ['let', 'x', '3', 'y', '4', ['add', 'x', 'y']]]]
        def parse(lo, hi):
            arr = []
            word = []

            i = lo
            while i < hi:
                if expression[i] == '(':
                    arr.append(parse(i + 1, parenEnd[i]))
                    i = parenEnd[i]
                elif expression[i] == ' ' or expression[i] == ')' and word != []:
                    if ''.join(word) != '':
                        arr.append(''.join(word))
                    word = []
                    i += 1
                elif expression[i] != ')':
                    word.append(expression[i])
                    i += 1
                else:
                    i += 1


            if word != []:
                arr.append(''.join(word))

            return arr

        # Change string expression into the list expression
        expressionList = parse(1, len(expression) - 1)

        # Eval expression with starting scope (variables)
        return self.genEval(expressionList, {})
    
    def genEval(self, expression, scope):
        if type(expression) != list:
            # If expression is just a variable or int
            try:
                return int(expression)
            except:
                return scope[expression]
        else:
            if expression[0] == 'let':
                # Remove "let" from expression list
                expression = expression[1:]
                
                # This loop updates the scope (variables)
                while len(expression) > 2:
                    scope = self.letEval(expression, scope.copy())
                    expression = expression[2:]
                    
                # Return the last value
                return self.genEval(expression[0], scope.copy())
                
            if expression[0] == 'add':
                return self.addEval(expression, scope.copy())
                
            if expression[0] == 'mult':
                return self.multEval(expression, scope.copy())


    
    def letEval(self, expression, scope):
        scope[expression[0]] = self.genEval(expression[1], scope)
        return scope
    
    def addEval(self, expression, scope):
        return self.genEval(expression[1], scope) + self.genEval(expression[2], scope)
    
    def multEval(self, expression, scope):
        return self.genEval(expression[1], scope) * self.genEval(expression[2], scope)
