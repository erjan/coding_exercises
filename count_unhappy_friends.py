'''
You are given a list of preferences for n friends, where n is always even.

For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.

All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:

x prefers u over y, and
u prefers x over v.
Return the number of unhappy friends.
'''

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Do I prefer someone over you? 
        # Do they prefer me back over thier person?
        # check who my partner is 
        # Check where I ranked them 
        # for anyone who ranked earlier than my current partner 
        # did they rank me earlier than thier current partner? if so I am unhappy
        
        pairingDict = {}
        for i in pairs:
            pairingDict[i[0]] = i[1]
            pairingDict[i[1]] = i[0]
        
        def unhappy(main,partner):
            #checks if main is unhappy with partner
            partnerIndex = preferences[main].index(partner)
            if partnerIndex == 0: 
                return False
            partnerIndex -= 1
            while partnerIndex >= 0:
                better = preferences[main][partnerIndex]
                betterPartner = pairingDict[better]
                #does better rank me higher then thier current partner? 
                if preferences[better].index(betterPartner) > preferences[better].index(main):
                    return True
                partnerIndex -= 1
                   
        unhappyCount = 0
        if len(pairs) == 1:
            return 0 
        for i in pairs:
            # is i[0] unhappy?
            if unhappy(i[0],i[1]):
                unhappyCount +=1 
            if unhappy(i[1],i[0]):
                unhappyCount +=1 
        return unhappyCount
      
---------------------------------------

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        def find_preferred_friends(x: int) -> List[int]:
            """
            Returns friends of x that have a higher preference than partner.
            """
			partner = partners[x]  # Find the partner of x.
            x_friends = friend_prefs[x]  # Find all the friends of x.
            partner_ranking = x_friends[partner]  # Get the partner's ranking amongst those friends.
            return list(x_friends)[:partner_ranking]  # Return all friends with a preferred lower ranking.

        def is_unhappy(x: int) -> bool:
            """
            Returns True if person x is unhappy, otherwise False.
            """
            # Find the partner for person x.
            partner = partners[x]  
            # Find the friends that person x prefers more than this partner.
            preferred_friends = find_preferred_friends(x)  
            # A friend is unhappy with their partner if there is another friend with a higher preference 
            # and that friend prefers them over their partner.
            return any(friend_prefs[friend][x] <= friend_prefs[friend][partners[friend]] 
                       for friend in preferred_friends)

        # Create dictionary to lookup friend preference for any person.
        friend_prefs = {
            person: {friend: pref for pref, friend in enumerate(friends)}
            for person, friends in enumerate(preferences)
        }
		# Example:
		# {0: {1: 0, 3: 1, 2: 2},
	    #  1: {2: 0, 3: 1, 0: 2},
	    #  2: {1: 0, 3: 1, 0: 2},
	    #  3: {0: 0, 2: 1, 1: 2}}
 
        # Create dictionary to find anyone's partner.
        partners = {}
        for x, y in pairs:
            partners[x] = y
            partners[y] = x
        
		# Count and return the number of unhappy people.
        return sum(is_unhappy(person) for person in range(n))
