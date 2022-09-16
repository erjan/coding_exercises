'''
HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.
'''

class Solution:
    def entityParser(self, text: str) -> str:
        
        html_symbol = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = text.replace( html_sym , formal_sym )
        
        return text
      
---------------------------------------------------------------------------------------------------
import re
class Solution:
    def entityParser(self, text: str) -> str:
        
        html_symbol = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = re.sub( html_sym , formal_sym, text )
        
        return text
      
----------------------------------------------------------------------------------------
class Solution:
    def entityParser(self, text):
        END = '&'
        START = ';'
        d = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }
        stack = []
        seen_start = False
        for ch in reversed(text):
            if ch == START:
                seen_start = True
            stack.append(ch)
            if ch == END and seen_start:
                # check for a match
                temp = []
                while stack[-1] != START:
                    temp.append(stack.pop())
                temp.append(stack.pop()) # the ;
                val = ''.join(temp)
                if val in d:
                    stack.append(d[val])
                else:
                    stack.append(val)
                seen_start = False
        return ''.join(reversed(stack))
      
-------------------------------------------------------
class Solution:

    def entityParser(self, text: str) -> str:
        """
        and I quote: &quot;...&quot;
        
        case ordinary -> append to result
        case & -> update the index
        case ;   -> try to decode the pattern
                
        """
		# try to decode the last pattern
        def convert(res, lastIdx):
            tmp = res[lastIdx:]
            if tmp in mp:
                res = res[:lastIdx] + mp[tmp]
            return res
            
        res = ''
        
        mp = {
            '&quot;':'"',
            '&apos;':"'",
            '&amp;':'&',
            '&gt;':'>',
            '&lt;':'<',
            '&frasl;':'/'
        }
        
        lastIdx = -1
		
        for c in text:
            res += c
			# & case, update the postion
            if c == '&':
                lastIdx = len(res)-1
                continue
			# ; enclose the html code, try to decode it
            if c == ';':
                if lastIdx != -1:
                    res = convert(res,lastIdx)
                    lastIdx = -1
                continue
        
        return res
