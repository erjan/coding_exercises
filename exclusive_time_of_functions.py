'''
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

 
 '''

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        helper = lambda log: (int(log[0]), log[1], int(log[2])) # to covert id and time to integer
        logs = [helper(log.split(':')) for log in logs]         # convert [string] to [(,,)]
        ans, s = [0] * n, []                                    # initialize answer and stack
        for (i, status, timestamp) in logs:                     # for each record
            if status == 'start':                               # if it's start
                if s: ans[s[-1][0]] += timestamp - s[-1][1]     # if s is not empty, update time spent on previous id (s[-1][0])
                s.append([i, timestamp])                        # then add to top of stack
            else:                                               # if it's end
                ans[i] += timestamp - s.pop()[1] + 1            # update time spend on `i`
                if s: s[-1][1] = timestamp+1                    # if s is not empty, udpate start time of previous id; 
        return ans
      
-------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        
        f = [0]*(n)
        
        
        stack=[]
        
        
        for i in logs:
            
            ID,pos,time = i.split(':')
            
            ID= int(ID)
            time= int(time)
            if pos == 'start':
                
                stack.append([ID,time])
            else:
                
                prID, prtime = stack.pop()
                
                timespent = time-prtime+1
                f[ID]+= timespent
                
                #remove the overlapping time 
                
                if stack:
                    f[stack[-1][0]]-= timespent
                    
        return f
