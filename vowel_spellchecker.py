'''
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 
 '''

class Solution:
    def spellchecker(self, W: List[str], Q: List[str]) -> List[str]:
        orig, lcase, mask = set(W), defaultdict(), defaultdict()
        regex = r'[aeiou]'
        for i in range(len(W)-1,-1,-1):
            word = W[i]
            wlow = word.lower()
            lcase[wlow] = word
            mask[re.sub(regex, '*', wlow)] = word
        for i in range(len(Q)):
            query = Q[i]
            qlow = query.lower()
            qmask = re.sub(regex, '*', qlow)
            if query in orig: continue
            elif qlow in lcase: Q[i] = lcase[qlow]
            elif qmask in mask: Q[i] = mask[qmask]
            else: Q[i] = ""
        return Q
      
-------------------------------------------------------------

Approach:

There are 4 possible scenarios for each word, we can try them in order of priority:

The word matches a word in wordlist
Creating a set of wordlist allows us to check if this is true in O(1) time.

The word matches a word in wordlist up to capitalization.
Convert the word to lowercase letters and check if the word is in
case_insensitive, if so, use the first word that matches with case insensitivity.

The word matches up to vowel errors.
Mask the word by converting all characters to lower case and all vowels to '*'.
Check if this mask is in vowel_insensitive. If so, use the first word that matches with vowel insensitivity.

None of the above are true, we add an empty string to res.

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        # Convert words and vowels to sets for O(1) lookup times
        words = set(wordlist)
        vowels = set('aeiouAEIOU')
        
        # Create two maps.  
        # One for case insensitive word to all words that match "key" -> ["Key", "kEy", "KEY"]
        # The other for vowel insensitive words "k*t*" -> ["Kite", "kato", "KUTA"]
        case_insensitive = collections.defaultdict(list)            
        vowel_insensitive = collections.defaultdict(list)
        for word in wordlist:
            case_insensitive[word.lower()].append(word)
            key = ''.join(char.lower() if char not in vowels else '*' for char in word)
            vowel_insensitive[key].append(word)

        res = []
        for word in queries:

            # Case 1: When query exactly matches a word
            if word in words:
                res.append(word)
                continue

            # Case 2: When query matches a word up to capitalization
            low = word.lower()
            if low in case_insensitive:
                res.append(case_insensitive[low][0])
                continue

            # Case 3: When query matches a word up to vowel errors
            key = ''.join(char.lower() if char not in vowels else '*' for char in word)
            if key in vowel_insensitive:
                res.append(vowel_insensitive[key][0])
                continue

            res.append('')

        return res
