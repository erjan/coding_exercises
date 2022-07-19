'''
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
'''

class Solution:
    def countAsterisks(self, s: str) -> int:
        btw_pair = False
        res = 0
        for i in range(len(s)):

            if s[i] == '|' and not btw_pair:
                btw_pair = True
            elif s[i] == '|' and btw_pair:
                btw_pair = False
            elif s[i] == '*' and not btw_pair:
                res += 1

        return res
      
-------------------------------------------------------------------------------------------------------------
# логика здесь: если нет | то мы добавляем в список
# добавлять все до тех пор пока не встретим | потом игнорировать - все что идет дальше это уже внутри скобок(пары) поэтому игнорировать
# потом добавить

class Solution:
  def f(s):

      lst = []
      for i in s:
          print('--------------------------')
          print('lst ' + str(lst))
          if '|' not in lst:                          
              print('adding %s' % i)
              lst.append(i)
          elif '|' in lst and i == '|':

              x = lst.pop()
              print('removing %s ' % x)
      print(lst)
      return lst.count('*')
