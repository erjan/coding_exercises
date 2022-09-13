'''
You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].
'''


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, l: List[int]) -> int:        
        # start from east, build angles for each point, exclude point same as stand point
        res = sorted([math.degrees(math.atan2((p[1] - l[1]), (p[0] - l[0]))) for p in points if p != l])        
        
        # build slide window
        angles = res + [x + 360 for x in res]         
        i = 0            
        best = 0            
        for j, ang in enumerate(angles):                
            while ang - angles[i] > angle:                    
                i += 1                    
            best = max(best, j - i + 1)              
        
        return best + (len(points) - len(res))  
      
---------------------------------------------------------------------------------------
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        x0,y0 = location
		# to radians
        angle *= pi/180
        # transform points to location + filter + transform to polar angle
        angles = sorted([atan2(x-x0,y-y0) for x,y in points if x!=x0 or y!=y0])
        n = len(angles)
        angles += [2*pi+a for a in angles]
        l,r = 0,0
        maxview=0
        while l<n:
            while r<2*n and angles[r]-angles[l]<=angle:
                r+=1
            maxview = max(maxview,r-l)
            while l<n and angles[r]-angles[l]>angle:            
                l+=1
        return maxview + len(points)-n
