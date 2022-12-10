'''
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
/a
/a/x
/a/x/y
/a/z
/b
/b/x
/b/x/y
/b/z
However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.
'''


class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.is_end = False
        self.child_hash = ""
        self.char = char

class Trie:
    def __init__(self):
        self.root = TrieNode("/")
        self.hashmap = collections.defaultdict(int)
        self.duplicates = []

    def insert(self, folder):
        current_node = self.root
        for char in folder:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        current_node.is_end = True

    def _hash_children(self, root):
        for char in sorted(root.children.keys()):
            self._hash_children(root.children[char])
            root.child_hash += char + '|' + root.children[char].child_hash + '|' 
        self.hashmap[root.child_hash] += 1
    
    def hash_children(self):
        current_node = self.root
        self._hash_children(current_node)
    
    def _get_duplicates(self, root, path):
        if root.children and self.hashmap[root.child_hash] > 1: 
            return
        self.duplicates.append(path + [root.char])
        for char in root.children:
            self._get_duplicates(root.children[char], path + [root.char])

    def get_duplicates(self):
        current_node = self.root
        for char in current_node.children:
            self._get_duplicates(current_node.children[char], [])
        return self.duplicates

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = Trie()
        for path in paths:
            trie.insert(path)
        trie.hash_children()
        return trie.get_duplicates()
      
-------------------------------------------------------------------------------------------------------------
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.delete = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        patterns = defaultdict(list)
        ans = []

        self.populate_trie(root, paths)
        self.generate_patterns(root, patterns)
        self.update_node_status(patterns)
        self.generate_valid_paths(root, [], ans)
        
        return ans
        
    def populate_trie(self, root, paths):
        for path in sorted(paths):
            node = root
            for c in path:
                node = node.children[c]

    def generate_patterns(self, node, patterns):
        pattern = f'({"".join(child + self.generate_patterns(node.children[child], patterns) for child in node.children)})'

        if pattern != "()":
            patterns[pattern].append(node)

        return pattern

    def update_node_status(self, patterns):
        for pattern in patterns:
            if len(patterns[pattern]) > 1:
                for node in patterns[pattern]:
                    node.delete = True

    def generate_valid_paths(self, node, path, ans):
        if path:
            ans.append(path[:])
        
        for child in node.children:
            if not node.children[child].delete:
                self.generate_valid_paths(node.children[child], path + [child], ans)
