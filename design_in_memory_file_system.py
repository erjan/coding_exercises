'''
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
'''


class FileSystem(object):

    def __init__(self):
        self.trie = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if len(path) == 1: 
            return sorted(self.trie.keys())
        path = path.split('/')
        node = self.trie
        for p in path[1:]:
            node = node.setdefault(p, {})
        if type(node) == str:
            return [path[-1]]
        return sorted(node.keys())
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        path = path.split('/')
        node = self.trie
        for p in path[1:]:
            node = node.setdefault(p, {})
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        path = filePath.split('/')
        f = path[-1]
        node = self.trie
        for p in path[1:-1]:
            node = node.setdefault(p, {})
        if f not in node:
            node[f] = content
        else:
            node[f] += content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        path = filePath.split('/')
        f = path[-1]
        node = self.trie
        for p in path[1:-1]:
            node = node.setdefault(p, {})
        
        return node[f]
      
-------------------------------------------------------------------------
from abc import ABC, abstractmethod

class FileStructure(ABC):
    
    @abstractmethod
    def get_type(self) -> bool:
        pass
    
    @abstractmethod
    def get_children(self) -> List[str]:
        pass
    
    def size(self) -> int:
        pass
    
class File(FileStructure):
    
    def __init__(self, name) -> None:
        self.name = name
        self.content = ""
    
    def get_type(self) -> str:
        return "File"
    
    def get_children(self)-> List[str]:
        return [self.name]
    
    def read(self) -> str:
        return self.content
    
    def write(self, val) -> None:
        self.content += val
        return 
    
class Directory(FileStructure):
    
    def __init__(self, name = "") -> None:
        self.name = name
        self.children = {} # Name : FileStructure
        
    def get_type(self) -> str :
        return "Directory"
    
    def get_children(self):
        children = []
        for child in self.children.values():
            children.append(child.name)
        return sorted(children)
            
    def add_child(self,name, FileStructure):
        self.children[name] = FileStructure

class FileStructureManager(ABC):
    @abstractmethod    
    def create(self, directory, path):
        pass
    
class FileManager(FileStructureManager):
    
    def create(self, directory, path) -> File:
        file = File(path)
        directory.add_child(path,file)
        return file
    
class DirectoryManager(FileStructureManager):
    
    def create(self, directory, path) -> Directory:
        if not path :
            return directory
        ptr_dir = directory
        for sp in path:
            dir = Directory(sp)
            ptr_dir.add_child(sp, dir)
            ptr_dir = dir
        return dir

            
class FileSystem:

    def __init__(self):
        self.root = Directory()
        self.filemgr = FileManager()
        self.dirmgr = DirectoryManager()
        
    def process_path(self, path):
        path = path.split("/")
        if path[-1]=="":
            path = path[:-1]
        return path[1:]
    
    def traverse_path(self,path):
        ptr = self.root
        ind = -1
        for ind, dir in enumerate(path):
            if dir not in ptr.children:
                break
            ptr = ptr.children[dir]
        return ind,ptr
        
    def ls(self, path: str) -> List[str]:
        path = self.process_path(path)
        _,ptr = self.traverse_path(path)
        return ptr.get_children()            

    def mkdir(self, path: str) -> None:
        path = self.process_path(path)
        ind,ptr = self.traverse_path(path)
        self.dirmgr.create(ptr , path[ind:])

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = self.process_path(filePath)
        ind, ptr = self.traverse_path(path)
        if ptr.get_type() != "File":
            dest_dir = self.dirmgr.create(ptr, path[ind:-1])
            file = self.filemgr.create(dest_dir, path[-1])
            file.write(content)
        else:
            ptr.write(content)    
             
    def readContentFromFile(self, filePath: str) -> str:
        path = self.process_path(filePath)
        _, ptr = self.traverse_path(path)
        if ptr.get_type()!= "File":
            return ""
        return ptr.read()
      
------------------------------------------------------------------------------------
class FileSystem(defaultdict):
    def __init__(self):
        super(FileSystem, self).__init__(FileSystem)
        self.content = ''

    def ls(self, path: str) -> List[str]:
        fs = self.mkdir(path)
        return path.rsplit('/', 1)[-1:] if fs.content else sorted(fs.keys())

    def mkdir(self, path: str) -> 'FileSystem':
        f = filter(None, path.split('/'))
        return reduce(dict.__getitem__, f, self)

    def addContentToFile(self, path: str, content: str) -> None:
        self.mkdir(path).content += content

    def readContentFromFile(self, path: str) -> str:
        return self.mkdir(path).content
      
-----------------------------------------------------------------------
class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        
    def _addContent(self, text):
        self.content += text
        
class Folder:
    def __init__(self):
        self.children = collections.defaultdict(Folder)
        self.files = collections.defaultdict(File)
        
    def _addFile(self, name, content):
        if name in self.files:
            self.files[name]._addContent(content)
        else:
            self.files[name] = File(name, content)
            
    def _readFile(self, name):
        return self.files[name].content
        

