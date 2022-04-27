'''
You are given a two-dimensional list of integers relations. Each element relations[i] contains [a, b] meaning that person a is following person b on Twitter.

Return the list of people who follow someone that follows them back, sorted in ascending order.


solution: the idea is that we use 2 containers to store - one for traversing and the other for checking then adding

we check if (b,a) is already seen then we add it to the final array
'''



class Solution:

    def solve(self, relations):

        ans = set()
        seen = set()

        for a, b in relations:
            seen.add((a, b))
            time.sleep(0.5)
            print('added ', (a, b))

            if (b, a) in seen:
                print('(b,a) in seen', (b, a))
                time.sleep(0.5)
                ans.add(b)
                ans.add(a)

        k = list(ans)
        rtr = sorted(k)
        print('----------')
        print(rtr)
        return rtr
    
----------------------------------------------------------------------
class Solution:
    def solve(self, relations):
        res = set()
        ans = set()
        for a, b in relations:
            ans.add((a, b))

            if (b, a) in ans:
                res.add(b)
                res.add(a)

        res = list(res)
        res.sort()
        print(res)
        return res
