'''
Your friend is typing his name into a keyboard. Sometimes, when typing a 
character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return 
True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
              
        f = lambda x: [list(group) for c, group in itertools.groupby(x)]

        name, typed = f(name), f(typed)

        if len(name) != len(typed): return False

        for i in range(len(name)):
            if not (name[i][0] == typed[i][0] and len(name[i]) <= len(typed[i])):
                return False

        return True
# 2 pointer solution

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n=len(name)
        m=len(typed)
        
        if m<n:
            return False
        i=j=0
        while(True):
            print(i,j)
            if i==n and j==m:
                return True
            
            if i<n and j<m and name[i]==typed[j]:
                i+=1
                j+=1
            elif j>0 and j<m and typed[j-1]==typed[j]:

                j+=1
            else:
                return False
