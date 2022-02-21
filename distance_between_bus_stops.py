'''
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs 
of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.
'''

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dest = destination
        if start == dest:
            return 0
        elif dest - start == 1:
            return distance[start]

        std_dest = 0
        if start < dest:
            for i in range(len(distance)):
                if i >= start and i < dest:
                    std_dest += distance[i]
            print('standard travel left to right : %d' % std_dest)

            d2 = 0
            for i in range(len(distance)):
                if i < start or i >= dest:
                    d2 += distance[i]
            print('another travel distance: %d' % d2)
        else:
            for i in range(len(distance)):
                if i >= dest and i < start:
                    std_dest += distance[i]
            print('standard travel left to right : %d' % std_dest)

            d2 = 0
            for i in range(len(distance)):
                if i < dest or i >= start:
                    d2 += distance[i]
            print('another travel distance: %d' % d2)

        res = (min(d2, std_dest))
        print(res)
        return res
