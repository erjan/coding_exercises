'''
You are given a character array keys containing unique characters and a string array values containing strings of length 2. You are also given another string array dictionary that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a 0-indexed string.

A string is encrypted with the following process:

For each character c in the string, we find the index i satisfying keys[i] == c in keys.
Replace c with values[i] in the string.
Note that in case a character of the string is not present in keys, the encryption process cannot be carried out, and an empty string "" is returned.

A string is decrypted with the following process:

For each substring s of length 2 occurring at an even index in the string, we find an i such that values[i] == s. If there are multiple valid i, we choose any one of them. This means a string could have multiple possible strings it can decrypt to.
Replace s with keys[i] in the string.
Implement the Encrypter class:

Encrypter(char[] keys, String[] values, String[] dictionary) Initializes the Encrypter class with keys, values, and dictionary.
String encrypt(String word1) Encrypts word1 with the encryption process described above and returns the encrypted string.
int decrypt(String word2) Returns the number of possible strings word2 could decrypt to that also appear in dictionary.
'''

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d1=[None for _ in range(26)]
        self.d2={}
        for i,item in enumerate(keys):
            self.d1[ord(item)-97]=values[i]
        self.dict=Trie()
        for item in dictionary:
            val=self.encrypt(item)
            self.dict.insert(val)
    def encrypt(self, word1: str) -> str:
        ans=[]
        for item in word1:
            item=ord(item)-97
            if(not self.d1[item]):
                return ""
            else:
                ans.append(self.d1[item])
        return "".join(ans)
    def decrypt(self, word2: str) -> int:
        return self.dict.search(word2)

class Trie:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.count=0
    def insert(self,word):
        for item in word:
            j=ord(item)-97
            if(not self.child[j]):
                self.child[j]=Trie()
            self=self.child[j]
        self.count+=1
    def search(self,word):
        for item in word:
            j=ord(item)-97
            if(not self.child[j]):
                return 0
            self=self.child[j]
        return self.count


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

---------------------------------------------------------------------------------------------------------------

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encrypt_map = {k: v for k, v in zip(keys, values)}
        self.decrypt_map = Counter()
        
        for word in dictionary:
            res = self.encrypt(word)
            self.decrypt_map[res] += 1

    def encrypt(self, word1: str) -> str:
        return ''.join([self.encrypt_map[letter] for letter in word1])

    def decrypt(self, word2: str) -> int:
        return self.decrypt_map[word2]
