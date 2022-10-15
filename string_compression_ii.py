'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.
'''


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
		@cache
        def compress(idx, previous, previous_count, k):
            if idx == len(s): return 0
            
            # Current letter
            current = s[idx]
            
            if current == previous:
                length = 1 if previous_count == 1 or previous_count == 9 or previous_count == 99 else 0
                # Compress
                return length + compress(idx + 1, previous, previous_count + 1, k)

            # If new letter
            keep = 1 + compress(idx + 1, current, 1, k)
            delete = compress(idx + 1, previous, previous_count, k - 1) if k - 1 >= 0 else float('inf')
            return min(keep, delete)

        return compress(0, None, None, k)
        
-----------------------------------------------------------------------------------------------------------------------

def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

	@lru_cache(None)
	def compressed_length(seqlen):
		if not seqlen: return 0
		if seqlen == 1: return 1
		if seqlen < 10: return 2
		if seqlen < 100: return 3
		if seqlen < 1000: return 4

	@lru_cache(None)
	def min_length(from_idx=0, last_char='', last_count=0, remains=k):
		if from_idx >= len(s): return compressed_length(last_count)

		possible_lengths = []

		if remains:  # delete this one
			possible_lengths += [min_length(from_idx+1, last_char, last_count, remains-1)]
		if s[from_idx] == last_char: # keep it, dont compress yet
			possible_lengths += [min_length(from_idx+1, last_char, last_count+1, remains)]
		else: # compress the previous length
			possible_lengths += [min_length(from_idx+1, s[from_idx], 1, remains) + compressed_length(last_count)]

		return min(possible_lengths)

	return min_length()
