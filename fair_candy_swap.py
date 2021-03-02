'''
Alice and Bob have candy bars of different sizes: A[i] is the size 
of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each 
so that after the exchange, they both have the same total 
amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar 
that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.
'''


# i did not solve it - получил ответ подсказку из видео федора меньшикова - разбор на 51 минуту!!! https://www.youtube.com/watch?v=cJG6anLR1H4
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a = A
        b = B
        suma = sum(a)
        sumb = sum(b)
        b_set = set(b)

        diff = int((suma - sumb)/2)
        for av in a:
            bv = av - diff
            if bv in b_set:
                return [av,bv]
