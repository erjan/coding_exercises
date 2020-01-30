 Given a sorted array, A, with possibly duplicated elements, 
find the indices of the first and last occurrences of a 
target element, x. Return -1 if the target is not found.

def first_last(l, target):
  res = list()
  for i in range(len(l)):
    if l[i] == target:
      if len(res) == 0:
        res.append(i)
      elif len(res) == 1:
        res.append(i)
      else:
        res = res[:-1]
        res.append(i)
  if len(res) == 0:
    print([-1,-1])
  elif len(res) == 1:
    print(res*2)
  else:
    print(res)


r = []
t = 2
first_last(r,t)
  
  
  
  
  #ugly solution - first 
  
  def first_last(l, target):
  first_found = False
  second_found = False
  res = list()
  for i in range(len(l)):
    if l[i] == target:
      if first_found == False:
        first_found = True
        res.append(i)
      elif second_found == False:
        second_found = True
        res.append(i)
      elif second_found:        
        res.append(i)
  if first_found == False:
    print([-1,-1])
  else:
    if len(res) > 2:
      print(res[0], res[-1])
    else:
      print(res)


r = [2,2,3,4,5,2]
t = 2
first_last(r,t)
