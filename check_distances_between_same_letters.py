'''
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

Return true if s is a well-spaced string, otherwise return false.
'''


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
            r = dict(zip(ascii_lowercase, distance))
            print(r)
            print()
            for k, v in r.items():
                if k not in s:
                    continue

                elif k in s:

                    print('letter %s' % k)
                    print('index at %s' % v)
                    print()
                    first = s.find(k)
                    second = s.rfind(k)
                    print('first %d' % first)
                    print('second %d ' % second)
                    print('second - first: %d' % (second-first))
                    if (second - first-1) != v:
                        print('bad')
                        return False
            print('true')
            return True
