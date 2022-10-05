'''
You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.

We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.

Implement the LUPrefix class:

LUPrefix(int n) Initializes the object for a stream of n videos.
void upload(int video) Uploads video to the server.
int longest() Returns the length of the longest uploaded prefix defined above.
'''

class LUPrefix:

    def __init__(self, n: int):
        self.videos = [False] * (n + 1)
        self.ans = 0

    def upload(self, video: int) -> None:
        self.videos[video] = True
        if video == self.ans + 1:
            while video < len(self.videos):
                if not self.videos[video]:
                    break
                self.ans += 1
                video += 1

    def longest(self) -> int:
        return self.ans
      
---------------------------------------------------------
class LUPrefix:
    """
    Memory: O(n)
    Time:   O(1) per upload call, because adding to the set takes O(1) time, and the prefix
				 can be increased no more than n times for all n calls to the upload function
    """

    def __init__(self, n: int):
        self._longest = 0
        self._nums = set()

    def upload(self, video: int) -> None:
        self._nums.add(video)
        # Since the prefix cannot decrease, it is enough for us to increase it
        # until we reach the number that has not yet been added
        while self._longest + 1 in self._nums:
            self._longest += 1

    def longest(self) -> int:
        return self._longest
