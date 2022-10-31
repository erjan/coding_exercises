'''
You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video on a platform was created by creator[i], has an id of ids[i], and has views[i] views.

The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the highest popularity and the id of their most viewed video.

If multiple creators have the highest popularity, find all of them.
If multiple videos have the highest view count for a creator, find the lexicographically smallest id.
Return a 2D array of strings answer where answer[i] = [creatori, idi] means that creatori has the highest popularity and idi is the id of their most popular video. The answer can be returned in any order.
'''


I have declared a hashmap to collect the following values,

total number current views for the creator
store the lexicographic id of the creator's popular video
current popular view of the creator
So my final hashmap for the given basic test case looks like {'alice': [10, 'one', 5], 'bob': [10, 'two', 10], 'chris': [4, 'four', 4]}
memo["alice"][0] = total number of views for alice
memo["alice"][1] = min lexicographic id for alice's popular video
memo["alice"][2] = max popular video views for alice

Alongside with these, I have also initiated overall_max_popular_video_count to track the max_total_number_of_views for a creator
Once we collect all the above mentioned values,
I compare each and every creator's total number of views with the current_popular_video_count and make my result array.
Thanks for reading!

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        memo = {}
		#tracking the max popular video count
        overall_max_popular_video_count = -1
        #looping over the creators
        for i in range(len(creators)):
            if creators[i] in memo:
                #Step 1: update number of views for the creator
                memo[creators[i]][0] += views[i]
                #Step 2: update current_popular_video_view and id_of_most_popular_video_so_far
                if memo[creators[i]][2] < views[i]:
                    memo[creators[i]][1] = ids[i]
                    memo[creators[i]][2] = views[i]
                #Step 2a: finding the lexicographically smallest id as we hit the current_popularity_video_view again!
                elif memo[creators[i]][2] == views[i]:
                    memo[creators[i]][1] = min(memo[creators[i]][1],ids[i])
            else:
			#adding new entry to our memo
			#new entry is of the format memo[creator[i]] = [total number current views for the creator, store the lexicographic id of the popular video, current popular view of the creator]
                memo[creators[i]] = [views[i],ids[i],views[i]]
			#track the max popular video count
            overall_max_popular_video_count = max(memo[creators[i]][0],overall_max_popular_video_count)
        
        result = []
        for i in memo:
            if memo[i][0] == overall_max_popular_video_count:
                result.append([i,memo[i][1]])
        return result
      