class FileSystem:

    def __init__(self):
        self.root = Folder()
        
    def _read(self, path, isFile):
        node = self.root
        result = []
        
        parts = path.split("/")
        for i in range(1, len(parts) - 1):
            p = parts[i]
            node = node.children[p]
            
        item = parts[-1]
        if item in node.files:
            if isFile:
                return node._readFile(item)
            else:
                return [item]
        else:
            if item != "":
                node = node.children[item]
            for child in node.children.keys():
                result.append(child)
            for filename in node.files.keys():
                result.append(filename)
            result.sort()
            return result
        
    def _make(self, path, content=None):
        node = self.root
        
        parts = path.split("/")
        for i in range(1, len(parts) if not content else len(parts) - 1):
            p = parts[i]
            if p not in node.children:
                node.children[p] = Folder()
            node = node.children[p]
        
        if content:
            filename = parts[-1]
            node._addFile(filename, content)
        

    def ls(self, path: str) -> List[str]:
        return self._read(path, False)
    
                
    def mkdir(self, path: str) -> None:
        self._make(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        self._make(filePath, content)
        

    def readContentFromFile(self, filePath: str) -> str:
        return self._read(filePath, True)
      
-----------------------------------------------------------------
class FileSystem:

    def __init__(self):
        self.d = {}

    def ls(self, path: str) -> List[str]:
        hier = path.split('/')[1:]
        h = self.d
        for level in hier:
            if level == '':
                break
            elif level not in h:
                return None
            elif isinstance(h[level], str):
                return [level]
            h = h[level]
        return sorted(h.keys())

    def mkdir(self, path: str) -> None:
        location = path.split('/')[1:]
        h = self.d
        for level in location:
            if level not in h:
                h[level] = {}
            h = h[level]
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        location = filePath.split('/')[1:]
        h = self.d
        for level in location[:-1]:
            if level not in h:
                h[level] = {}
            h = h[level]
        h[location[-1]] = h.get(location[-1], '') + content
        
    def readContentFromFile(self, filePath: str) -> str:
        h = self.d
        location = filePath.split('/')[1:]
        for level in location[:-1]:
            if level not in h:
                return None
            h = h[level]
        return h.get(location[-1], None)
      
-----------------------------------------------------------------------------
class FileSystem:

    def __init__(self):
        self.root = {}
        

    def ls(self, path: str) -> List[str]:
        current_path = self.root
        for file in path.split("/"):
            if file:
                current_path = current_path[file]
        if "$" in current_path:
            return [path.split("/")[-1]]
        else:
            return sorted(current_path.keys())
        
        

    def mkdir(self, path: str) -> None:
        current_path = self.root
        for file in path.split("/"):
            if file:
                if file in current_path:
                    current_path = current_path[file]
                else:
                    current_path[file] = {}
                    current_path = current_path[file]

    def addContentToFile(self, filePath: str, content: str) -> None:
        current_path = self.root
        for file in filePath.split("/"):
            if file:
                if file in current_path:
                    current_path = current_path[file]
                else:
                    current_path[file] = {}
                    current_path = current_path[file]
        
        if "$" in current_path:
            current_path["$"] += content
        else:
            current_path["$"] = content
        
        

    def readContentFromFile(self, filePath: str) -> str:
        current_path = self.root
        for file in filePath.split("/"):
            if file:
                if file in current_path:
                    current_path = current_path[file]
                else:
                    current_path[file] = {}
                    current_path = current_path[file]
        
        return current_path["$"]
      
------------------------------------------------------------------
class Trie:
    def __init__(self) -> None:
        self.t_root = {}
        self.is_file = False
        self.content = ''
        
    def insert(self, path: str):
        node = self.fs_root
        path = path.split('/')[1:]
        for directory in path:
            if directory not in node.t_root:
                node.t_root[directory] = Trie()
            node = node.t_root[directory]
        return node
    
    def search(self, path: str):
        node = self.fs_root
        path = path.split('/')[1:]
        for directory in path:
            node = node.t_root[directory]
        return node

class FileSystem(Trie):
    def __init__(self) -> None:
        self.fs_root = Trie()
        
    def insert(self, path: str) -> Trie:
        return Trie.insert(self, path)
        
    def search(self, path: str) -> Trie:
        return Trie.search(self, path)

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(self.fs_root.t_root.keys())
        node = self.search(path)
        path = path.split('/')[1:]
        if node.is_file:
            return [path[-1]]
        return sorted(node.t_root.keys())

    def mkdir(self, path: str) -> None:
        node = self.insert(path)
        
    def addContentToFile(self, path: str, content: str) -> None:
        node = self.insert(path)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, path: str) -> str:
        node = self.search(path)
        return node.content
