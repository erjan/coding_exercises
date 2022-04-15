'''
You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Implement the LogSystem class:

LogSystem() Initializes the LogSystem object.
void put(int id, string timestamp) Stores the given log (id, timestamp) in your storage system.
int[] retrieve(string start, string end, string granularity) Returns the IDs of the logs whose timestamps are within the range from start to end inclusive. start and end all have the same format as timestamp, and granularity means how precise the range should be (i.e. to the exact Day, Minute, etc.). For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", and granularity = "Day" means that we need to find the logs within the inclusive range from Jan. 1st 2017 to Jan. 2nd 2017, and the Hour, Minute, and Second for each log entry can be ignored.
'''

class LogSystem(object):

    def __init__(self):
        self.log = {} # Define a dictionary to store all log information

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        
        # Add the id and timestamp into the dictionary, split the timestamp base on granularity
        self.log[id] = timestamp.split(":") 

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        output = []
        
        # Split the start and end time strings
        start_string = s.split(":")
        end_string = e.split(":")
        
        # Create a granularity dictionary to store time-based index
        granularity = {"Year":0, "Month":1, "Day":2, "Hour":3, "Minute":4, "Second":5}
        
        # Convert the time string into a integer for comparison
        start_time = int(''.join(start_string[:granularity[gra]+1]))
        end_time = int(''.join(end_string[:granularity[gra]+1]))
        
        # For each log in storage, check whether it is within the time range
        for k, v in self.log.items():
            if int(''.join(v[:granularity[gra]+1]))>=start_time and int(''.join(v[:granularity[gra]+1]))<=end_time:
                output.append(k)

        return output
      
------------------------------------
class LogSystem:

    def __init__(self):
        self.logs = []
        self.granLookup = {"Year":5, "Month":8, "Day":11, "Hour":14, "Minute":17, "Second":20}
        self.timeStampLength = 19

    def put(self, id: int, timestamp: str) -> None:
        # add the log data in a sorted manner using bisect.insort
        bisect.insort(self.logs, (timestamp, id))
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        result = []
        # find the index of position in timestamp
        index = self.granLookup[granularity]
        # Append with 0 since that is lowest ascii char for digits. We want the left most position
        start = start[:index] + ("0" * (self.timeStampLength-index))
        # append A at end since ascii value of A is larger than any digit
        end = end[:index] + ("A" * (self.timeStampLength-index))
        # find the leftmost position
        leftIndex = bisect.bisect_left(self.logs, (start, -math.inf))
        # start from leftIndex since rightindex will always be greater (log is sorted based on timestamp)
        rightIndex = bisect.bisect_right(self.logs, (end, math.inf), leftIndex)
        # extract the ids from leftindex to rightindex -1 
        for ind in range(leftIndex, rightIndex):
            # second value of tuple is id
            result.append(self.logs[ind][1])
        return result
-------------------------------------------------------------------------------------------------

Explanation
Prettry straightforward question, but make sure you read the question carefully.
e.g.
As question described, retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")
Need to return every logs happened in 2016 and 2017, NOT between 2016 and 2017
Or in another way return logs between the beginning of 2016 and the end of 2017
That is, for any time within [2016:00:00:00:00:00, 2017:59:59:59:59:59] inclusive
Everytime we got a start & end, we modify the start & end time accordingly to the granularity, as explained above
Then iterate the dictionary to find valid log_id with timestamp in that range
Implementation
class LogSystem:
    def __init__(self):
        self.d = collections.defaultdict(int)                                 # {timestamp: log_id}
        self.gra_start = {'Year': 1, 'Month': 2, 'Day': 3, 'Hour': 4, 'Minute': 5, 'Second': 6} # start index for changing granularity

    def put(self, log_id: int, timestamp: str) -> None:
        self.d[timestamp] = log_id                                            # set time: id

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        s, e = s.split(':'), e.split(':')                                     # split timestamp for easier update
        for i in range(self.gra_start[gra], 6): s[i], e[i] = '00', '59'       # update start/end timestamp boundary
        s, e = ':'.join(s), ':'.join(e)                                       # re-join to string
        return [log_id for time, log_id in self.d.items() if s <= time <= e]  # O(n) iterative
      
-------------------------------------------------------------------------------
from sortedcontainers import SortedDict
class LogSystem:

    def __init__(self):
        self.map = SortedDict(list)
        self.gra = {
            'Year': 5,
            'Month':8,
            'Day':11,
            'Hour': 14,
            'Minute':17,
            'Second':20,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.map.setdefault(timestamp, []).append(id)
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.gra[granularity]
        left = self.map.bisect_left(start[:idx]) 
        
        result = []
        for i in range(left, len(self.map)):   # DO NOT USE bisect to find right, it may only granular to year, but date exceeds
            key = self.map.keys()[i]
            if key[:idx]>end[:idx]: break
            
            result.extend(self.map[key])
        return result
      
-------------------------------------------------------------
class LogSystem:

    def __init__(self):
        self.logs=[]

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((timestamp,id))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        index={"Year":5,"Month":8,"Day":11,"Hour":14,"Minute":17,"Second":20}[gra]
        s,e=s[:index],e[:index]
        res=[]
        for tm in sorted(self.logs):
            if s<=tm[0][:index]<=e: res.append(tm[1])
        return res
