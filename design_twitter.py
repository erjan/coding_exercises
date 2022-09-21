'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
'''

class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i=len(self.tweets)-1
        while i>=0 and len(res)<10:
            if self.tweets[i][0] in self.users[userId] or self.tweets[i][0]==userId:
                res.append(self.tweets[i][1])
            i-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]: self.users[followerId].remove(followeeId)
