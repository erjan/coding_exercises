'''
Consider a matrix M with dimensions width * height, such that every cell has value 0 or 1, and 
any square sub-matrix of M of size sideLength * sideLength has at most maxOnes ones.

Return the maximum possible number of ones that the matrix M can have.
'''

Long Version:

class Solution:
    def maximumNumberOfOnes(self, w: int, h: int, s: int, m: int) -> int:
    	(a,b), (c,d) = divmod(w,s), divmod(h,s)
    	if c > a: (a,b), (c,d) = (c,d), (a,b)
    	fs = m*a*c
    	if m <= b*d: return fs + (a+c+1)*m
    	if m <= s*d: return fs + (a+c+1)*b*d + a*(m-b*d)
    	if m > s*d: return fs + (a+c+1)*b*d + a*d*(s-b) + c*(min(m-s*d, b*(s-d)))
		
		
One Line Version:

class Solution:
    def maximumNumberOfOnes(self, w: int, h: int, s: int, m: int) -> int:
    	return (lambda c,d,a,b: m*a*c+(a+c+1)*min(m,b*d)+a*(min(max(m,b*d),s*d)-b*d)+c*(min(m-s*d,b*s-b*d))*(m>s*d))(*sum(sorted([[w//s,w%s],[h//s,h%s]]),[]))
      
      
---------------------------------------------------------------------
Don't check whether there are too many "1"s in a submatrix, this is too hard to implement. Instead, only look at the top left submatrix, try to set all points in it to "1", and find out how much benifit each "1" can make. Since you are only allowed to have "maxOnes" number of "1"s in a submatrix, you don't actually set them all to "1", instead you choose only those with best "benifit" to set to "1".
"Benifit" here means, if I set this position in the top left submatrix, then how many more "1" I can get in other folded submatrix.
If the big matrix can exactly fit all submatrix folded from top left submatrix, then all points should have the same folding benifits, just randomly pick any "maxOnes" number of points will work. But if not, then those at top left side will have more folding benifits than those on the bottom right side.
The final result will be the sum of all "benifits" from the choosen points in the top left submatrix

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res=[]
        for i in range(sideLength):
            for j in range(sideLength):
                xFolds=(width-i-1)//sideLength+1
                yFolds=(height-j-1)//sideLength+1
                res.append(xFolds*yFolds)
        res.sort(reverse=True)
        return sum(res[:maxOnes])
        
--------------------------------------------------------------

If we create the first square matrix, the big matrix will just be the copies of this one. (translation copies)
The value of each location in the square matrix will appear at multiple locations in the big matrix, count them.
Then assign the ones in the square matrix with more occurances with 1.

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res = []
        for i in range(sideLength):
            for j in range(sideLength):
                res += [((width - i - 1) // sideLength + 1) * ((height - j - 1) // sideLength + 1)]
        res = sorted(res,reverse = True)
        return sum(res[:maxOnes])
Or 1-liner just for fun..

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        return sum(sorted([((width-i-1)//sideLength+1)*((height-j-1)//sideLength+1) for i in range(sideLength) for j in range(sideLength)],reverse = True)[:maxOnes])
