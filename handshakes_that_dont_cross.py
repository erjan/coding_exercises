'''
You are given an even number of people numPeople that stand around a circle and each person shakes hands with someone else so that there are numPeople / 2 handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since the answer could be very large, return it modulo 109 + 7.
'''


The first person and the person he shakes hand with divide the group into two parts. These two parts are the sub-problems.

class Solution:
    def numberOfWays(self, num_people: int) -> int:
        self.memo = {0:1}
        def dp(n):
            if n not in self.memo:
                self.memo[n] = sum([dp(i - 2) * dp(n-i) for i in range(2,n+1,2)]) % (10**9+7)
            return self.memo[n]
        return dp(num_people)
      
      
---------------------------------------------------------------
let's take num_people = 6 for example.
6 people stand around a circle, they are numbered as 1,2,3,4,5,6.
We can take any of them to launch hands shaking, let's take NO.1.
i. 1 shakes hands with 2, left left 0 people, right left 4 people. Then we get 2 ways of hands shaking.
ii. 1 shakes hands with 4, left left 2 people, right left 2 people. Then we get 1 way of hands shaking.
iii. 1 shakes hands with 6, left left 4 people, right left 0 people. Then we get 2 ways of hands shaking.

With each left and right, the procedure will be applied repeatly.

class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        d = {
            0: 1,
            2: 1,
            4: 2
        }
        
        for i in range(6, num_people + 1, 2):
            s = 0
            for j in range(i / 2):
                left = j * 2
                right = i - left - 2
                s += d[left] * d[right]
            d[i] = s    
            
                
        
        return d[num_people] % (10 ** 9 + 7)
      
---------------------------------------------------------------
The first person and the person he shakes hand with divide the group into two parts.
These two parts are the sub-problems. Let dp[n] be the number of ways they handshakes,
base case: dp[0] = dp[2] = 1,
recurrece relation: dp[n] = sum(dp[i] * dp[n - 2 - i] for i in [0, 2, ..., n - 2]).

    def numberOfWays(self, num_people: int) -> int:
        def recursive(n):
            mod = 10 ** 9 + 7
            if n in dp:
                return dp[n]
            dp[n] = 0
            for i in range(0, n, 2):
                dp[n] = (dp[n] + recursive(i) * recursive(n - 2 - i)) % mod
            return dp[n]
            
        dp = {0: 1, 2: 1}
        return recursive(num_people)
      
---------------------------------------------------------------------------
const numberOfWays = n => {
    let mod = BigInt(1000000007);
    let dp = new Array((n >> 1) + 1).fill(0n); // n >> 1 is just a fancy way of dividing n by 2 
    
    dp[0] = dp[1] = 1n;

    for (let i = 2; i <= n >> 1; i++) {
        for (let j = 1; j <= i; j++) {
            dp[i] = (dp[i] + dp[j - 1] * dp[i - j]) % mod;
        }
    }
    
    return dp[dp.length - 1]; 
}
First, I want to point out how incredibly similar this problem is to https://leetcode.com/problems/unique-binary-search-trees/.

The above problem states: Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Here's the solution to unique-binary-search-trees:

const numTrees = n => {
    let dp = new Array(n + 1).fill(0); 
    
    dp[0] = dp[1] = 1; 
    
    for (let i = 2; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
            dp[i] += dp[j - 1] * dp[i - j]; 
        }
    }
    
    return dp[dp.length - 1]; 
}
I wanted to understand why these nearly identical procedures give correct answers to two seemingly unrelated problms. My conclusion is that the best way to understand is to map the procedure to a visual diagram. In other words, I want to know what these loops represent in terms of the people standing in the circle and their handshakes.

image

In the image above, let's try to understand what's going on from the perspective of person #1.

Person #1 has (n / 2 = 4 / 2 = 2) options as to whose hand to shake. Either he shakes #2, or #4.
He cannot shake #3, as #2 would no longer be able to shake #4 due to crossing.

