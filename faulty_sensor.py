'''

An experiment is being conducted in a lab. To ensure accuracy, there are two sensors collecting data simultaneously. You are given two arrays sensor1 and sensor2, where sensor1[i] and sensor2[i] are the ith data points collected by the two sensors.

However, this type of sensor has a chance of being defective, which causes exactly one data point to be dropped. After the data is dropped, all the data points to the right of the dropped data are shifted one place to the left, and the last data point is replaced with some random value. It is guaranteed that this random value will not be equal to the dropped value.

For example, if the correct data is [1,2,3,4,5] and 3 is dropped, the sensor could return [1,2,4,5,7] (the last position can be any value, not just 7).
We know that there is a defect in at most one of the sensors. Return the sensor number (1 or 2) with the defect. If there is no defect in either sensor or if it is impossible to determine the defective sensor, return -1.
'''


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        ans = -1
        
        fi = 0
        for i, values in enumerate(zip(sensor1, sensor2)):
            v1, v2 = values
            if v1 != v2:
                fi = i
                break
        
        # Treat sensor1 as correct
        if sensor1[fi+1:] == sensor2[fi:-1]:
            ans = 2
            
        # Treat sensor2 as correct
        if sensor2[fi+1:] == sensor1[fi:-1]:
            # If ans recognized as 1 which means impossible to determine            
            ans = 1 if ans < 0 else -1
            
        return ans
