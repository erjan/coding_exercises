'''
You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").

Find the number of unique good subsequences of binary.

For example, if binary = "001", then all the good subsequences are ["0", "0", "1"], so the unique good subsequences are "0" and "1". Note that subsequences "00", "01", and "001" are not good because they have leading zeros.
Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        f0 = f1 = 0
        for ch in binary: 
            if ch == "0": f0 += f1
            else: f1 += f0 + 1
        return (f0 + f1 + int("0" in binary)) % 1_000_000_007
