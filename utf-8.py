'''
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
'''


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        unicode=[]
        for i in range(len(data)):
            x=bin(data[i]).replace("0b", "")
            if len(x)<8:
                x='0'*(8-len(x))+x
            unicode.append(x)
        curr=None
        cont=0
        for i in range(len(unicode)):
            if cont>0:
                if unicode[i][:2]!='10':
                    return False
                cont-=1
            elif cont==0 and unicode[i][:2]=='10':
                return False
            else:
                for j in range(5):
                    if unicode[i][j]=='0':
                        if j==0:
                            curr=1
                        else:
                            curr=j
                            cont=j-1
                        break
                else:
                    print("ok2")
                    return False
        if cont>0:
            return False
        return True
