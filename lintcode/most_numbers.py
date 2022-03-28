'''
Find the number with the most occurrences in the given array.
When the number of occurrences is the same, return the smallest one.
'''

def f(array):     
      num2cnt = dict()
      for num in array:
          if num in num2cnt.keys():
              num2cnt[num] += 1
          else:
              num2cnt[num] = 1
      max_num = -1
      res = -1
      for k, v in num2cnt.items():
          if v > max_num:
              max_num = v
              res = k
          elif v == max_num and k < res:
              res = k
      return res
    
#my solution

        n = array
        d = dict(Counter(n))
        d = list(d.items())

        d = sorted(d, key = lambda x: x[0], reverse=True)

        d = sorted(d, key = lambda x: x[1], reverse=True)
        most_freq = d[0][1]

        res = 0
        for i in range(len(d)-1,-1,-1):
            if most_freq == d[i][1]:
                return d[i][0]
