'''
You are given the strings key and message, which represent a cipher key and a secret 
message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter 
in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.
'''


from string import ascii_lowercase as ascii


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = dict()
        c = 0
        for i in range(len(key)):
            if key[i] != ' ':
                if key[i] not in d:
                    d[key[i]] = ascii[c]
                    c += 1

        res = ''
        for i in range(len(message)):
            if message[i] == ' ':
                res += ' '
            else:
                res += d[message[i]]
        return res
-----------------------------------------------------------------------------------

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        for char in message:
            res += mapping[char]
                
        return res
