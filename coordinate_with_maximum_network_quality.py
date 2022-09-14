'''
You are given an array of network towers towers, where towers[i] = [xi, yi, qi] denotes the ith network tower with location (xi, yi) and quality factor qi. All the coordinates are integral coordinates on the X-Y plane, and the distance between the two coordinates is the Euclidean distance.

You are also given an integer radius where a tower is reachable if the distance is less than or equal to radius. Outside that distance, the signal becomes garbled, and the tower is not reachable.

The signal quality of the ith tower at a coordinate (x, y) is calculated with the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower and the coordinate. The network quality at a coordinate is the sum of the signal qualities from all the reachable towers.

Return the array [cx, cy] representing the integral coordinate (cx, cy) where the network quality is maximum. If there are multiple coordinates with the same network quality, return the lexicographically minimum non-negative coordinate.
'''

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        return max(
            (
                (sum(qi // (1 + dist) for xi, yi, qi in towers if (dist := sqrt((xi - x) ** 2 + (yi - y) ** 2)) <= radius),
                 [x, y]) for x in range(51) for y in range(51)
            ),
            key=lambda x: (x[0], -x[1][0], -x[1][1])
        )[1]
      
----------------------------------------------------------------------------------------
class Solution:
    def bestCoordinate(self, towers, radius: int):
        x_max = y_max = 0
        for x, y, q in towers:
            x_max = max(x_max, x)
            y_max = max(y_max, y)
        points = []
        for x in range(x_max + 1):
            for y in range(y_max + 1):
                quality = 0
                for xt, yt, q in towers:
                    distance = pow(pow(xt - x, 2) + pow(yt - y, 2), 0.5)
                    if distance <= radius:
                        quality += int(q / (1 + distance))
                points.append([x, y, quality])
        return max(points, key=lambda lst: lst[2])[:2] if points else [0, 0]
