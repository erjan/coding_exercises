'''

Given an array of distinct strings words, return the minimal possible abbreviations for every word.

The following are the rules for a string abbreviation:

Begin with the first character, and then the number of characters abbreviated, followed by the last character.
If there is any conflict and more than one word shares the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original word.
If the abbreviation does not make the word shorter, then keep it as the original.

'''


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def makeAbbr(word, k):
            # create abbreviation from word 
            # k - # of letters that should be changed
            if k >= len(word)-2:
                return word
            wordAbbr = word[:k]
            wordAbbr +=  str(len(word) - 1 - k)
            wordAbbr += word[-1]
            return wordAbbr

        l = len(words)
        ans = [''] * l
        prefix = [0] * l

        # create max abbriviation for words
        for i in range(l):
            prefix[i] = 1
            ans[i] = makeAbbr(words[i], 1)

        for i in range(l):
            # this value only for while loop
            a = 0
            while a == 0:
                hashSet = []

                for j in range(i+1, l):
                    # looking duplicates and add index in list
                    if ans[j] == ans[i]:
                        hashSet.append(j)

                if len(hashSet) == 0:
                    # if we don't have duplicates abbreviation
                    a = 1

                hashSet.append(i) # we should add index of 1st duplicate word
                if len(hashSet) > 1: # if we have 2 words with same abbreviation
                    for k in hashSet:
                        prefix[k] += 1 # increase prefix
                        ans[k] = makeAbbr(words[k], prefix[k]) # change abbreviation
        return ans
      
---------------------------------------

validAbbs_table = {}
words = dict
def formAbb(word,prefix):
	pre = word[:prefix]
	return pre+str(len(word)-len(pre)-1)+word[-1]

def validate(arr):
	table = {}
	invalidAbbs = []
	for i in arr:
		if i[1] in table:
			table[i[1]].append(i[0])
		else: table[i[1]] = [i[0]]
	for i in table:
		if len(table[i]) == 1:
			abb = (i,table[i][0])
			if len(i) >= len(table[i][0]):
				abb = (table[i][0],table[i][0])
			validAbbs_table[abb[1]] = abb[0]
		else: invalidAbbs.extend(table[i])
	return invalidAbbs

def abbreviate(dict,count):
	if not dict:
		return [validAbbs_table[i] for i in words]
	arr = []
	for i in dict:
		abb = formAbb(i,count)
		arr.append((i,abb))
	invalidAbbs = validate(arr)
	return abbreviate(invalidAbbs,count+1)
return abbreviate(dict,1)
