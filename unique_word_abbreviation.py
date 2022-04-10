'''

The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

For example:

dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
it --> it because any word with only two characters is an abbreviation of itself.
Implement the ValidWordAbbr class:

ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
There is no word in dictionary whose abbreviation is equal to word's abbreviation.
For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.

'''


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = dictionary
        self.dictionary = defaultdict(list)
        for word in self.words:
            self.dictionary[self.getAbbr(word)].append(word)

    def isUnique(self, word: str) -> bool:
        abbrivation = self.getAbbr(word)
        if abbrivation in self.dictionary:
            for w in self.dictionary[abbrivation]:
                if word != w:
                    return False
        return True
          
            
    def getAbbr(self, word: str) -> str:
        n = len(word)
        return word[0]+str(n)+word[-1] if n > 2 else word
      
      
-----------------------

class ValidWordAbbr:

	def __init__(self, dictionary: List[str]):
		self.words = defaultdict(list)
		for word in dictionary:
			self.words[ word[0] + str(len(word) -2) + word[-1]  ].append(word)

	def isUnique(self, word: str) -> bool:
		if word[0] + str(len(word) -2) + word[-1]  in self.words:
			for w in self.words[ word[0] + str(len(word) -2) + word[-1]  ]:
				if not w == word: return False
		return True