Each location in the dp represents the solution for a given number of people.
The first location, 0, represents the solution for 0 people.
The second location, 1, represents the solution for 2 people.
The third location, 2, represents the soltuion for 4 people, and so on.

As base cases, let's say that dp[0] = dp[1] = 1. If there are zero people, there is 1 unique handshake (I know this sounds weird, but just accept it for now, you'll see why it makes sense in a bit), and if there are two people, there is also 1 unique handshake, that is, the handshake between these two people.

Let's go back to #1's perspective, and let's see what happens when #1 decides whose hand to shake.

n = 4,
dp = [1, 1, 0];

image

If #1 decides to shake #2's hand, how many people are to the left of #1? Zero. There are no people standing to the left of #1.
How many people are to the right of #1? Two. Therefore, we can say that if #1 shakes #2's hand, there are dp[0] * dp[1] (solution for zero people * solution for two people) ways to shake hands. Ok, so let's add dp[0] * dp[1] = 1 to our dp[2].

dp = [1, 1, 1];

image

If #1 decides to shake #4's hand, how many people are to the left of #1? Two. There are two people standing to the left of #1.
How many people are to the right of #1? Zero. Therefore, we can say that if #1 shakes #4s hand, there are dp[1] * dp[0] (solution for two people * solution for zero people) ways to shake hands. Ok, so let's add dp[1] * dp[0] = 1 to our dp[2].

dp = [1, 1, 2];

And there we go, if we have 4 people, we have dp[2] = 2 ways to shake hands.

Now let's exand this to 6 people and see what happens.

n = 6
dp = [1, 1, 2]

Let's assume that the outer i loop has already iterated once, thus solving the problem for 4 people and placing the answer in dp[2].

What happens when i = 3?

image

Again, let's think from #1's perspective. #1 can either shake #2's hand, #4's hand, or #6's hand. If he shakes #2's hand, there are zero people on the left, four people on the right (3, 4, 5, 6). So, we multiply dp[0] * dp[2] (solution for zero people * solution for four people) and add that to dp[3] .

dp = [1, 1, 2, 2]

If he shakes #4's hand, there are two people on the left (2, 3), two people on the right (5, 6). So, we multiply dp[1] * dp[1] (solution for two people * solution for two people) and add that to dp[3] .

dp = [1, 1, 2, 3]

If he shakes #6s hand, there are four people on the left (2, 3, 4, 5), zero people on the right. So, we multiply dp[2] * dp[0] (solution for four people * solution for zero people) and add that to dp[3] .

dp = [1, 1, 2, 5]

And there we go! dp[3] now contains the solution to 6 people.

At each new iteration of i, we explore each option of dividing the circle, multiplying the solutions for the left and right side, and adding them to dp[i].

I strongly recommend looking at the unique binary trees problem and exploring how the dp procedure to that one relates.


-----------------------------------------------------------------------------------------
The main intuition behind the code is that, if all the people are standing in one circle, if we choose one people then the circle is divided into two groups.

Group1 : All the people standing to the left of the person selected
Group2: All the people standing to the right of the person selected

If we can calculate the number of ways the people in group1 can shake hand, and the number of ways people in group2 can shake hands. That is the number of ways in which the choosen person can shake hands.

We need to repeat the above step for all the people in the circle, and the summation of all the result is our solution.

We need to define a base case. if there are 0 people then null is the only one ways in which they can shake hands. Therefore this would be our base case dp[0] = 1

Code based on above explaination :

class Solution:
    def numberOfWays(self, num_people: int) -> int:
        
        dp = dict()
        
        dp[0]=1 # Base Case
        
        def process(i):
            if i < 0 or i % 2 != 0: # As per question only even number of people can shake hands, for rest it would be zero
                return 0
            if i in dp:
                return dp[i]
            
            res = 0
            for j in range(1,i+1):
                res += process(j-1)*process(i-j-1)
							# Grp 1 * Grp 2
            dp[i] = res % (10**9 + 7)
            return dp[i]
        
        
        return process(num_people)
