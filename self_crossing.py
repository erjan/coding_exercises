'''
You are given an array of integers distance.

You start at point (0,0) on an X-Y plane and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return true if your path crosses itself, and false if it does not.
'''


def self_crossing(x):
    for i in range(3,len(x)):

        if x[i-3]>=x[i-1] and x[i]>=x[i-2]:
            return True
        
        if i>=4:
            if x[i-3] == x[i-1] and x[i-2]<=(x[i-4]+x[i]):
                return True

        if i>=5:
            if x[i-2]>=x[i-4] and x[i-3]>=x[i-1] and (x[i-5]+x[i-1])>=x[i-3] and (x[i-4]+x[i])>=x[i-2]:
                return True

    return False
  
---------------------------------------------------------------------------------------------------------------
b = c = d = e = 0
    for a in x:
        if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
            return True
        b, c, d, e, f = a, b, c, d, e
    return False
