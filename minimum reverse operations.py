'''
You are given an integer n and an integer p in the range [0, n - 1]. Representing a 0-indexed array arr of length n where all positions are set to 0's, except position p which is set to 1.

You are also given an integer array banned containing some positions from the array. For the ith position in banned, arr[banned[i]] = 0, and banned[i] != p.

You can perform multiple operations on arr. In an operation, you can choose a subarray with size k and reverse the subarray. However, the 1 in arr should never go to any of the positions in banned. In other words, after each operation arr[banned[i]] remains 0.

Return an array ans where for each i from [0, n - 1], ans[i] is the minimum number of reverse operations needed to bring the 1 to position i in arr, or -1 if it is impossible.

A subarray is a contiguous non-empty sequence of elements within an array.
The values of ans[i] are independent for all i's.
The reverse of an array is an array containing the values in reverse order.
 
 '''


This problem was hard to understand, and it has an O(K∗N)O(K * N)O(K∗N) issue that needs to be addressed.

Approach
The basic algorithm is a breadth-first search of positions, where depth is a reversal operation.

Avoid set lookups by marking banned positions with a -2 reduces the constant coefficient speed-up. This is not enough to avoid a TLE, however.
Every visited position has O(k)O(k)O(k) potential target positions. On visiting a new position, the multiplicative cost can be avoided by updating nextNode2s, which originally points forward 2, to point beyond all target positions considered for that position.
Complexity
Time complexity: O(n+k)O(n + k)O(n+k)

Space complexity: O(n)O(n)O(n)

Code
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        out = [-1] * n
        # To speed up iterations, mark banned positions differently; remember to
        # convert them to -1 at the end.
        for node in banned:
            out[node] = -2
        # Perform reversals in level-based breadth-first order.
        nodes = [p]
        depth = 0
        out[p] = depth
        step = k - 1
        
        # TLEs occur when n is large, k is large, and not to many are banned,
        # so that very O(N) points have O(N) possible post-reverse positions.
        # These O(N) post-reverse positions are 2 apart, but each only needs
        # to be visited once. We will nextNode2s dynamically to save work.
        nextNode2s = [i + 2 for i in range(n)]  # might be out of range

        while nodes:
            depth += 1
            newNodes = []
            for node1 in nodes:
                # The post-reverse positions are every other node between
                # loNode2 and hiNode2, inclusive.
                loReverseStart = max(node1 - step, 0)
                hiReverseStart = min(node1, n - k) # Inclusive
                loNode2 = 2 * loReverseStart + k - 1 - node1
                hiNode2 = 2 * hiReverseStart + k - 1 - node1  # Inclusive
                # We will exclude the entire range from future iterations
                # by setting nextNode2s[node2] to hiNode2 + 2 for every
                # visited node2.
                postHiNode2 = hiNode2 + 2
                node2 = loNode2
                while node2 <= hiNode2:
                    nextNode2 = nextNode2s[node2]
                    nextNode2s[node2] = postHiNode2
                    if node2 >= 0 and node2 < n and out[node2] == -1:
                        newNodes.append(node2)
                        out[node2] = depth
                    node2 = nextNode2
            nodes = newNodes
            
        # Mark all banned positions as -1 (see above).
        for i in range(n):
            if out[i] == -2:
                out[i] = -1
        return out
