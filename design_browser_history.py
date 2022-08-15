'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''



class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

        
class BrowserHistory:
    

    def __init__(self, homepage: str):
        
        self.ll = Node(homepage, None, None)
       

    def visit(self, url: str) -> None:
        nxt = Node(url, None, None)
        self.ll.next = nxt
        nxt.prev = self.ll
        self.ll = self.ll.next
        return self.ll.val
        

    def back(self, steps: int) -> str:
        
        i = 0
        while i < steps and self.ll.prev is not None:
            
            self.ll = self.ll.prev
            i+=1
        return self.ll.val
        

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.ll.next is not None:
            self.ll = self.ll.next
            i+=1
        return self.ll.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


--------------------------------------------------------------------------------------------------------------------------
class BrowserHistory:
    
    '''
    We use two stacks here because anytime we'll need to go forward or backward to the 
    most recent page we were at. A Stack helps us accomplish exactly that
    
    Eg: We are at "YouTube" -> We then visit "Facebook" -> We then visit "Google"
    At this point our prevStack = ["YouTube", "Facebook"]
    If we called back(1), we need to go to Facebook (which was the most recent before Google)
        - We need to go back to Facebook (top of our prevStack rn)
        - But we need to add our curPage to the forward stack because I called forward(1) after this operation, I would need to go back to Google
        
    You should be able to do the same analysis for forward(steps) 
    
    This should help you see the intuition behind using 2 stacks and the general logic
    '''

    def __init__(self, homepage: str):
        self.curPage = homepage # We keep track of the page we are currently on
        self.prevStack = [] # We keep track of the pages if we were to go back 
        self.forwardStack = [] # We keep track of the pages if we were to go forward

    def visit(self, url: str) -> None:
        '''
        Step 1: Since we're visiting a new page from curPage (our current page/url), if we go back, we need to go back to curPage first, hence add curPage to the top of prevStack
        
        Step 2: Reset forwardStack as mentioned in question
        
        Step 3: Now we need to make sure we update our current page correctly
        '''
        
        
        self.prevStack.append(self.curPage) # Step 1
        self.forwardStack = [] # Step 2
        self.curPage = url # Step 3
        

    def back(self, steps: int) -> str:
        
        '''
        
        Algorithm: 
            Step 0. Keep repeating until we still have to go back
            Step 1. If we're going to go back from our curPage to page X, if we go forward from page X, we need to land at curPage, so add it to the forwardStack
            Step 2. We need to go back now so update the curPage as needed and remove it from the prevStack
            Step 3. We went back one more step at this point, so decrement possible by 1
        
        '''
        
        possible = min(steps, len(self.prevStack)) # In order to hamdle cases where steps > len(self.prevStack) ,we take the minimum of the two at all times
        
        while possible:  # Step 0
            self.forwardStack.append(self.curPage) # Step 1
            self.curPage = self.prevStack.pop() # Step 2
            possible -= 1 # Step 3 
        
            
        return self.curPage # We need to return the page we're at currently
    

    def forward(self, steps: int) -> str:
        
        '''
        
        Algorithm: 
            Step 0. Keep repeating until we still have to go forward
            Step 1. If we're going to go forward from our curPage to page X, if we go backward from page X, we need to land at curPage, so add it to our prevStack
            Step 2. We need to go forward now so update the curPage as needed and remove it from the forwardStack
            Step 3. We went forward one more step at this point, so decrement possible by 1
        
        '''
        
        possible = min(steps, len(self.forwardStack)) # In order to hamdle cases where steps > len(self.forwardStack) ,we take the minimum of the two at all times
        
        while possible:  # Step 0
            self.prevStack.append(self.curPage) # Step 1
            self.curPage = self.forwardStack.pop() # Step 2
            possible -= 1 # Step 3
        
        return self.curPage # We need to return the page we're at currently
      
-------------------------------------------------------------------------------------------

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while(steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while(steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val
-------------------------------------------------------------------------------
#stack 1 only

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0


    def visit(self, url: str) -> None:
        while len(self.history) > self.index + 1:
            self.history.pop()
        self.history.append(url)
        self.index += 1


    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.history[self.index]


    def forward(self, steps: int) -> str:
        self.index = min(len(self.history)-1, self.index + steps)
        return self.index
      
      
