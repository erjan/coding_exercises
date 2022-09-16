'''
There is an n x n 0-indexed grid with some artifacts buried in it. You are given the integer n and a 0-indexed 2D integer array artifacts describing the positions of the rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith artifact is buried in the subgrid where:

(r1i, c1i) is the coordinate of the top-left cell of the ith artifact and
(r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will excavate the cell (ri, ci), return the number of artifacts that you can extract.

The test cases are generated such that:

No two artifacts overlap.
Each artifact only covers at most 4 cells.
The entries of dig are unique.
'''

class Solution:
    def digArtifacts(self, n, artifacts, dig):

        #turn dig into set for easy (constant time) lookup later
        dig = set((r,c) for r,c in dig)

        count =0
        #check each position of the artifact
        for r1,c1, r2,c2 in artifacts:
            positions = set()
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    positions.add((r,c))

            #if all positions are dug up, add to result
            if all([pos in dig for pos in positions]):
                count+=1

        return count
      
-------------------------------------------------

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
	    # Time: O(max(artifacts, dig)) which is O(N^2) as every position in the grid can be in dig
		# Space: O(dig) which is O(N^2)
        result, dig_pos = 0, set(tuple(pos) for pos in dig)
        for pos in artifacts:
            if all((x, y) in dig_pos for x in range(pos[0], pos[2] + 1) for y in range(pos[1], pos[3] + 1)):     
                result += 1
        return result
      
----------------------------------------------------------------------

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        pos_to_artifacts = {} # (x, y) => artifact unique index
        artifacts_to_remaining = {} # artifact unique index to remaining spots for artifact to dig up
        results = 0
        
		# Each artifact is identified by a unique index.
        for id, artifact in enumerate(artifacts):
            start, end = (artifact[0], artifact[1]), (artifact[2], artifact[3])
            size = 0
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    pos_to_artifacts[(x, y)] = id
                    size += 1
            artifacts_to_remaining[id] = size
        
        for pos in dig:
            if tuple(pos) not in pos_to_artifacts:
                continue
            id = pos_to_artifacts[tuple(pos)]
            artifacts_to_remaining[id] = artifacts_to_remaining[id] - 1
            if artifacts_to_remaining[id] == 0:
                results += 1

        return results
