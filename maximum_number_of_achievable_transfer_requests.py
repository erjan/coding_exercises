'''
We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.
'''

create all the possible combinations of requests
for each combination, check if the combination is possible, i.e. assume that all the transfers are made; the final inflow should be equal to the final outflow of each building
class Solution:
    @staticmethod
    def combination_possible(n, combination) -> bool:
        in_degree = [0] * n
        out_degree = [0] * n
        for node in combination: # node: (from, to)
            out_degree[node[0]] += 1
            in_degree[node[1]] += 1
        return in_degree == out_degree
    
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maximum_requests = 0
        for requestsIncluded in range(1, len(requests) + 1):
            for combination in list(combinations(requests, requestsIncluded)):
                if Solution.combination_possible(n, combination):
                    maximum_requests = requestsIncluded
                    continue
        return maximum_requests
