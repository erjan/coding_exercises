'''
You are given a list of blocks, where blocks[i] = t means that the i-th block needs t units of time to be built. A block can only be built by exactly one worker.

A worker can either split into two workers (number of workers increases by one) or build a block then go home. Both decisions cost some time.

The time cost of spliting one worker into two workers is given as an integer split. Note that if two workers split at the same time, they split in parallel so the cost would be split.

Output the minimum time needed to build all blocks.

Initially, there is only one worker.
'''



Code at end. Sorry in advance for typos, it's 2 am here in Australia, lol.

I initially though this was a dynamic programming question, and was even assuming I was aiming for O(n^2) because the max number of blocks is so low at 1000. Normally this means O(n^2). But after a little thinking, I realised this is not the best way to approach it at all. We can do it greedily!

We can model this entire question as a binary tree that we need to construct with a minimum max depth cost. Each of the blocks is a leaf node, with a cost of its face value. And then each inner node will be of cost split. nodes that are sitting at the same level represent work that is done in parallel. We know there will be len(blocks) - 1 of these inner nodes, so the question now is how can we construct the tree such that it has the minimum depth.

For example, a possible (not optimal) tree for the data set
[1, 2, 4, 7, 10] with split cost 3 is:
(Sorry for ascii art, 2 AM is too late at night to do this properly :) )

........3
...../....\
.....3.....\
../.....\....\
 3.......3....\
/..\..../..\...\
1...2...4...7...10

This tree has a maximum depth of 16 (3 -> 3 -> 3 -> 7).

So, how can we optimise the construction of this tree? Huffman's algorithm!

I'm going to assume you're familiar with Huffman's algorithm. If not, google it or read this. Note that it's traditionally used for building compression codes, but there is no reason we can't also use it here.
https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

Instead of actually building the whole tree, we can just keep track of the nodes the huffman algorithm still needs to consider, as the maximum depth below them. So put all the leaf node (blocks) onto a priority queue, and then repeatedly take the 2 smallest off and add split onto the biggest of the 2 (this is Huffman's algorithm, it's greedy) and put the result back onto the priority queue.

Once there is only one left, this is the depth of the root node, and we return it.

It is O(n-log-n) because we are making 2n - 1 insertions into a heap and n removals, and both heap insertion and removal have a cost of O(log-n). We drop the constants, giving a final cost of O(n-log-n).

And here is the code.

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            block_1 = heapq.heappop(blocks)
            block_2 = heapq.heappop(blocks)
            new_block = max(block_1, block_2) + split
            heapq.heappush(blocks, new_block)
        return blocks[0]
Small improvement: As kimS pointed out, we know that block_2 is the biggest, as the smallest came off the heap first. So we don't need that call to max, and we don't need to put block_1 into a variable. Thanks!
  
  
------------------------------------------
def minBuildTime(self, A, split):
        heapq.heapify(A)
        while len(A) > 1:
            x, y = heapq.heappop(A), heapq.heappop(A)
            heapq.heappush(A, y + split)
        return heapq.heappop(A)
      
------------------------------------------------------------
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            a = heapq.heappop(blocks)
            b = heapq.heappop(blocks)
            heapq.heappush(blocks, split + max(a, b))
        return heapq.heappop(blocks)
      
      
--------------------------------------------------------------------------
Let's binary search least amount of time needed to build the buildings. Suppose we asked to build in time time. Let's reproduce workers until we can, while building blocks that can't be prolonged building further, and see wheather we succeed for given time.

class Solution:
    def minBuildTime(self, blocks, split):
        blocks.sort(reverse=True)

        # greedily build in given time: reproduce till can, while build tallest buildings that cant be prolonged
        def can(time):
            # current time, current block to build, number of available workers
            cur, i, x = 0, 0, 1
            
            while True:
                if x >= len(blocks) - i:
                    return True

                # need to build this buildings right now
                while i < len(blocks) and blocks[i] + cur + split > time:
                    i += 1
                    x -= 1

                if x < 0:
                    return False
                if i == len(blocks):
                    return True
                if x == 0:
                    return False

                x = 2 * x
                cur = cur + split


        mx = max(blocks)
        l = mx - 1
        r = 10 * split + mx
        
        # binary search: r - amount of time in which guaranteed that can be build, l - guaranteed cannot
        while r - l >= 2:
            m = (l + r) // 2
            if can(m):
                r = m
            else:
                l = m

        return r
      
      
