'''
 Given an input string array, reverse 
 the array word by word. A word is defined as a sequence of non-space strings.

The input character array does not contain 
leading or trailing spaces and the words are always separated by a single space.
'''
  
  def reverse_words(self, str: str) -> str:
        s = str
        s = s.split()

        s = s[::-1]
        s = " ".join(s)
        return s
