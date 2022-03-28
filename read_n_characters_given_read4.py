'''
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.
'''

class Solution:
    def read(self, buf: List[str], n: int) -> int:
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4
        
        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)
            
            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1
        
        return copied_chars

    
#another

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ## RC ##
        ## APPROACH : BUFFER READING ##
        ## 1. dont get confused with question description, our final buf will have min( n, all the characters that are in file)
        ## 2. At any point buf4, will maximum of 4 characters or count returned from the read4.
        ## 3. As I can read utmost 4 chars at a time, I create an array of size 4 and pass it to the function read4(buf4). That read4 function will fill my buf4 and returns the count how many characters it filled.
        ## 4. I take those buf4 chars filled and append it to my final buf.
        
        buf4 = [''] * 4         
        read = 0
        while read < n: 
            count = read4(buf4)             # Read file into buf4 && count -> num of chars in buf4
            if not count: break             # no of chars to read, EOF
            count = min(count, n - read)    # if n = 5 and file size is 8, in second read you have to take only n-read i.e 5-4 = 1
            buf[read:] = buf4[:count]       # Copy from buf4 to buf.
            read += count
        return read   
