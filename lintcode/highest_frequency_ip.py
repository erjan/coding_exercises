'''

Given a string array lines, each element represents an IP address. Please find the IP address with the highest frequency.

'''


from typing import (
    List,
)

class Solution:
    """
    @param ip_lines: ip  address
    @return: return highestFrequency ip address
    """
    def highest_frequency(self, ip_lines: List[str]) -> str:
        # Write your code here
        d = dict()

        for ip in ip_lines:
            if ip not in d:
                d[ip] = 1
            else:
                d[ip] += 1

        d = list([k, v] for k, v in d.items())
        d.sort(key=lambda x: x[1], reverse=True)
        return d[0][0]
        
        
----------------------------------------

class Solution:
    """
    @param ipLines: ip  address
    @return: return highestFrequency ip address
    """
    def highestFrequency(self, ipLines):
        # Write your code here
        ans = ipLines[0]
        #使用mapdic记录每个IP出现的次数
        mapdic = {}
        for ip in ipLines:
            if ip in mapdic:
                mapdic[ip] += 1
            else:
                mapdic[ip] = 1
        max = 0
        #遍历mapdic得到频率最高的IP
        for key in mapdic:
            if int(mapdic[key]) > max:
                max = mapdic[key]
                ans = key
        return ans
