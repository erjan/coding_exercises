'''
Line boundary character is a symbol of auxiliary text recording language, is an organic part of written language, used to express the nature and function of another line. Please complete the code in solution.py to realize the function of splitlines: split a paragraph of text into a list according to line boundary characters. The parameter src is a string containing 0 or more line boundary characters. Write code in the function body to split the incoming src string at the position where the line boundary character appears, and finally return the string with the largest length among all the strings split according to the line boundary character. If there are multiple results, The first matching string is returned.

'''
def splitlines(src: str) -> str:
    """
    :param src: The source string needs to be processed
    :return: The maximum length of the string
    """
    # -- write your code here --
    s = src
    s = s.splitlines()

    return max(s, key = lambda x: len(x))
