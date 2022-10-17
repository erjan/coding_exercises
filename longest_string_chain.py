'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.


How should we approach this problem? 🤔
The first thing which comes into mind is DP. There are a few reasons for this thought.

It asks for longest possible word chain, so it is an optimization problem.
The chain is extended by adding a new word which only depends on the last word of the chain. So, it can be broken down into subproblems.
✅ Solution I: Bottom-Up DP [Accepted]

Generally, we need to think of a recursive relation in a DP problem and then optimize it. But here, it wasn't required. Can we start with the shortest word and try to build a chain starting with it? Let's think in this direction. We then need to find the next shortest word and so on. It could be expensive, so sorting the entire array based on length will help.

Let prev be the predecessor of a word. Building a successor from prev will be more expensive than building a predecessor from that word. The following example will make it clear:

prev = "chain"
To build all possible successors, we need to add a letter anywhere in the word.
_ c _ h _ a _ i _ n _
We have 6 possible spaces and 26 possible letters, so a total of 6 * 26 possibilities.

Now, getting a predecessor from a word is a lot easier. Just remove a letter.
word = "chains"
pred = {"hains", "cains", "chins", "chans", "chais", "chain"}
So, for each word, we'll look for a predecessor. Wouldn't it be great if can have a data structure with the following two properties:

Can tell which of these predecessors are present in the array efficiently.
Store size of the chain ending with that predecessor.
Turns out that we already have one. It is unordered_map in C++ and dictionary in python.

'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = dp[prev] + 1
                    res = max(res, dp[word])

        return res

----------------------------------------------------------------------------------------------------------------

'''
FIrstly sort the given array on basis of length of words. Such that for a word i we would be checking words having length smaller than i

Create a dictionary or mapping to store the chain length till that words.
When chain of bigger word is to be found , it will be -> 1 + smaller_length_of_chain.

Initialize the chain length of each word to be 1.

As word.length <= 16, it is easy to create all combinations by taking out one character.

Form different words successor by deleting a letter and check if that word has a larger chain length.

Keep updating and select maximum chain length from mapping / dictionary.

UPVOTE IF HELPFuuL
'''


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)
        dic = {}
        
        for i in words:
            dic[ i ] = 1
            
            for j in range(len(i)):
                
                # creating words by deleting a letter
                successor = i[:j] + i[j+1:]
                if successor in dic:
                    dic[ i ] = max (dic[i], 1 + dic[successor])
        
        res = max(dic.values())
        return res
    
---------------------------------------------------------------------------------------------------------------------------------
The problem can be solved using DP as it's asking to find the longest string chain which means we have to go through all the possible paths to find the optimial solutions. We also need a way to define the overlapping subproblems and cache it.

✔️Solution I - Memoization - Top Down
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        words_set={w:idx for idx, w in enumerate(words)}
        
        @cache
        def dp(i):                 
            curr=words[i]
            max_length=0
            for idx in range(len(curr)):
                new_wc = curr[:idx] + curr[idx+1:]
                if new_wc in words_set:
                    max_length=max(max_length, 1 + dp(words_set[new_wc]))
        
            return max_length
        
        return max(dp(i)+1 for i in range(n))
A more concise variation shared by atorre

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        w_set = set(words)
        @cache
        def dp(w:str) -> int:
            return 1 + max((dp(s) for i in range(len(w)) if (s:=w[:i]+w[i+1:]) in w_set), default=0)
        return max(dp(w) for w in words)
if N is length of words and L is the max length of a word in words,

Time - O(N * L * L ) - first L is for the loop to find new words by deleting one character and the second L is to generate the new word.
Space - O(N * L) - space required for words_set.

✔️Solution I I - Tabulation - Bottom Up
A more concise version only possible because it's python :)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:                
        words.sort(key=len)
        dp={}
        for w in words:
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
