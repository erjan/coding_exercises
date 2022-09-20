'''
There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

Given students and mentors, return the maximum compatibility score sum that can be achieved.
'''

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        res = [-1]
        visited = [False]*len(students)
        #ssf ===> score so far
        #res ==> final result. It is a list as it acts as a global variable
        #idx ====> index over students array.
        self.maxCompatibilityUtil(students,mentors,0,visited,res,0)
        return res[0]
    
    
    def maxCompatibilityUtil(self,students,mentors,ssf,visited,res,idx):
        if idx==len(students):
            res[0] = max(res[0],ssf)
            return 
        
        for i in range(len(mentors)):
            if visited[i]==False:
                visited[i]=True
                temp = 0
                for j in range(len(mentors[i])):
                    if mentors[i][j]==students[idx][j]:
                        temp = temp+1
                self.maxCompatibilityUtil(students,mentors,ssf+temp,visited,res,idx+1)
                visited[i]=False
                
----------------------------------------------------------------------------------------------------------
#another backtracking
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        mentors_vis = [False]* m
        def calculate_score(s_id, m_id):
            return sum(students[s_id][i]==mentors[m_id][i] for i in range(n))

        score_dp=[[0]*m for _ in range(m)]
        for s_id in range(m):
            for m_id in range(m):
                score_dp[s_id][m_id]=calculate_score(s_id,m_id)

        def get_score(s_id,m_id): return score_dp[s_id][m_id]

        def select_next_stu(s_id, score):
            if s_id==m: return score
            maxx=0
            for m_id in range(m):
                if mentors_vis[m_id]: continue
                mentors_vis[m_id]=True
                maxx=max(maxx, select_next_stu(s_id+1, score+get_score(s_id,m_id)))
                mentors_vis[m_id]=False
            return maxx

        return select_next_stu(0,0)
      
--------------------------------------------------------------------------------------------------------
class Solution:
    def maxCompatibilitySum(self, students, mentors):
        
        """
            . find correct match for mentors/students based on answers matching
            
            q. is there faster way to mattch answeers of mentor/student
            a. sorting ?
                NO. Tried didnt work. example. Reason: 
                    Imagine, if we choose greedy approach to mattch with best matching combination we get
                        m1, s1 combination match 100%
                        m2, s2 combination match 5%     
                    but suppose
                        m1, s2 combination is 60%
                        m2, s1 combinatini is 60 % so they didntt not match eexactly like in case 1 but theere total is 120% , meeaning we will have to lookahead and try all combination
                        
                So, backtrack/DP            
        """
        
        """
            DP(tuple_used_mentors, curr_index_student)
            states: 
				tuple_used_mentors -> used mentors state.. we can also use bitmask
				curr_index_student -> index at wee are at in students arr.. as soon as we are at end, we are finished. we can have also used mentor index here. doesnt really matter
            statet transition:
                for un_used mentors in tuples_used, 
                    getMatch(un_used, curr_index_student) + dp(tuple.add(curr_index), curr_index_student+1)
            base case
                curr_iindex is at end
        """
        n = len(students)
        
        def get_score(m, s):
            c = 0
            for i in range(len(m)):
                if m[i] == s[i]:
                    c += 1
            
            return c
        
        @cache
        def dp(curr_index_student, tuple_ment):
            
            if curr_index_student == n:
                return 0
            
            list_ment = list(tuple_ment)
            m = -inf
            
            for mentor_index in range(n):
                if list_ment[mentor_index-1] == True:
                    continue
                list_ment[mentor_index-1] = True
                score = get_score(mentors[mentor_index], students[curr_index_student])
                m = max(m, score + dp(curr_index_student+1, tuple(list_ment)))
                list_ment[mentor_index-1] = False
            
            return m
                
        
        return dp(0, tuple([False] * n))
