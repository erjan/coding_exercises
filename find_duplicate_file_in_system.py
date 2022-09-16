'''
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"
'''

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contMap, ans = defaultdict(list), []
        for pStr in paths:
            sep = pStr.split(" ")
            for i in range(1, len(sep)):
                parts = sep[i].split('(')
                cont = parts[1][:-1]
                contMap[cont].append(sep[0] + '/' + parts[0])
        for v in contMap.values():
            if len(v) > 1: ans.append(v)
        return ans
      
--------------------------------------------------------------------------------

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        duplicateFiles=[]
        for filePath in paths:
            fileNames = filePath.split() #Split the path to filenames
            directoryPath = fileNames[0] #To take only the directory from the given filePath
            for file in fileNames[1:]: #traverse through each file
                fileName,fileContent = file[:file.index('(')],file[file.index('('):-1]#To get fileName and fileContent
                if fileContent not in dic:# if the content not in dic make an empty list for that particular key
                    dic[fileContent] = []
                dic[fileContent].append(directoryPath+'/'+fileName)#Just append the value of the key in the dictionary every key has a list of fileNames
        for value in dic.values():
            if len(value)>1: #Append only if the len the values in the Dictionary is > 1
                duplicateFiles.append(value)
        return duplicateFiles[::-1] #To generate the output as it is in the expected I have used [::-1]
