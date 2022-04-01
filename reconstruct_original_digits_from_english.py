'''

Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

'''


class Solution:
    def originalDigits(self, s: str) -> str:
            zero = s.count('z')
            two = s.count('w')
            four = s.count('u')
            six = s.count('x')
            eight = s.count('g')

            one = s.count('o') - zero - two - four
            three = s.count('h') - eight
            five = s.count('f') - four
            seven = s.count('s') - six
            nine = s.count('i') - six - eight - five

            res = zero * "0" + one * '1' + two * '2' + three * '3' + four * \
                '4' + five * '5' + six * '6' + seven*'7' + eight*'8' + nine * '9'
            print(res)
            return res
