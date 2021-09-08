#my code - actually good solution
if __name__ == "__main__":
    l = list(map(int, input().split()))

    min1 = l[0]
    changed = False
    for i in range(len(l)):
        if l[i] < min1 and l[i] % 2 == 0:
            changed = True
            min1 = l[i]
    if not changed:
        print('no existe: -1')
    else:
        print('min even number in list is: %d' % min1)
        
#code based on idea from the lecture https://www.youtube.com/watch?v=SKwB41FrGgU&t=2s

if __name__ == "__main__":
  l = list(map(int, input().split()))
  
  ans = -1
  
  for i in range(len(l)):
    if  l[i] %2 == 0 and (ans == -1 or ans > l[i]):
       #we have not seen yet and changing it for the first time
        ans = l[i]
  print(ans)





