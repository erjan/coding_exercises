#given an array of integers return a new array so each element at index i is the product of all the numbers in the original array except the one at i

import numpy as np
l = list(int(i) for i in input().split(' '))
res = 1
res = np.prod(l)
print(res)
# for el in l:
#   res *= el

for i in range(len(l)):
  l[i] = res / l[i]
print(l)


#what if you can't use division?

l = list(int(i) for i in input().split(' '))
result_l = list()
for i in range(len(l)):
  cur_prod = 1
  for j in range(len(l)):
    if j != i:
      cur_prod *= l[j]
  result_l.append(cur_prod)
print(result_l)
      

