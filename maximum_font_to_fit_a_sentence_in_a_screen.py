'''
You are given a string text. We want to display text on a screen of width w and height h. You can choose any font size from array fonts, which contains the available font sizes in ascending order.

You can use the FontInfo interface to get the width and height of any character at any available font size.

The FontInfo interface is defined as such:

interface FontInfo {
  // Returns the width of character ch on the screen using font size fontSize.
  // O(1) per call
  public int getWidth(int fontSize, char ch);

  // Returns the height of any character on the screen using font size fontSize.
  // O(1) per call
  public int getHeight(int fontSize);
}
The calculated width of text for some fontSize is the sum of every getWidth(fontSize, text[i]) call for each 0 <= i < text.length (0-indexed). The calculated height of text for some fontSize is getHeight(fontSize). Note that text is displayed on a single line.

It is guaranteed that FontInfo will return the same value if you call getHeight or getWidth with the same parameters.

It is also guaranteed that for any font size fontSize and any character ch:

getHeight(fontSize) <= getHeight(fontSize+1)
getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)
Return the maximum font size you can use to display text on the screen. If text cannot fit on the display with any font size, return -1.
'''

Binary Search
Do binary search, checking both height and width.
C++

int maxFont(string s, int w, int h, vector<int>& fonts, FontInfo fontInfo) {
    int l = -1, r = fonts.size() - 1;
    while (l < r) {
        int m = max(l + 1, (l + r) / 2);
        if (fontInfo.getHeight(fonts[m]) > h || accumulate(begin(s), end(s), 0, [&](int t, char ch)
            { return t + fontInfo.getWidth(fonts[m], ch); }) > w)
            r = m - 1;
        else
            l = m;
    }
    return l == -1 ? -1 : fonts[l];
}
Complexity Analysis

Time: O(n * log m), where n is the number of character, and m - the number of fonts.
Memory: O(1)
Optimized Solution
As suggested by zed_b, we can count characters 'a'...'z' in our string. This way, we will need to call getWidth only 26 times per a font size, multiplying by the corresponding count.
Python

def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
    l, r, cnt = -1, len(fonts) - 1, Counter(text)
    while l < r:
        m = max(l + 1, (l + r) // 2)
        if fontInfo.getHeight(fonts[m]) > h or sum(n * fontInfo.getWidth(fonts[m], ch) for ch, n in cnt.items()) > w:
            r = m - 1
        else:
            l = m
    return fonts[l] if l != -1 else -1
--------------------------------------------------------------------------

lass Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        
        def helper(num):
            count = 0
            for t in text:
                count += fontInfo.getWidth(num, t)
            
            return count
        
        left = 0
        right = len(fonts) - 1
        
        while left < right:
            mid = (left+right+1) // 2
            width = helper(fonts[mid])
            
            height = fontInfo.getHeight(fonts[mid])

            if height <= h and width <= w:
                left = mid
            else:
                right = mid -1 
        
        
        return fonts[left] if helper(fonts[left]) <= w and fontInfo.getHeight(fonts[left]) <= h else -1
      
-----------------------------------------------------------------------------

# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """

class Solution:
    """
    Brute force linear search: loop over font size in reverse order. For the first time a font size fits the screen, return that font size.
    Optimized: Binary search through font sizes.
    
    write sub-function can_fit(font_size): returns if font_size fits screen:
    calculate width of text in font size, sum
    return true if text width less than screen width and text height less than screen height
    
    binary search through sorted fontsize array for optimal font size
    """
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        
        def can_fit(font_size):
            text_width=sum([fontInfo.getWidth(font_size,char) for char in text])
            text_height=fontInfo.getHeight(font_size)
            return text_width<=w and text_height<=h
        
        #binary search for the largest font size that can fit the screen, by shrinking the window
        #to a window of lenght 1 or 2, and then perform a linear search on smaller window.
        l,r=0,len(fonts)-1
        
        while r-l>1:
            m=l+(r-l)//2
            font_size=fonts[m]
            if not can_fit(font_size):
                r=m-1
            elif can_fit(font_size):
                l=m
        
        for i in range(r,l-1,-1):
            font_size=fonts[i]
            if can_fit(font_size):
                return font_size
        
        return -1
      
-------------------------------------------------------------------------------------------------------------------------
# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def isValid(fontSize):
            if fontInfo.getHeight(fontSize) > h:
                return False
            
            return sum(fontInfo.getWidth(fontSize, c) for c in text) <= w
                    
        low, high = 0, len(fonts)-1
        
        while low <= high:
            mid = low + (high-low)//2
            if isValid(fonts[mid]):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1 if high == -1 else fonts[high]
---------------------------------------------------------------

class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:

        left, right = 0, len(fonts)-1
        
        def if_valid(input_font_size):
            
            total_w = 0
            
            for c in text:
                total_w+=fontInfo.getWidth(input_font_size, c)
                
            if(total_w <= w and fontInfo.getHeight(input_font_size) <= h):
                return True
            else:
                return False
            
        if(if_valid(fonts[0]) == False):
            return -1
                   
        while(left < right):
            
            mid = (left+right)//2
            
            mid_font_size = fonts[mid]
			
            if(if_valid(mid_font_size)):
                left = mid+1
            else:
                right = mid
         
		#be careful about the boundary case
        if(if_valid(fonts[left])):
            return fonts[left]
        else:
            return fonts[left-1]
---------------------------------------------------------------

Best template ever (imo):

https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems

Modified it for this question

U want the lowest index for which the condition is true, which can be n, just after the last element (n - 1 ) which is why right is n.

class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        
        def condition(i):
            font = fonts[i]
            if fontInfo.getHeight(font) > h:
                return True
            current_width = 0
            
            for ch in text:
                current_width += fontInfo.getWidth(font, ch)
                if current_width > w:
                    
                    return True
                
            return False
        
        n = len(fonts)
        
        left = 0
        right = n
        
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        if left > 0:
            return fonts[left-1]
        
        return -1
      
      
          
      
      
  
