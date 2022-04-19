'''
Alice and Bob take turns playing a game with Alice starting first.

In this game, there are n piles of stones. On each player's turn, the player should remove any positive number of stones from a non-empty pile of his or her choice. The first player who cannot make a move loses, and the other player wins.

Given an integer array piles, where piles[i] is the number of stones in the ith pile, return true if Alice wins, or false if Bob wins.

Both Alice and Bob play optimally.
'''


Approach 1 -- bitmask dp

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        mask = 0
        for i, x in enumerate(piles): mask |= x << 3*i
        
        @cache
        def fn(mask): 
            """Return True if current player can win by playing optimally."""
            for i in range(len(piles)): 
                val = (mask >> 3*i) & 7
                for k in range(1, val+1): 
                    mask0 = mask - (k << 3*i)
                    if not fn(mask0): return True 
            return False 
        
        return fn(mask)
class Solution {
public:
    bool nimGame(vector<int>& piles) {
        unordered_map<int, bool> memo; 
        
        function<bool(int)> fn = [&](int mask) {
            if (!memo.count(mask)) {
                memo[mask] = false; 
                for (int i = 0; i < piles.size(); ++i) {
                    int val = (mask >> 3*i) & 7; 
                    for (int x = 1; x <= val; ++x) 
                        if (!fn(mask - (x << 3*i))) return memo[mask] = true; 
                }
            }
            return memo[mask]; 
        }; 
        
        int mask = 0; 
        for (int i = 0; i < piles.size(); ++i) mask |= piles[i] << 3*i; 
        return fn(mask); 
    }
};
Approach 2 -- Sprague-Grundy Theorem

class Solution {
public:
    bool nimGame(vector<int>& piles) {
        int ans = 0; 
        for (auto& x : piles) ans ^= x; 
        return ans; 
    }
};

-----------------------------------------------


It is noted that piles like [3,2,1], [2,3,1], [1,2,3] are equivalent. So we can use sorted tuple to remove many duplicates which accelerates the search.

from functools import lru_cache
class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def helper(piles):
            if sum(piles)==0:
                return False
            
            piles = list(piles)
            
            for i in range(len(piles)):
                for j in range(1, piles[i]+1):
                    ## try every possible number of stones from piles[i]
                    piles[i] -= j
                    ## use sorted tuple to remove many duplicates
                    if not helper(tuple(sorted(piles))): 
                        return True
                    piles[i] += j ## backtracking
                    
            return False
        
        piles.sort()
        if helper(tuple(piles)):
            return True
        else:
            return False
-----------------------------------------------------

from functools import cache

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
		# make [1,2,3] to '123'
        return self.helper(''.join(map(str, piles)))
        
    @cache
    def helper(self, piles: str):
        if int(piles) == 0:
            return False # Lose if no pile to remove
        for i in range(len(piles)):
            p = int(piles[i])
            for x in range(p):
				# For each pile try to remove any number, if any can cause the opponent lose, then win.
                if not self.helper(piles[:i]+str(x)+piles[i+1:]):
                    return True
        return False
--------------------------------------------------------------------------

Since the number range only goes up to 7, it is obviously Octal numbers. So we can just directly use Octal Bitmask to do the memoization.

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        n = len(piles)
        piles.sort()
        
        def to_oct(num):
            res = str(oct(num))
            index = res.find('o')
            res = res[index + 1:]
            return ("0" * (n - len(res))) + res
        
        def win(key):
            cnt = 0
            for x in key:
                if x == '0':
                    cnt += 1
            return cnt == len(key) - 1
        
        @lru_cache(None)
        def dfs(num):
            s = to_oct(num)
            if win(s):
                return True
            for i in range(n):
                if s[i] == '0':
                    continue
                v = int(s[i])
                while v > 0:
                    v -= 1
                    next = s[:i] + str(v) + s[i + 1:]
                    next = "".join(sorted(next))
                    next = int(next, 8)
                    if not dfs(next):
                        return True
            return False
        
        piles = "".join(map(str, piles))
        res = dfs(int(piles, 8))
        dfs.cache_clear()
        return res
--------------------------------------------------------

class Solution:
    _memo = {}
    def nimGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        self.memo = self._memo
        return self.helper(piles, total)
    
    def helper(self, piles, total):
        if total == 0:
            return False
        
        string = self.encode(piles)
        if string in self.memo:
            return self.memo[string]
        
        for i in range(len(piles)):
            if piles[i] > 0:
                prev_val = piles[i]
                for take in range(1, prev_val+1):
                    piles[i] = prev_val - take
                    if not self.helper(piles, total-take):
                        piles[i] = prev_val
                        self.memo[string] = True
                        return True
                    piles[i] = prev_val
                
        self.memo[string] = False
        return False
    
    def encode(self, piles):
        string = ""
        for p  in piles:
            string += str(p) + " "
        return string.strip()
-------------------------------------------------------------

def nimGame(self, piles):
    ans = 0
    
    for i in piles:
        ans = ans^i
        
    return ans != 0
  
  
      
      
      
          
