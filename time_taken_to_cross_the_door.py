'''
There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second.

You are given a non-decreasing integer array arrival of size n, where arrival[i] is the arrival time of the ith person at the door. You are also given an array state of size n, where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door.

If two or more persons want to use the door at the same time, they follow the following rules:

If the door was not used in the previous second, then the person who wants to exit goes first.
If the door was used in the previous second for entering, the person who wants to enter goes first.
If the door was used in the previous second for exiting, the person who wants to exit goes first.
If multiple persons want to go in the same direction, the person with the smallest index goes first.
Return an array answer of size n where answer[i] is the second at which the ith person crosses the door.

Note that:

Only one person can cross the door at each second.
A person may arrive at the door and wait without entering or exiting to follow the mentioned rules.
'''



from heapq import heappush, heappop
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        cur, cur_state = 0, -1
        ques = [[],[]]
        ENTER, EXIT = 0, 1
        arrival.append(float('inf'))
        state.append(EXIT)
        res = [0]*len(arrival)
        for i, (t, s) in enumerate(zip(arrival, state)):
            while cur < t and (ques[0] or ques[1]):
                if cur_state == -1:
                    if ques[EXIT]:
                        j = heappop(ques[EXIT])
                        res[j] = cur 
                        cur_state = EXIT 
                    else:
                        j = heappop(ques[ENTER])
                        res[j] = cur 
                        cur_state = ENTER 
                elif cur_state == EXIT:
                    if ques[EXIT]:
                        j = heappop(ques[EXIT])
                        res[j] = cur 
                    else:
                        j = heappop(ques[ENTER])
                        res[j] = cur 
                        cur_state = ENTER
                else:
                    if ques[ENTER]:
                        j = heappop(ques[ENTER])
                        res[j] = cur 
                    else:
                        j = heappop(ques[EXIT])
                        res[j] = cur 
                        cur_state = EXIT 
                cur += 1
            heappush(ques[s], i)
            if cur < t: cur_state = -1
            cur = t
        res.pop()
        return res
------------------------------------------------------------------------------------
import collections


class Solution:
    def timeTaken(self, arrivals: list[int], states: list[int]) -> list[int]:
        n = len(arrivals)
        answer = [0] * n

        time, direction = 0, 1
        queues = [collections.deque(), collections.deque()]

        def exhaust_until(end_time: int=2*10**5) -> None:
            nonlocal time, direction
            while end_time > time and any(queues):
                if not queues[direction]:
                    direction ^= 1
                answer[queues[direction].popleft()] = time
                time += 1

        for index, (arrival, state) in enumerate(zip(arrivals, states)):
            exhaust_until(arrival)
            if arrival > time:
                time, direction = arrival, 1
            queues[state].append(index)

        exhaust_until()
        return answer
