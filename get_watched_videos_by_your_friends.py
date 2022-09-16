'''
There are n people, each person has a unique id between 
0 and n-1. Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i.

Level 1 of videos are all
watched videos by your friends, level 2 of videos 
are all watched videos by the friends of your friends and so on. In general, the level k of videos are all watched videos by people with the shortest path exactly equal to k with you. Given your id and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest. 
'''

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = [id]
        count = 0
        seen = set(queue)
        while queue and count < level: #bfs
            count += 1
            temp = set()
            for i in queue: 
                for j in friends[i]:
                    if j not in seen: 
                        temp.add(j)
                        seen.add(j)
            queue = temp
        
        movies = dict()
        for i in queue: 
            for m in watchedVideos[i]: 
                movies[m] = movies.get(m, 0) + 1
        return [k for _, k in sorted((v, k) for k, v in movies.items())]
      
-----------------------------------------

from collections import Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue, seen = {id}, {id}
        for _ in range(level):
            queue = {j for i in queue for j in friends[i] if j not in seen}
            seen |= queue 
        freq = Counter(v for i in queue for v in watchedVideos[i])
        return sorted(freq.keys(), key=lambda x: (freq[x], x))
--------------------------------------------------------------------------------
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friends_already_visited=set()
        friends_at_last_level=set([id])
        for l in range(0,level):
            friends_already_visited.update(list(friends_at_last_level))
            newfriends=set()
            for oldfriend in friends_at_last_level:
                newfriends.update(friends[oldfriend])
            friends_at_last_level=newfriends.difference(friends_already_visited)
        video_freq=dict()
        for friend in friends_at_last_level:
            for video in watchedVideos[friend]:
                if video not in video_freq:
                    video_freq[video]=0
                video_freq[video]+=1
        return [video for video,freq in sorted(video_freq.items(), key= lambda item : (item[1], item[0]))]
      
