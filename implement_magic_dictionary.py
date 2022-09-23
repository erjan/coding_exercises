'''
Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
 
 '''


class MagicDictionary:

    def __init__(self):
        self.myDict=set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.myDict.add(word)

    def search(self, searchWord: str) -> bool:
        
        for word in self.myDict:
            if len(word)==len(searchWord) and word!=searchWord:
                changes=0
                for l1,l2 in zip(searchWord,word):
                    if l1!=l2:
                        changes+=1
                    if changes>1:
                        break
                if changes==1:
                    return True
        return False
