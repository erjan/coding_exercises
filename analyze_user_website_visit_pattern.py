'''
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

'''
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        users = defaultdict(list)
    
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])): 
            users[user].append(site)

        patterns = Counter()

        for user, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))

        return max(sorted(patterns), key=patterns.get)
        
        
------------------------------------


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
		
		# Create tuples as shown in description
		# The timestamps may not always be pre-ordered (one of the testcases)
		# Sort first based on user, then time (grouping by user)
		# This also helps to maintain order of websites visited in the later part of the solution
		
		users = defaultdict(list)
	    # It is not necessary to use defaultdict here, we can manually create dictionaries too
		
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):    
            users[user].append(site)     # defaultdicts simplify and optimize code

        patterns = Counter()   # this can also be replaced with a manually created dictionary of counts
		
		# Get unique 3-sequence (note that website order will automatically be maintained)
		# Note that we take the set of each 3-sequence for each user as they may have repeats
		# For each 3-sequence, count number of users
		
        for user, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))     
		
		# Re-iterating above step for clarity
		# 1. first get all possible 3-sequences combinations(sites, 3)
		# 2. then, count each one once (set)
		# 3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter)) 
		# - updating a dictionary will update the value for existing keys accordingly (int in this case)
		
		# An expanded version of the above step is given below.
			
    #         print(patterns)  # sanity check
	
		# get most frequent 3-sequence sorted lexicographically
        return max(sorted(patterns), key=patterns.get)
