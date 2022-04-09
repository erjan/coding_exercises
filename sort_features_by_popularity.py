'''

You are given a string array features where features[i] is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array responses, where each responses[i] is a string containing space-separated words.

The popularity of a feature is the number of responses[i] that contain the feature. You want to sort the features in non-increasing order by their popularity. If two features have the same popularity, order them by their original index in features. Notice that one response could contain the same feature multiple times; this feature is only counted once in its popularity.

Return the features in sorted order.
'''

class Solution:
    def sortFeatures(self, features, responses):
        c, f = Counter(features), set(features)
        for r in responses: c += Counter(set(r.split()) & f)
        return (n for n, i in c.most_common())
      
      
      
class Solution:
    def sortFeatures(self, features, responses):
        c, f = Counter(features), set(features)
        c += reduce(add, (map(lambda r : Counter(set(r.split()) & f), responses)))
        return (n for n, i in c.most_common())
      
class Solution:
    def sortFeatures(self, features, responses):
        c, f = Counter(features), set(features)
        c += reduce(add, (Counter(set(r.split()) & f) for r in responses))
        return (n for n, i in c.most_common())      
