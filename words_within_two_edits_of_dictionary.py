'''
You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

 
 '''

class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def add_word(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]


def search(node: Node, word: str, i: int = 0, replace: int = 2) -> bool:
    if replace == -1:
        return False
    if i == len(word):
        return True

    for char, node in node.children.items():
        if search(node, word, i + 1, replace - (char != word[i])):
            return True
    return False


class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        result: list[str] = []
        trie = Trie()

        for word in dictionary:
            trie.add_word(word)

        for word in queries:
            if search(trie.root, word):
                result.append(word)

        return result
--------------------------------------------------------------------------------------------------------
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def fut(a,b):
            ret = 0
            for i in range(len(a)):
                if a[i] != b[i]: ret += 1
            return ret
        res = []
        for q in queries:
            for d in dictionary:
                if fut(q,d) <= 2:
                    res.append(q)
                    break
        return res
