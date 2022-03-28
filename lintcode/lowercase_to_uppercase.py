#Convert a lowercase character to uppercase.

class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercase_to_uppercase(self, character: str) -> str:
        # write your code here

        if character.isupper():
            return character.lower()
        return character.upper()
