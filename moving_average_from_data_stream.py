'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
'''



class MovingAverage:

    def __init__(self, size: int):
        
        self.st = list()
        self.le = size
        
        

    def next(self, val: int) -> float:
        if len(self.st) == 0:
            self.st.append(val)
            return self.st[0]
        
        elif len(self.st) < self.le:
            self.st.append(val)
            return sum(self.st)/ len(self.st)
        
        else:
            self.st.append(val)
            return sum(self.st[- self.le:])/ self.le
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
