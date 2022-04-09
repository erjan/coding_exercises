'''

An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character '.' splits the groups.

For example, the binary number 00001111 10001000 11111111 01101011 (spaces added for clarity) formatted as an IP address would be "15.136.255.107".
A CIDR block is a format used to denote a specific set of IP addresses. It is a string consisting of a base IP address, followed by a slash, followed by a prefix length k. The addresses it covers are all the IPs whose first k bits are the same as the base IP address.

For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20. Any IP address whose binary representation matches 01111011 00101101 0100xxxx xxxxxxxx, where x can be either 0 or 1, is in the set covered by the CIDR block.
You are given a start IP address ip and the number of IP addresses we need to cover n. Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the inclusive range [ip, ip + n - 1] exactly. No other IP addresses outside of the range should be covered.

Return the shortest list of CIDR blocks that covers the range of IP addresses. If there are multiple answers, return any of them.
'''

class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ip_parts = ip.split(".")
        converted_ip = 0
        for ip_part in ip_parts:
            converted_ip = converted_ip * 256 + int(ip_part)
        curr_ip = converted_ip
        
        res = []
        while n > 0:
            count = curr_ip & (-curr_ip)
            
            if count == 0:
                count = self.get_highest_one(n)
                
            while count > n:
                count /= 2
            
            res.append(self.getCIDR(curr_ip, count))
            n -= count
            curr_ip += count
        return res
    
    def getCIDR(self, curr_ip, count):
        ip_list = []
        for i in range(4):
            ip_list.append(str(curr_ip & 255))
            curr_ip = curr_ip >> 8

        length = 0
        while count > 0:
            count /= 2
            length += 1
        mask = 32 - (length - 1)
        return ".".join(ip_list[::-1]) + '/' + str(mask)
    
    def get_highest_one(self, n):
        length = 0
        while n > 1:
            n /= 2
            length += 1
        return 1 << length
