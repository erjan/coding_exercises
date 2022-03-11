'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

'''

class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        i = 0
        while i < len(command):
            
            
            cur = command[i]
            
            if cur == 'G':
                result += "G"
                i+=1
            
            elif cur == '(':
                if command[i+1] == ')':
                    result+= "o"
                    i+=2
                elif command[i+1] == 'a':
                    result += "al"
                    i+=4
                    
        print(result)
        return result
            
