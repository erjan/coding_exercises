'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def helper(self, stones):            
            n = stones
            #print(n)
            n = sorted(n)
            if len(n) == 0:
                print('empty list')
                return 0
            if len(n) == 1:
                print('length is 1')
                return n[0]
            if len(n) < 2:
                print('length is < 2')
                #print(n)
                return n
            res = n[-2:]
            rest = n[:-2]
            if len(res) == 2:
                first_max = res[1]
                second_max = res[0]
                if first_max == second_max:
                    n = n[:-2]
                    print('mutually destroyed, sending array %s' % n)
                    return helper(self,n)
                else:
                    n = rest
                    n.append(first_max - second_max)
                    
                    return helper(self,n)
        return helper(self, stones)
