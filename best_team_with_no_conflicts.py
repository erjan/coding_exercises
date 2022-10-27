'''
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.
'''

class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        l = len(scores)
        mapped = [[ages[i], scores[i]] for i in range(l)]
        mapped = sorted(mapped, key = lambda x : (x[0], x[1]))
        dp = [i[1] for i in mapped]
    
        for i in range(l):
            for j in range(0, i):
                if mapped[j][1] <= mapped[i][1]:
                    dp[i] = max(dp[i], mapped[i][1] + dp[j])
                elif mapped[i][0] == mapped[j][0]:
                    dp[i] = max(dp[i], mapped[i][1] + dp[j])
                    
        return max(dp)
      
------------------------------------------------------------------------

'''
Anytime I couldn't solve a problem, the above question bugged me alot. I have a train of thought which I use to get to the solution. Feel free to pick what works for you and device your own methods to arrive at solutions.

Thinking forward
In this train of thought, we first look at all information that is available to us. We are given 2 arrays of scores and age and the problem suggests that it has something to do with ordering w.r.t ages.
The word ordering quickly suggests that we can sort the input based on ages. ( But what kind of sort ? Ascending or Descending ? )
Will this sorting even take us closer to the solution ?

Jot down an example to answer yourself.
Let the scores array and ages array be the following ( Try to be as random as possible ) :
scores : [ 10, 2, 6, 4, 9 ]
ages. : [ 5, 1, 4, 5, 7]

Sorting the above array it by age (ASCENDING) leads me to ( If ages are equal sort ascending by score )
scores : [ 2, 6, 4, 10, 9 ]
ages. : [ 1, 4, 5, 5, 7]

Now that we get here, let's observe the constraints again.
Team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Let's modify this statement for a pair of sorted arrays. Since the arrays are now sorted by age, any younger player comes before an older player. This means, IF I am choosing a bunch of players for my solution, THEN, in the order from left to right in scores array, I am allowed to choose scores as long as they are increasing --> More strictly, they arenon-decreasing because it is allowed for a score of younger player = score of older player.
With the scores being [ 2, 6, 4, 10, 9 ]
I can pick a team with [2, 4, 9] => Total = 15
I can pick a team with [2, 6, 10] => Total = 18
Note: In doing the above, I DID NOT consider the age array at all! Because, inherently, age of any element on the left is less than or equal to the ones of the right. (For i < j, age[i] <= age[j] )

Now I can reformulate the problem statement saying,
We are given one array (HERE Scores array) and we can choose any number of elements in the order from LEFT to RIGHT , PROVIDED that the sequence of elements I pick are non-decreasing.

To put it more formally,
We have to select a sequence S in the given array A, such that for this sequence S any pair of indices i, j should yeild S[i] <= S[j], and we have to maximize sum(S)

So far we have simplified whatever information that was given to us. Let's now go to the next step.

Thinking backwards
In this train of thought, we think What topics is this problem related to ?
Brainstorm your ideas in this step to find what is relevant to this problem. More formally, the questions you ask yourself are ( the following are random ideas just to see what sticks )
Can I apply two pointers ? ( Doesn't look like it! )
Can I think of graphs ? ( To be honest, I thought about this to be graph problem for a long time. I thought is it about finding longest path where edges are given between younger player and older player based on age and score constraints. But this didn't lead me anywhere )
I see sequence in my problem statement, does this involve any Longest Increasing Subsequence Methods ? (But again LIS is for increasing sequence, but I need non-decreasing, Do I need to tweak LIS probably? ( You just hit Jackpot! Congratulations!! )
'''


def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    n = len(scores)
    players = [[a, s] for a, s in zip(ages, scores)]
    players.sort(reverse = True)
    
    ans = 0
    dp = [0]*n
    
    for i in range(n):
        score = players[i][1]
        dp[i] = score
        for j in range(i):
            if players[j][1] >= players[i][1]:
                dp[i] = max(dp[i], dp[j] + score)
        ans = max(ans, dp[i])
    
    return ans
  
