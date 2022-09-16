'''
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 
 '''

def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
	languages = [set(l) for l in languages]

	dontspeak = set()
	for u, v in friendships:
		u = u-1
		v = v-1
		if languages[u] & languages[v]: continue
		dontspeak.add(u)
		dontspeak.add(v)

	langcount = Counter()
	for f in dontspeak:
		for l in languages[f]:
			langcount[l] += 1

	return 0 if not dontspeak else len(dontspeak) - max(list(langcount.values()))

----------------------------------------------------------------------------------------------------
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(x) for x in languages]
        
        users = set()
        for u, v in friendships: 
            if not languages[u-1] & languages[v-1]: 
                users.add(u-1)
                users.add(v-1)
        
        freq = {}
        for i in users: 
            for k in languages[i]:
                freq[k] = 1 + freq.get(k, 0)
        return len(users) - max(freq.values(), default=0)
