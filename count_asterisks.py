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
# добавлять все до тех пор пока не встретим | , как только началась первая |  - все что идет дальше это уже внутри скобок(пары) поэтому можно игнорировать
# потом если мы видим 2ую | - мы удаляем ее, и снова можно добавлять все элементы как не внутри скобок

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
    
--------------------------------------------------
# idea - bar count even odd
class Solution:
    def countAsterisks(self, s: str) -> int:
        bar_count = 0
        ast_count = 0
        
        for char in s:
            # check if this is a bar
            if char == '|':
                # adjust bar count
                bar_count += 1
            elif char == '*':
                # only if bar count is even, we should count it
                # because in this example l|*e*et|c**o|*de|
                # we skip the *e*et because it has odd bar count
                if bar_count & 1 == 0:
                    ast_count += 1
        
        return ast_count
