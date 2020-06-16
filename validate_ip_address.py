'''
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each 
ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are 
separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit 
some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, 
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to 
pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, 
the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.
'''





class Solution:
    
    def validIPAddress(self, IP: str) -> str:
        def ip6(self,IP):
            s = IP
            hexdigits = '0123456789abcdefABCDEF'
            seven_colons = False
            seven_colons = s.count(':') == 7
            if seven_colons == False:
                return "Neither"
            hex_nums = s.split(':')

            for num in hex_nums:
                if len(num) == 0 or len(num) > 4:
                    return "Neither"

            for num in hex_nums:
                if num.isalnum() == False:
                    return "Neither"
            for num in hex_nums:
                for c in num:
                    if c not in hexdigits:
                        return 'Neither'
            return 'IPv6'
        
        def ip4(self,IP):
            three_dots = False
            bad_range = False
            leading_zero = False
            s = IP
            three_dots = s.count('.') == 3
            if three_dots == False:
                return "Neither"

            nums = s.split('.')

            for n in nums:
                if len(n) > 1 and n.startswith('0'):
                    leading_zero = True
                    return 'Neither'   

            for n in nums:
                if n.isdigit() == False:
                    return 'Neither'
                if int(n) < 0 or int(n) > 255:
                    bad_range = True
                    return 'Neither'

            return 'IPv4'
        
        res1 = ip4(self,IP)
        res2 = ip6(self,IP)
        if res1 == 'IPv4':
            return res1
        elif res2 == 'IPv6':
            return res2
        return 'Neither'
