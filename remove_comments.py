'''
Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.

In C++, there are two types of comments, line comments, and block comments.

The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others.

For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.

For example, source = "string s = "/* Not a comment. */";" will not be a test case.
Also, nothing else such as defines or macros will interfere with the comments.

It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.
'''

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        inblock = False
        for line in source:
            if not inblock:
                ans.append([])
            i = 0
            while i < len(line):
                if not inblock:
                    if line[i] == '/' and i + 1 < len(line) and line[i+1] in '/*':
                        if line[i+1] == '/':
                            break
                        i += 1    
                        inblock = True
                    else:
                        ans[-1].append(line[i])
                else:
                    if line[i] == '*' and i + 1 < len(line) and line[i+1] == '/':
                        i += 1
                        inblock = False
                i += 1
        return [''.join(line) for line in ans if line]
-----------------------------------------------------------------------------------------
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans, inComment = [], False
        new_str = ""
        for c in source:
            if not inComment: new_str = ""
            i, n = 0, len(c)
            # inComment, we find */
            while i < n:
                if inComment:
                    if c[i:i + 2] == '*/' and i + 1 < n:
                        i += 2
                        inComment = False
                        continue
                    i += 1
                # not in Comment, we find /* // and common character
                else:
                    if c[i:i + 2] == '/*' and i + 1 < n:
                        i += 2
                        inComment = True
                        continue
                    if c[i:i + 2] == '//' and i + 1 < n:
                        break
                    new_str += c[i]
                    i += 1
            if new_str and not inComment:
                ans.append(new_str)
                    

        return ans
----------------------------------------------------------------------------------      
      
