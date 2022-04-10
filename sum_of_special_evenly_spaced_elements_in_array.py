'''
You are given a 0-indexed integer array nums consisting of n non-negative integers.

You are also given an array queries, where queries[i] = [xi, yi]. The answer to the 
ith query is the sum of all nums[j] where xi <= j < n and (j - xi) is divisible by yi.

Return an array answer where answer.length == queries.length and answer[i] is the answer to the ith query modulo 109 + 7.

'''

def solve(A, Q):
    n, M = len(A), 10**9+7
    m = int(n**0.5)+2
    P = [A[:] for _ in range(m)]
    for i in range(1,m):
        for j in range(n-1,-1,-1):
            if i+j < n:
                P[i][j] = (P[i][j]+P[i][i+j]) % M
    return [P[k][b] if k < m else sum(A[b::k])%M for b, k in Q]
  
  
  It took me a few mins to write a brute force solution, but a couple hours to get an optimized solution.

My final solution runtime was 4668 ms (Solution at the bottom)

Lets start with the brute force one:

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        answer = []
        
        for xi, yi in queries:
            _sum = 0
            for j in range(len(nums)):
                if xi <= j < n and (j - xi) % yi == 0:
                    _sum += nums[j]
            answer.append(_sum % (10**9 + 7))
        
        return answer
As you can see its pretty much direct translation of the question, there is nothing too much to say here.

But when I look at this part:

            _sum = 0
            for j in range(len(nums)):
                if xi <= j < n and (j - xi) % yi == 0:
                    _sum += nums[j]
I can see that there is definitely room for optimization. since the index of nums must be always equal than xi, when we start the loop to get the sum we can start from the index xi directly!
And when looking at the part (j - xi) % yi == 0 this is basically saying that the index minux xi must be multiply of yi, which makes the yi to be the step size of the loop, this is a great news because when we loop to get the sum we can use step size of yi to speed up.
And we can also use the builtin sum and list slice to get what we want, so I come up with this optimized solution:

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        answer = []
        
        for xi, yi in queries:
            _sum = nums[xi]
            if n - xi >= yi:
                _sum += sum(nums[xi+yi: n: yi])

            answer.append(_sum % (10**9 + 7))
        
        return answer
Well unfortunately this still doesn't pass.

Look again on the failed test, it was a TLE which means the input is too long for my current loop to work, and the only slow park of the current algorithm is the sum part! So lets takea look at the sum part.

As we discovered earlier, the yi is the step size of the loop, which controls how many elements we can skip. So intuitively, if the step size is really large, then the calculation steps are very less, which makes the speed really fast, and vice versa.

For example, lets say we have an array of 1000 elements. When we calculate the sum, if the step size is 1000, then we only do 1 calculation, which is to add the first and last element. However, if the step size is 1, then we have to add all 1000 elements altogether, so that's 1000 calculations.

Knowing this, there must be some room to improve there, and from the hint we know this magic number is sqrt(n) (you can mathmatical approve this but I'll skip here). So this becomes clear that in the for loop we need to check the valu of yi, then our logic becomes this:

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mod = 10**9 + 7
        
        qualify_pairs = {(xi, yi) for xi, yi in queries if yi > sqrt(n)}
        pre_processed_pairs = {(xi, yi): sum(nums[xi: n: yi]) for xi, yi in qualify_pairs}
        
        answer = []
        for xi, yi in queries:
            if yi > sqrt(n):
                answer.append(pre_processed_pairs[(xi, yi)] % mod)
            else:
				# We need to do something here to optimize the small step size
        
        return answer
So the only problem is how to optimize the loop for small step size.
Think about this for a bit, the variables here are really just two: the step size and our starting position in array, since we know the step size, we just need to find the starting position in array, and we can make this pair a key in the hashmap to store the sums of different positions.

For exmaple, lets say we are start from 0, and the step size is 3, then the hashmap is
{(0, 3): [0, 0 + nums[0], 0 + nums[0] + nums[3], 0 + nums[0] + nums[3] + nums[6], .... ,]
Note that we need to add an zero to the first position of array for its to calculate correctly, because for each position in the array, its the sum of all values from the previous positions. Such way of doing calculation was inspired by the famous Fibonacci number.
And in this array, we can use index to get the sum from different starting point wiith the same step size, we can just do array[last index] - array[x device by y].

I learnt that this is actually an existing method to do calculations, and this method is called Prefix Sum Array, you can do a google search for details.

Then the solution becomes clear:

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mod = 10**9 + 7
        pre_sum_array = defaultdict(list)
        
        qualify_pairs = {(xi, yi) for xi, yi in queries if yi > sqrt(n)}
        pre_processed_pairs = {(xi, yi): sum(nums[xi: n: yi]) for xi, yi in qualify_pairs}
        
        answer = []
        for xi, yi in queries:
            if yi > sqrt(n):
                answer.append(pre_processed_pairs[(xi, yi)] % mod)
            else:
                start_point = xi % yi
                if (start_point, yi) not in pre_sum_array:
                    _sum = nums[start_point]
                    pre_sum_array[(start_point, yi)].extend([0, _sum])
                    
                    for x in range(start_point + yi, n, yi):
                        _sum += nums[x]
                        pre_sum_array[(start_point, yi)].append(_sum)

                answer.append(
                    (
                        pre_sum_array[(start_point, yi)][-1] - pre_sum_array[(start_point, yi)][xi // yi]
                    )
                    % mod
                )
        
        return answer
Runtime 6376 ms

Then I optimized it a bit to move the prefix sum calculation out of the loop, it becomes:

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mod = 10**9 + 7
        pre_sum_array = defaultdict()
        
        big_y_pairs = {(xi, yi) for xi, yi in queries if yi > sqrt(n)}
        big_y_pair_sums = {(xi, yi): sum(nums[xi: n: yi]) for xi, yi in big_y_pairs}
        
        pre_sum_array_keys = {(xi % yi, yi) for xi, yi in queries if yi <= sqrt(n)}
        
        for start_point, yi in pre_sum_array_keys: 
            _sum = nums[start_point]
            pre_sum_array[(start_point, yi)] = [0, _sum]
            for x in range(start_point + yi, n, yi):
                _sum += nums[x]
                pre_sum_array[(start_point, yi)].append(_sum)

        return [
            (
                big_y_pair_sums[(xi, yi)] 
                if yi > sqrt(n)
                else pre_sum_array[(xi % yi, yi)][-1] - pre_sum_array[(xi % yi, yi)][xi // yi]
            ) % mod
            for xi, yi in queries
        ]
