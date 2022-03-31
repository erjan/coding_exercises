'''
A value-equal string is a string where all characters are the same.

For example, "1111" and "33" are value-equal strings.
In contrast, "123" is not a value-equal string.
Given a digit string s, decompose the string into some number of consecutive value-equal substrings where exactly one substring has a length of 2 and the remaining substrings have a length of 3.

Return true if you can decompose s according to the above rules. Otherwise, return false.

A substring is a contiguous sequence of characters in a string.
'''



class Solution:
    def isDecomposable(self, s: str) -> bool:
        
            res = list()
            for c, g in groupby(s):
                #print(c, list(g))
                res.append(len(list(g)))

            print(res)


            res = list(set(res))  
            print(res)

            count2 = res.count(2)
            print('num of 2:', count2)
            # case 1 - separate length 2 and separate length3 strings
            if count2 == 1:
                 res.remove(2)
                 #all others should be div by 3
                 for i in range(len(res)):
                      if res[i] %3 != 0:
                           return False
                 return True

            elif count2 == 0:
                 nondiv3 = list(filter(lambda x: x%3 != 0, res))
                 print(nondiv3)
                    
                 if len(nondiv3) == 0:
                    print('bad')
                    return False

                 nondiv3 = nondiv3[0]

                 res.remove(nondiv3)
                 for i in range(len(res)):
                      if res[i] %3 != 0:
                           return False
                 if (nondiv3 - 2) %3 !=0:
                      return False
                 return True
              
              
#another solution

class Solution:
    def isDecomposable(self, s: str) -> bool:
        two_found = False
        count = 1
        for i, c in enumerate(s):
            if i == len(s) - 1 or c != s[i+1]:
                if count % 3:
                    if count % 3 ==  1 or two_found:
                        return False
                    two_found = True
                
                count = 0

            count += 1
                
        return two_found
      
      
#another

class Solution:
    def isDecomposable(self, s: str) -> bool:
        if len(s)%3 != 2:
            return False
        for i in range(0,10):
            if str(i)*3 in s:
                s = s.replace(str(i)*3,'')
        if len(s) == 2 and s[0] == s[1]:
            return True
        return False
      
#BEST

def isDecomposable(self, s: str) -> bool:
        c = itertools.groupby(s)
        two = 0
        for k, v in c:
            val = len(list(v))
            if val % 3 == 0:
                continue
            elif val % 3 == 2:
                two += 1
                if two >= 2:
                    return False
            else:
                return False
        return True if two == 1 else False
      
      
