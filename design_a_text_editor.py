'''
Design a text editor with a cursor that can do the following:

Add text to where the cursor is.
Delete text from where the cursor is (simulating the backspace key).
Move the cursor either left or right.
When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

Implement the TextEditor class:

TextEditor() Initializes the object with empty text.
void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TextEditor:
    def __init__(self):
        self.cursor = Node(-1)
        
    def addText(self, text: str) -> None:
        curr = self.cursor
        last = curr.right
        for c in text:
            curr.right = Node(c)
            curr.right.left = curr
            curr = curr.right
        curr.right = last
        if last:
            last.left = curr
        self.cursor = curr
        
    def deleteText(self, k: int) -> int:
        curr = self.cursor
        last = curr.right
        tot = 0
        while k and curr.val != -1:
            curr = curr.left
            k -= 1
            tot += 1
        if last:
            last.left = curr
        curr.right = last
        self.cursor = curr
        return tot
        
    def cursorLeft(self, k: int) -> str:
        while k and self.cursor.val != -1:
            self.cursor = self.cursor.left
            k -= 1
        return self.getvals(self.cursor)
    
    def cursorRight(self, k: int) -> str:
        while k and self.cursor.right:
            self.cursor = self.cursor.right
            k -= 1
        return self.getvals(self.cursor)
    
    def getvals(self, curr):
        vals = deque()
        k = 10
        while k and curr.val != -1:
            vals.appendleft(curr.val)
            curr = curr.left
            k -= 1
        return "".join(vals)
----------------------------------------------------------------
class TextEditor:
    def __init__(self):
        self.left = deque()
        self.right = deque()
        
    def addText(self, text: str) -> None:
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        tot = 0
        while k and self.left:
            self.left.pop()
            k -= 1
            tot +=1
        return tot
        
    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.appendleft(self.left.pop())
            k -= 1
        return self.getvals()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.popleft())
            k -= 1
        return self.getvals()
        
    def getvals(self):
        N = len(self.left) 
        return "".join(self.left[i] for i in range(max(N-10, 0), N))
      
---------------------------------------------------------------------------------------
class TextEditor:

    def __init__(self):
        self.txt = ''  
        self.ptr = 0  

    def addText(self, text: str) -> None:
        self.txt = self.txt[:self.ptr] + text + self.txt[self.ptr:]
        self.ptr += len(text)  

    def deleteText(self, k: int) -> int:
        org = len(self.txt)  
        self.txt = self.txt[:max(self.ptr - k, 0)] + self.txt[self.ptr:]
        self.ptr = max(self.ptr - k, 0)  
        return org - len(self.txt)

    def cursorLeft(self, k: int) -> str:
        self.ptr = max(self.ptr - k, 0)  
        return self.txt[max(0, self.ptr - 10):self.ptr]

    def cursorRight(self, k: int) -> str:
        self.ptr = min(self.ptr + k, len(self.txt))  
        return self.txt[max(0, self.ptr - 10):self.ptr]
