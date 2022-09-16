'''
You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 
 '''

class TopVotedCandidate:
    
    def __init__(self, persons: List[int], times: List[int]):
        self.topVoted = [0] * len(times)
        countVotes = Counter()
        currentTop = persons[0]
        
        for i, (person, time) in enumerate(zip(persons, times)):
            countVotes[person] += 1
            if countVotes[person] >= countVotes[currentTop]:
                currentTop = person
            self.topVoted[i] = (time, currentTop)

    def q(self, t: int) -> int:
        left, right = 0, len(self.topVoted) - 1
        
        while left <= right:
            mid = (left + right) // 2
            time, top = self.topVoted[mid]
            if time == t:
                return top
            if time < t:
                left = mid + 1
            else:
                right = mid - 1

        time, top = self.topVoted[right]
        return top
      
-------------------------------------------------------------------------

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        
        self.leading =[]
    
        self.times = []
        
        count = defaultdict(int)
        ma = 0
        
        for i , p in enumerate(persons):
            
            count[p]+=1
            
            if count[p]>= ma:
                
                ma= count[p]
                self.leading.append(p)
                self.times.append(times[i])
            
            
    def search(self, ar , target):
        l,r = 0,len(ar)-1
        while l<=r:
                
            mid = l+(r-l)//2
            if ar[mid] == target:
                return mid
            elif ar[mid] > target:
                r = mid-1
            else:
                l= mid+1
        return l-1
        
        

    def q(self, t: int) -> int:
        
        index = self.search(self.times, t)
        return self.leading[index]
        
