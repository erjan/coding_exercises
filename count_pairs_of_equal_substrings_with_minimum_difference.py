'''

You are given two strings firstString and secondString that are 0-indexed and consist only of lowercase English letters. Count the number of index quadruples (i,j,a,b) that satisfy the following conditions:

0 <= i <= j < firstString.length
0 <= a <= b < secondString.length
The substring of firstString that starts at the ith character and ends at the jth character (inclusive) is equal to the substring of secondString that starts at the ath character and ends at the bth character (inclusive).
j - a is the minimum possible value among all quadruples that satisfy the previous conditions.
Return the number of such quadruples.
'''

class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        s2idx2 = {s:i for i,s in enumerate(secondString)}
        min_value = float('inf')
        count = 0
        for i in range(len(firstString)):
            if firstString[i] in s2idx2:
                if i - s2idx2[firstString[i]] < min_value:
                    min_value = i - s2idx2[firstString[i]]
                    count = 1
                elif i - s2idx2[firstString[i]] == min_value:
                    count += 1
        return count 

--------------------------------------------------------
class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        left = [float('inf')] * 26
        right = [-1] * 26
        res = 0
        mi = float('inf')
        for i, ch in enumerate(firstString):
            left[ord(ch) - ord('a')] = min(left[ord(ch) - ord('a')], i)
        for i, ch in enumerate(secondString):
            right[ord(ch) - ord('a')] = max(right[ord(ch) - ord('a')], i)
        for i in range(26):
            if left[i] != -1:
                mi = min(mi, left[i] - right[i])
        for i in range(26):
            if left[i] != float('inf') and right[i] != -1:
                if left[i] - right[i] == mi:
                    res += 1
        return res
--------------------------------------------

Time Complexity: O(n) ∵ creating first, last, overlap, and mini are all O(n) operations
Space Complexity: O(1) ∵ first, last, overlap, and diff_ja will never contain more than 26 elements
Intuition:

The fourth point is key to solving this problem efficiently:

j - a is the minimum possible value among all quadruples that satisfy the previous conditions.

This means that:

Any substring that uses the character 'a' for example must use the first 'a' in firstString as it's last character and the last 'a' in secondString as it's first character.
The substring must be 1 character long.
It took me a little while to wrap my head around this fact. Here are some examples that helped: (click to show)
Approach:

Find the index of the first occurrence of each character in firstString.
Find the index of the last occurrence of each character in secondString.
For each character that appears in both firstString and secondString,
store the character in a dictionary diff_ja where key = (j - a) and the value is a list of
characters that have the key (j - a).
Find the smallest key mini in the dictionary.
Because each substring must be 1 character long,
the number of characters in diff_ja[mini] will be the answer.
class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        
        # 1. Find the first occurrence of each character in firstString.
        first = {}
        for j, char in enumerate(firstString):
            first.setdefault(char, j)
            
        # 2. Find the last occurrence of each character in secondString.
        last = {}            
        for a, char in enumerate(secondString):
            last[char] = a
        
        # 3. Find the value of (j - a) for characters that appear in both strings.
        diff_ja = defaultdict(list)
        overlap = set(firstString) & set(secondString)
        for char in overlap:
            diff_ja[first[char] - last[char]].append(char)
        
        # 4. Return the number of characters that share the minimum (j - a) value.
        mini = min(diff_ja.keys() or [0])
        return len(diff_ja[mini])
More Concisely:

class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        first = {firstString[j]: j for j in range(len(firstString)-1, -1, -1)}
        last = {secondString[a]: a for a in range(len(secondString))}            
        diff_ja = collections.Counter((first[char] - last[char] for char in set(firstString) & set(secondString)))
        return diff_ja[min(diff_ja.keys() or [None])]
    
---------------------------------------------

class Solution:
	def countQuadruples(self, firstString: str, secondString: str) -> int:
		d = {}
		res = 0
		dist = inf
		for i in range(len(firstString)):
			if firstString[i] not in d:
				d[firstString[i]] = i
		for i in range(len(secondString)):
			if secondString[i] in d:
				if d[secondString[i]] - i < dist:
					dist = d[secondString[i]] - i
					res = 1
				elif d[secondString[i]] - i == dist:
					res += 1
		return res
-------------------------------------------------------------------------------

Like Hint#1 says, only need to track single characters.
Since we are looking to keep track of the minimum difference, I started this by using python's min-heap, then realized I only ever needed to check one element and disregard all others since it would be directly replaced...not added to the heap-->single list.

	def countQuadruples(self, firstString: str, secondString: str) -> int:
		# store result in len(2) list: [current mimimum difference, number of characters with that difference]
        # initial value has an impossible difference with 0 occurrences for the case of no overlap of the strings
        minDiff = [max(len(firstString),len(secondString)), 0]
        for ch in set(firstString) & set(secondString):
            diff = firstString.find(ch)-secondString.rfind(ch)
            if minDiff[0] > diff:   # if current difference is smaller, reset list to 1 occurrence
                minDiff = [diff, 1]
            elif minDiff[0]==diff:
                minDiff[1] += 1     # if current difference is same as smallest, increment occurrences
			# ignore other cases as irrelevant
                
        return minDiff[1] # return number of occurrences
-----------------------------------------------------------------------------------------

		#define a map to hold the leftmost indices of each char
        indices = {}
        
        #iterate the firstString to get the leftmost indices of each char
        for i,c in enumerate(firstString):
            if c not in indices:
                indices[c]=i

        #define two variables to hold the result and dist==INF        
        result,dist = 0, float("inf")
        
        # now iterate the secondString :
        # 1. for each char check if present in firstString
        for a in range(len(secondString)):
            c = secondString[a]
            #2. if char present in both, get the dist of indices
            if c in indices:
                # new smallest distance found, update the distance & result
                if indices[c]-a<dist:
                    dist=indices[c]-a
                    result=1
                # else another instance of smallest distance found, increase result by 1
                elif indices[c]-a==dist:
                    result+=1
        return result
-------------------------------------------------------------------------------    
    
    
