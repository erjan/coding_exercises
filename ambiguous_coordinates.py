'''
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended up with the string s.

For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".
Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)
'''

Idea:
For this problem, we have two basic challenges. The first challenge is preventing invalid coordinates. For that, we can define a helper function (parse) which will take a string (str) and only pass on valid options for another helper (process) to handle.

We can break down the options into three categories:

No decimal: Any option except one with more than 1 digit and a leading "0".
Decimal after first digit: Any option with more than 1 digit and no trailing "0".
Decimals throughout: Any option that doesn't start and end with a "0"
After defining our first helper function, the next thing we should do is iterate through possible comma locations in our input string (S) and separate the coordinate pair strings (xStr, yStr).

Then we'll run into the second challenge, which is to avoid repeating the same processing. If we were to employ a simple nested loop or recursive function to solve this problem, it would end up redoing the same processes many times, since both coordinates can have a decimal.

What we actually want is the product of two loops. The basic solution would be to create two arrays and iterate through their combinations, but there's really no need to actually build the second array, since we can just as easily process the combinations while we iterate through the second coordinate naturally.

So we should first build and validate all decimal options for the xStr of a given comma position and store the valid possibilities in an array (xPoss). Once this is complete we should find each valid decimal option for yStr, combine it with each value in xPoss, and add the results to our answer array (ans) before moving onto the next comma position.

To aid in this, we can define process, which will either store the valid decimal options from xStr into xPoss or combine valid decimal options from yStr with the contents of xPoss and store the results in ans, depending on which coordinate string we're currently on (xy).

Once we finish iterating through all comma positions, we can return ans.



class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        ans, xPoss = [], []
        def process(st: str, xy: int):
            if xy:
                for x in xPoss:
                    ans.append("(" + x + ", " + st + ")")
            else: xPoss.append(st)
        def parse(st: str, xy: int):
            if len(st) == 1 or st[0] != "0":
                process(st, xy)
            if len(st) > 1 and st[-1] != "0":
                process(st[:1] + "." + st[1:], xy)
            if len(st) > 2 and st[0] != "0" and st[-1] != "0":
                for i in range(2, len(st)):
                    process(st[:i] + "." + st[i:], xy)  
        for i in range(2, len(S)-1):
            strs, xPoss = [S[1:i], S[i:-1]], []
            for j in range(2):
                if xPoss or not j: parse(strs[j], j)
        return ans
--------------------------------------------------------------------------------

class Solution:
def ambiguousCoordinates(self, s: str) -> List[str]:
    
    def create(num):
        l=len(num)
        if l==1:
            return [num]
        if num[0]=="0" and num[-1]=="0":
            return []
        if num[0]=="0":
            return ["0."+num[1:]]
        if num[-1]=="0":
            return [num]
        local=[num]
        for i in range(1,len(num)):
            local.append(num[:i]+"."+num[i:])
        return local
    
    s=s[1:-1]
    n=len(s)
    res=[]
    for i in range(1,n):
        left = create(s[:i])
        right= create(s[i:])
        if not left or not right:
            continue
        for l in left:
            for r in right:
                res.append(f'({l}, {r})')
    return res
  ----------------------------------------------------------------
  class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        S = S[1:-1]
        def numbers(s):
            ans = []
            for i in range(1, len(s)+1):
                ns = s[:i]
                if s[i:]:
                    ns += "." + s[i:]
                if len(ns) > 1 and (
                    ns[0] == '0' and ns[-1] == '0' or
                    ns[0] == '0' and ns[1] != '.' or
                    ns[-1] == '0' and '.' in ns):
                    continue
                ans.append(ns)    
            return ans        
        return ['(' + p[0] + ', ' + p[1] + ')'
               for i in range(1, len(S))
               for p in itertools.product(numbers(S[:i]), numbers(S[i:]))]
      
