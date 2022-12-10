'''
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].
'''

def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
	Node = lambda: collections.defaultdict(Node)
	trie = Node()
	for w in words:
		node = functools.reduce(dict.__getitem__, sorted(set(w)), trie)
		# use key 0 to store counts
		node[0] = node.get(0, 0) + 1

	def dfs(p, node=trie, collect=False):
		if not node:
			return 0
		ans = node.get(0, 0) if collect else 0
		# iter all possible chars            
		for c in p:
			if c in node:
				# start to collect if we see the first char of puzzle
				ans += dfs(p, node[c], collect or c == p[0])
		return ans

	return [dfs(p) for p in puzzles]
