'''
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.


Intuition
The first half part of palindrome is ordered.
Not leading zeros allowd, so ther starts with 100000, 100001, 100002..
Every number is added a base in pow of 10.


Explanation
Find the base that we need to add to every element.
The pow equals to the half of the length l.

For each query index q,
we firstly turn it q - 1, whichis 0-based index,
then add it with the base.

Finally we make it palindrome by add its reversed string.
'''

def kthPalindrome(self, queries: List[int], L: int) -> List[int]:
    l1=[]
    st=""
    if L%2==0:
        n=L//2-1
    else:
        n=L//2
    start=pow(10,n)
    for i in queries:
        ans=str(start+i-1)
        rev=ans[::-1]
        if L%2==0:
            st=ans+rev
        else:
            st=ans+rev[1:]
        if len(st)==L:
            l1.append(st)
        else:
            l1.append(-1)
    return l1
