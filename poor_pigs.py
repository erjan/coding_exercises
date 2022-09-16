'''
There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

Choose some live pigs to feed.
For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time. Each pig can feed from any number of buckets, and each bucket can be fed from by any number of pigs.
Wait for minutesToDie minutes. You may not feed any other pigs during this time.
After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
Repeat this process until you run out of time.
Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.


Method: Math

Let T be the number of times to test so T = minutesToTest / minutesToDie
& p be the numbers of pigs to test in each round
& b be the maximum number of buckets that can be test.

First of all, we need to find out the relatioship between T and p.


For the example 1: T = 60 / 15= 4

When p = 1

At 0 mins: 
	- Feed pig with b1

At 15 mins: 
	- If pig dies, b1 is poisonous.
	- else feed pig with b2

At 30 mins: 
	- If pig dies, b2 is poisonous.
	- else feed pig with b3

At 45 mins: 
	- If pig dies, b3 is poisonous.
	- else feed pig with b4

At 60 mins: 
	- If pig dies, b4 is poisonous.
	- else b5 is poisonous.
Thus, when p = 1, b = 5 < 1000 buckets
If we stores those step into a matrix, it looks like:
image

When p = 2, the matrix looks like:
image

Then p1 would drink the buckets at each row in each round
& p2 would drink the buckets at each column in each round.

At 0 mins: 
	- Feed p1 with b1 + b2 + b3 +b4 + b5
	- Feed p2 with b1 + b6 + b11 + b16 + b21

At 15 mins: 
	- If p1 and p2 die, b1 is poisonous.
	- If p1 dies and p2 lives, one of b2 + b3 + b4 + b5 is poisonous
		- Feed b2 + b3 + b4 in the following rounds
	- If p1 lives and p2 dies, one of b6 + b11 + b16 + b21 is poisonous
		- Feed b6 + b11 + b16 in the following rounds
	- If p1 lives and p2 lives, 
		- Feed p1 with b6 + b7 + b8 + b9 + b10 (b6 is not poisonous, but put it here for easy-understanding)
		- Feed p2 with b2 + b7 + b12 + b17 + b22 (b2 is not poisonous, but put it here for easy-understanding)

And so on...
Thus, we can find that b = 25.

When p = 1 and T = 5,

b = 5 = T ^ 1
When p = 2 and T = 5,

b = 25 = T ^ 2
Thus, we can inference that
T ^ p ≥ buckets
p * log(T) ≥ log(buckets)
p ≥ log(T, buckets)
Thus, p = roundup(log(T, buckets))


'''

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets) / log(minutesToTest / minutesToDie + 1));
