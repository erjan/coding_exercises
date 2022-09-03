'''
Design an algorithm to encode a list of strings to a string. The encoded string is 
then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).
'''

class Codec:
    def encode(self, strs: [str]) -> str:
        return "".join(f"{len(ss)}|{ss}" for ss in strs)

    def decode(self, s: str) -> [str]:
        ans = []
        i = 0
        while i < len(s):
            ii = s.find("|", i)
            i = ii+1+int(s[i:ii])
            ans.append(s[ii+1:i])
        return ans 
      
-----------------------------------------

class Codec:
    def encode(self, strs: [str]) -> str:
        msg =  ''
        for s in strs : 
            msg+=s + chr(259)
        msg=msg[0:len(msg)-1]   
        return msg     
        
    def decode(self, s: str) -> [str]:
        lst = s.split(chr(259)) 
        return lst 
-----------------------------------------------

We need a delimiter to separate elements of strings. One way is to find a delimiter that is not in the 256 ASCII chars.
Here, we provide another way to encode and decode the strings, assumed that we don't acces to chars except those in 256 ASCII (I am not sure if this is a useful assumption). Delimiter is not an option in this assumption since it may be confused with those already in the strings. For example, if we choose '#' and strings are ['Hello#', '# world'], the encoded string becomes [Hello###World]. In decoder, we may end up with ['Hello', '##Word'], ['Hello#', '#World'] or ['Hello##', 'World']. Without other information, we don't know which one is the solution.
Another way to separate the encoded string is by recording the length for each original string, together with number of the strings in the list. For the Hello World case, we will record [5,5,2]. By 'HelloWorld' and [5,5,2], we can totally recover the original string list.
I think there are many ways to implement the idea. One way is to add length information in the encoded string. Here is one example:

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        str_encode = ''.join(strs)
        str_encode += '#'
        total_strs = len(strs)
        for s in strs:
            str_encode += str(len(s))+'#'
        str_encode += str(total_strs)
        return str_encode

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []
        strs = []
        index_start = s.rfind('#')
        num_strs = int(s[index_start+1:])
        s = s[:index_start]
        lens = []
        for _ in range(num_strs):
            index_start = s.rfind('#')
            s_len = int(s[index_start+1:])
            lens.append(s_len)
            s = s[:index_start]
        for l in lens[::-1]:
            strs.append(s[:l])
            s = s[l:]
        return strs
-------------------------------------------------------------------

class Codec:
    def encode(self, strs: [str]) -> str:
        self.d=[0]
        for x in strs:
            self.d.append(self.d[-1]+len(x))
        return "".join(strs)
            

    def decode(self, s: str) -> [str]:
        res=[]
        for i in range(1,len(self.d)):
            res.append(s[self.d[i-1]:self.d[i]])
        return res
            
------------------------------------------------

Overkill for this problem but I thought it was worth showing.

	class HuffmanTree:
        # Node class used to build Huffman Tree
        class Node:
            def __init__(self, char='', freq=0, left=None, right=None):
                self.char = char
                self.freq = freq
                self.left = left
                self.right = right

            def __lt__(self, other):
                return self.freq < other.freq
        
        def __init__(self, counter: defaultdict(int)) -> None:
            self.root = self.getRoot(counter)
            self.encoding = self.getEncodingDict()
        
        # Builds the Huffman Tree using a min-heap and returns the root node
        def getRoot(self, counter) -> 'Node':
            nodes = [self.Node(t[0], t[1]) for t in list(counter.items())]
            heapify(nodes)
            while len(nodes) > 1:
                l, r = heappop(nodes), heappop(nodes)
                heapq.heappush(nodes, self.Node('', l.freq+r.freq,l,r))
            return heappop(nodes)
        
        # Returns a dictionary of chars -> encodings
        def getEncodingDict(self) -> dict:
            encoding = {}
            def fillEncodingDict(root, s):
                if not root:
                    return
                if root.char != '':
                    encoding[root.char] = s
                else:
                    fillEncodingDict(root.left, s+'0')
                    fillEncodingDict(root.right, s+'1')
            fillEncodingDict(self.root, '')
            return encoding
        
        # Returns the encoding of a single string
        def encodeString(self, string: str) -> str:
            return ' '.join([self.encoding[c] for c in string])
        
        # Returns a list of encodings for a list of strings
        def encodeStrings(self, strings: list[str]) -> list[str]:
            return [self.encodeString(string) for string in strings]
        
        # Returns a single decoded string
        def decodeString(self, string: str) -> str:
            res, node = [], self.root
            for c in string:
                if c == '0':
                    node = node.left
                elif c == '1':
                    node = node.right
                if node.char != '':
                    res.append(node.char)
                    node = self.root
            if not string:
                res.append(self.root.char)
            return ''.join(res)
        
        # Returns a list of decoded strings
        def decodeStrings(self, strings: list[str]) -> str:
            return [self.decodeString(string) for string in strings]
    
    # We can't use the default counter as it doesn't handle empty strings
    def getCounter(self, strs: [str]) -> defaultdict(int):
        counter = defaultdict(int)
        for s in strs:
            if s == '':
                counter[''] += 1
                continue
            for c in str(s):
                counter[c] += 1
        return counter
            
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        counter = self.getCounter(strs)
        self.HuffmanTree = self.HuffmanTree(counter)
        return self.HuffmanTree.encodeStrings(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return self.HuffmanTree.decodeStrings(s)
--------------------------------------------------      
      
        
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ''
        for s in strs:

            res += str(len(s)) + '#' + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != '#':
                j+=1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j+1+length
        return res
      
      
