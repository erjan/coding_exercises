'''

You are given a list of list of integers intervals where each element contains the inclusive interval [start, end].

Return the most frequently occurring number in the intervals. If there are ties, return the smallest number.

solution:
Let's do a line sweep. Running a vertical line from left to right, we encounter OPEN and CLOSE events of the intervals.

First, we find max_active, the largest number of intervals that can be stabbed by a vertical line.

After, the first time that an interval can be stabbed max_active number of times, we return the left-most point of that interval.
'''
class Solution:
    def solve(self, intervals):    
      events = []
      for s, e in intervals:
          events.append([s, 'OPEN'])
          events.append([e, 'CLOSE'])
      events.sort()

      for e in events:
          print(e)
      print()
      active = max_active = 0
      for x, cmd in events:
          print('-----------------------------')
          print(x, cmd)
          print()
          if cmd == 'OPEN':
              active += 1
              print('increase active', active)
          else:
              active -= 1
              print('decrease active', active)

          max_active = max(max_active, active)
      print('max active', max_active)
      print()
      for x, cmd in events:
          active += 1 if cmd == 'OPEN' else -1
          if active == max_active:
              return x

      return 0
