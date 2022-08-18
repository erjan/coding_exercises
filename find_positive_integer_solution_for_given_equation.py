'''
Given a callable function f(x, y) with a hidden formula and a value z, reverse engineer the formula and return all positive integer pairs x and y where f(x,y) == z. You may return the pairs in any order.

While the exact formula is hidden, the function is monotonically increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this:

interface CustomFunction {
public:
  // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
  int f(int x, int y);
};
We will judge your solution as follows:

The judge has a list of 9 hidden implementations of CustomFunction, along with a way to generate an answer key of all valid pairs for a specific z.
The judge will receive two inputs: a function_id (to determine which implementation to test your code with), and the target z.
The judge will call your findSolution and compare your results with the answer key.
If your results match the answer key, your solution will be Accepted.
'''



class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
		# record of all solution pairs (x, y)
        solution_pair = []
        
		# Two pointers, 
		# x goes from lower bound, 1, to upper bound z
		# y goes from upper bound, z, to lower bound 1
        x, y = 1, z
        
        while x <= z and y >= 1:
            
            f_of_x_y = customfunction.f(x,y)
            
            if f_of_x_y > z:
                # this f(x,y) is too big, make y smaller
                y -= 1
                
            elif f_of_x_y < z:
                # this f(x,y) is too small, make x bigger
                x += 1
            
            else:
                # pair (x, y) is a solution to f(x,y) = z
                solution_pair.append( (x,y) )

                # make x bigger for next iteration
                x += 1
        
        return solution_pair
