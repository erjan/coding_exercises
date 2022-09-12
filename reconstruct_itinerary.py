'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
'''


class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      graph = {}
      # Create a graph for each airport and keep list of airport reachable from it
      for src, dst in tickets:
          if src in graph:
              graph[src].append(dst)
          else:
              graph[src] = [dst]

      for src in graph.keys():
          graph[src].sort(reverse=True)
          # Sort children list in descending order so that we can pop last element 
          # instead of pop out first element which is costly operation
      stack = []
      res = []
      stack.append("JFK")
      # Start with JFK as starting airport and keep adding the next child to traverse 
      # for the last airport at the top of the stack. If we reach to an airport from where 
      # we can't go further then add it to the result. This airport should be the last to go 
      # since we can't go anywhere from here. That's why we return the reverse of the result
      # After this backtrack to the top airport in the stack and continue to traaverse it's children

      while len(stack) > 0:
          elem = stack[-1]
          if elem in graph and len(graph[elem]) > 0: 
              # Check if elem in graph as there may be a case when there is no out edge from an airport 
              # In that case it won't be present as a key in graph
              stack.append(graph[elem].pop())
          else:
              res.append(stack.pop())
              # If there is no further children to traverse then add that airport to res
              # This airport should be the last to go since we can't anywhere from this
              # That's why we return the reverse of the result
      return res[::-1]
-----------------------------------------------------------------------------------------------------------------------  


def findItinerary(self, tickets):
    d = defaultdict(list)
    for flight in tickets:
        d[flight[0]] += flight[1],
    self.route = ["JFK"]
    def dfs(start = 'JFK'):
        if len(self.route) == len(tickets) + 1:
            return self.route
        myDsts = sorted(d[start])
        for dst in myDsts:
            d[start].remove(dst)
            self.route += dst,
            worked = dfs(dst)
            if worked:
                return worked
            self.route.pop()
            d[start] += dst,
    return dfs()
