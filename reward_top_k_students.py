'''
You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.
'''

class Solution:
    def topStudents(self, pos_feed: List[str], neg_feed: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos, neg, score_id = set(pos_feed), set(neg_feed), []
        for r, id in zip(report, student_id):
            score = sum(3 if w in pos else -1 if w in neg else 0 for w in r.split(" "))
            score_id.append((-score, id))
        return [id for _, id in sorted(score_id)[0 : k]]
      
-----------------------------------------------------------------------------------------------
class Solution: 
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        mp = {}
        for sentence, id in zip(report, student_id): 
            point = 0 
            for word in sentence.split(): 
                if word in positive_feedback: point += 3
                elif word in negative_feedback: point -= 1
            mp[id] = point 
        return sorted(mp, key=lambda x: (-mp[x], x))[:k]
----------------------------------------------------------------------------------------------------------------

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        d = dict()
        for rep,s_id in zip(report,student_id):

            r = rep.split(' ')
            point = 0
            for word in r:
                if word in positive_feedback: point+=3 
                elif word in negative_feedback: point-=1
            
            d[s_id] = point
        
        d = sorted(d, key = lambda x: (-d[x],x))

        return d[:k]                        
