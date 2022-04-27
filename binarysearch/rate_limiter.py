'''
Implement a rate limiter that limits users’ requests with the following methods:

RateLimiter(int expire) constructs a new rate limiter with the given expire time.
limit(int uid, int timestamp) represents a request from user uid at time timestamp and should return whether the given user’s request fails. It should fail if the user had a successful request less than expire time ago.
You can assume that timestamp is monotonically increasing between requests.
'''


class RateLimiter:
    def __init__(self, expire):

        self.period = expire
        self.d = dict()
        

    def limit(self, uid, timestamp):

        if uid not in self.d or self.d[uid] + self.period <= timestamp:
            self.d[uid] = timestamp
            return False
        return True
      
      
----------------------------------------------------------------------------------
class RateLimiter:
    def __init__(self, expire):
        self.user_request_time = collections.defaultdict(lambda: float("-inf"))
        self.expire = expire

    def limit(self, uid, timestamp):
        user_request_time = self.user_request_time
        ptime = user_request_time[uid]
        ntime = timestamp
        if ntime >= ptime + self.expire:
            user_request_time[uid] = timestamp

        return ntime < ptime + self.expire

      
---------------------------------------------------------------------
class RateLimiter:
    def __init__(self, expire):
        self.requests = {}
        self.exp = expire

    def limit(self, uid, timestamp):
        if uid not in self.requests or timestamp - self.requests[uid] >= self.exp:
            self.requests[uid] = timestamp
            return False

        return True