------------------------------------------------------------------------------
Dynamic Programming (Recursion + Memorization)
You might have read other posts using huffman algorithm, which is pretty brilliant, however, what will you do if you were facing a problem like this in a realy interview? There is no chances for you to read posts first. TBH, I didn't realize the huffman algorithm even getting AC.

Now I tell you a template using recursion to resolve most of hard problems that can be solved by DP. Well, in some terms DP is identical to recursion + memorization.

Note, I'm not saying this temple is always the optimal solution, but at least gives you a working approach, which is acceptable in intervew if you are being asked of questions like this.

Specific to this problem, the first intuiition is that we should use DP (or recursion + memorization) since we have perfect candidates for key used in memorziation, blocks and workers, where blocks represents the index of blocks to build, and the workers represents the number of workers.
Now we can think of the base case:

base case:
   block == 0: return 0 as no more blocks to build
	 worker == 0: return float('inf') as no workers to work
	 worker >= n - block: return max(block) as workers can build blocks in parallel.
otherwise:
    * we split: split + helper(i, workers * 2)
    * we build: max(block[i], helper(i + 1, workers  - 1))
then return min(split, build)
See the framework is done, and we see it passes the examples.
However, it causes TLE.
Why? We need some improvement, first of which is to sort the blocks first. Then we don't need return max(block) but block[i] instead. Because it's better to start building the larger blocks than smaller blocks.

Then the second improvement is that we build too slow by one step each time with sorted blocks max(block[i], helper(i + 1, workers - 1)). Because we know block[i] is the biggest one of remaining blocks, and the maximum time shouldn't be changed if there is no split. Then we can assign half of workers to start building and leave the rest of half for next split or continuing building. max(block[i], helper(i + workers / 2, workers / 2).
You might ask why half? I'd say intuition... another hints is that each split can double workers at the same time, then we might try to assign half of workers to work, and get back to the same number of workers by spliting the half of workers.

def minBuildTime(self, blocks: List[int], split: int) -> int:
	n = len(blocks)
    blocks.sort(reverse=True)
        
    @lru_cache(None)
    def helper(i, workers):
		if i >= n: 
			return 0
		if not workers:
			return float('inf')
		if n - i <= workers:
			return blocks[i]
		return min(max(blocks[i], helper(i + workers - workers // 2 , workers // 2)), helper(i, workers * 2) + split)
	return helper(0, 1)


-----------------------------------------------------------------------------------------------
Ideas from other posts:

Top down: 1s - 17/37
Bottom up: 500ms - 22/37.
TLE.
class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        blocks.sort(reverse=True)
        
        dp = [0] * (len(blocks)+1)
        
        for i in xrange(len(blocks)-1, -1, -1):
            dp[-1] = blocks[i]
            for k in xrange(len(blocks)-1, 0, -1):
                dp[k] = min(
                    max(blocks[i], dp[k-1]),
                    split + (dp[k*2] if k*2 < len(blocks) else blocks[i])
                )
            dp[0] = float('inf')
        
        return dp[1]
        
    def _minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        def dp(i, k):
            if (i, k) in memo: return memo[i, k]
            
            # no more blocks to build -> no time
            if i == len(blocks): memo[i, k] = 0; return 0
            # no more workers but still have blocks -> no way, inf
            if k == 0: memo[i, k] = float('inf'); return float('inf')
            # workers >= blocks -> build all in parallel -> time = max(blocks[i:]) = blocks[i]
            if k >= (len(blocks)-i): memo[i, k] = blocks[i]; return blocks[i]
            
            memo[i, k] = min(
                max(blocks[i], dp(i+1, k-1)), # build block i
                split + dp(i, k*2)            # split all workers
            )
            return memo[i, k]
       
        blocks.sort(reverse=True)
        memo = {}
        return dp(0, 1)
