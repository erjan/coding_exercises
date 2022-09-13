'''
A delivery company wants to build a new service center in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new center in a position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.
'''

def getMinDistSum(self, P: List[List[int]]) -> float:
        from math import sqrt
        def dist_all(x, y):  # calculate the sum of distances from (x, y) to all points
            return sum(sqrt((x2-x)**2 + (y2-y)**2) for x2, y2 in P)

        l = len(P)
        x, y = sum(x for x, y in P) / l, sum(y for x, y in P) / l  # use centroid as the start point
        d = dist_all(x, y)  # sum of distances for initial point
        
        # step: inital searching step. choosing 10 since all point coordinates are in range [0, 100]
        # eps: since the problem demands an accuracy of 10^-5. I choose a smaller one, no reason
        # these two numbers are kind of arbitrarily choosen
        step, eps = 10, 0.000001
        while step > eps:
            flag = False  # Do we find a better point in this round?
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                x2, y2 = x + step * dx, y + step * dy
                t = dist_all(x2, y2)
                if t < d:  # do find a better solution point
                    x, y, d = x2, y2, t
                    flag = True
                    break
            if not flag: step /= 2  # if no better point is found, shrink ths step for a closer search
        return d
