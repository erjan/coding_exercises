'''
A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every minute, hour, or day).

For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:

Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
Every day (86400-second chunks): [10,10000]
Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (10000 in the above example).

Design and implement an API to help the company with their analysis.

Implement the TweetCounts class:

TweetCounts() Initializes the TweetCounts object.
void recordTweet(String tweetName, int time) Stores the tweetName at the recorded time (in seconds).
List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) Returns a list of integers representing the number of tweets with tweetName in each time chunk for the given period of time [startTime, endTime] (in seconds) and frequency freq.
freq is one of "minute", "hour", or "day" representing a frequency of every minute, hour, or day respectively.
'''

class TweetCounts:

    def __init__(self):
        self.tweets = dict()

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.setdefault(tweetName, []).append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute": seconds = 60 
        elif freq == "hour": seconds = 3600
        else: seconds = 86400
        
        ans = [0] * ((endTime - startTime)//seconds + 1)
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime: ans[(t-startTime)//seconds] += 1
        return ans 
      
-------------------------------------------

class TweetCounts:

    def __init__(self):
        self.dict = {}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if(tweetName not in self.dict):
            self.dict[tweetName] = [time]
        else:
            self.dict[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        times = self.dict[tweetName]
        
        size = 0 
        secs = 0
        
        if(freq == 'minute'):
            secs = 60
            size = (endTime - startTime) / 60 + 1
        if(freq == 'hour'):
            secs = 3600
            size = (endTime - startTime) / 3600 + 1
        if(freq == 'day'):
            secs = 86400
            size = (endTime - startTime) / 86400 + 1
                
        r = [0] * int(size)
        
        for i in times:
            if(startTime <= i and i <= endTime):
                index = int((i-startTime)/secs)
                r[index] += 1

        return r
--------------------------------------------------------------------

class TweetCounts:

    def __init__(self):
        self.tweetNames = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweetNames[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        if freq=="minute":
            chunk_size = 60
        elif freq=="hour":
            chunk_size = 60 * 60
        else:
            chunk_size = 60 * 60 * 24
            
        chunk_count = int((endTime - startTime)/chunk_size) + 1
        
        bins = [0] * (chunk_count)
        
        for tweettime in self.tweetNames[tweetName]:
            if(startTime <= tweettime and tweettime <= endTime):
                chunk_number = int((tweettime-startTime)/chunk_size)
                bins[chunk_number] +=1

        return bins
      
