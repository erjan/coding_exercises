'''
You have a video sharing platform where users can upload and delete videos. Each video is a string of digits, where the ith digit of the string represents the content of the video at minute i. For example, the first digit represents the content at minute 0 in the video, the second digit represents the content at minute 1 in the video, and so on. Viewers of videos can also like and dislike videos. Internally, the platform keeps track of the number of views, likes, and dislikes on each video.

When a video is uploaded, it is associated with the smallest available integer videoId starting from 0. Once a video is deleted, the videoId associated with that video can be reused for another video.

Implement the VideoSharingPlatform class:

VideoSharingPlatform() Initializes the object.
int upload(String video) The user uploads a video. Return the videoId associated with the video.
void remove(int videoId) If there is a video associated with videoId, remove the video.
String watch(int videoId, int startMinute, int endMinute) If there is a video associated with videoId, increase the number of views on the video by 1 and return the substring of the video string starting at startMinute and ending at min(endMinute, video.length - 1) (inclusive). Otherwise, return "-1".
void like(int videoId) Increases the number of likes on the video associated with videoId by 1 if there is a video associated with videoId.
void dislike(int videoId) Increases the number of dislikes on the video associated with videoId by 1 if there is a video associated with videoId.
int[] getLikesAndDislikes(int videoId) Return a 0-indexed integer array values of length 2 where values[0] is the number of likes and values[1] is the number of dislikes on the video associated with videoId. If there is no video associated with videoId, return [-1].
int getViews(int videoId) Return the number of views on the video associated with videoId, if there is no video associated with videoId, return -1.
 
'''


class VideoSharingPlatform:

    def __init__(self):
        self.id = -1
        self.removed = []
        self.id_to_like = collections.defaultdict(int)
        self.id_to_dislike = collections.defaultdict(int)
        self.id_to_content = collections.defaultdict(str)
        self.id_to_view = collections.defaultdict(int)

    def upload(self, video: str) -> int:
        if not self.removed:
            self.id += 1

        new_id = heapq.heappop(self.removed) if self.removed else self.id
        self.id_to_content[new_id] = video
        self.id_to_like[new_id] = 0
        self.id_to_dislike[new_id] = 0
        self.id_to_view[new_id] = 0
        return new_id
        

    def remove(self, videoId: int) -> None:
        if videoId in self.id_to_content:
            self.id_to_content.pop(videoId)
            self.id_to_like.pop(videoId)
            self.id_to_dislike.pop(videoId)
            self.id_to_view.pop(videoId)
            heapq.heappush(self.removed, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.id_to_content:
            return "-1"

        self.id_to_view[videoId] += 1
        content = self.id_to_content[videoId][startMinute: endMinute+1]
        return content

    def like(self, videoId: int) -> None:
        self.id_to_like[videoId] += 1

    def dislike(self, videoId: int) -> None:
        self.id_to_dislike[videoId] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.id_to_content:
            return [-1]

        return [self.id_to_like[videoId], self.id_to_dislike[videoId]]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.id_to_content:
            return -1

        return self.id_to_view[videoId]
        
        
# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)
