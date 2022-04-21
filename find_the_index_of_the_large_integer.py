'''
We have an integer array arr, where all the integers in arr are equal except for one integer which is larger than the rest of the integers. You will not be given direct access to the array, instead, you will have an API ArrayReader which have the following functions:

int compareSub(int l, int r, int x, int y): where 0 <= l, r, x, y < ArrayReader.length(), l <= r and x <= y. The function compares the sum of sub-array arr[l..r] with the sum of the sub-array arr[x..y] and returns:
1 if arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y].
0 if arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y].
-1 if arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y].
int length(): Returns the size of the array.
You are allowed to call compareSub() 20 times at most. You can assume both functions work in O(1) time.

Return the index of the array arr which has the largest integer.

 

Example 1:

Input: arr = [7,7,7,7,10,7,7,7]
Output: 4
Explanation: The following calls to the API
reader.compareSub(0, 0, 1, 1) // returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with arr[1]).
Thus we know that arr[0] and arr[1] doesn't contain the largest element.
reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
Notice that we made only 3 calls, so the answer is valid.
Example 2:

Input: nums = [6,6,12]
Output: 2
'''

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (hi - lo + 1) % 2 == 0:
                compare = reader.compareSub(lo, mid, mid + 1, hi)
            else:
                compare = reader.compareSub(lo, mid, mid, hi)
            
            if compare < 0:
                lo = mid + 1
            else:
                hi = mid
                
        return lo
      
-------------------------------

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        def binSearch(left, right, reader):
            if left >= right:
                return left
            
            total = left + right
            mid = total // 2
            if total % 2 == 0:
                flag = reader.compareSub(left, mid, mid, right)
                if flag == 0:
                    return mid
            else:
                flag = reader.compareSub(left, mid, mid + 1, right)
            
            if flag == 1:
                return binSearch(left, mid, reader)
            else:
                return binSearch(mid + 1, right, reader)
        
        return binSearch(0, reader.length() - 1, reader)
-------------------------------------

Just a regular binary search, with two caveats:

The lengh of two halfs should be the same.
Go "down" only if the biggest number is in the left half.
Otherwise, it can be in the right part (-1) or it's the last element in the case of odd intervals.
We can add a special check for 0 and exit earlier, but sorry - #minimalizm.
Java (and also C++ and C#)
Adding C# because there is a bug in C# code definition.

// Pascal-case all functions for C#: GetIndex, Length, CompareSub
// int getIndex(ArrayReader &rd) { // use for C++
public int getIndex(ArrayReader rd) { // use for Java and C#
    int l = 0, r = rd.length() - 1;
    while (l < r) {
        int h = (r - l + 1) / 2; // half, h * 2 <= r - l + 1
        if (rd.compareSub(l, l + h - 1, l + h, l + h * 2 - 1) != 1)
            l = l + h;
        else
            r = l + h - 1;
    }
    return l;
}
Python

class Solution:
    def getIndex(self, rd: 'ArrayReader') -> int:
        l, r = 0, rd.length() - 1
        while l < r:
            h = (r - l + 1) // 2  # half, h * 2 <= r - l + 1
            if rd.compareSub(l, l + h - 1, l + h, l + h * 2 - 1) != 1:
                l = l + h
            else:
                r = l + h - 1
        return l
------------------------------------------------------------------------------
                                  
Binary Search, each time calculate interval length:

If length%2==0, our mid will be 1 index to the left of the exact middle so search between (L and mid) and (mid+1 and R)
If length%2!=0, our mid will be the index of the exact middle so search between (L and mid-1) and (mid+1 and R):
if both sides are equal, the value is in mid
If anywhere in the while loop, L==R means the value is in both our pointers and we've reached the end, so we return any of them
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l=0
        r=reader.length()-1
        while l<=r:
            mid = (l+r)//2
            if (r-l+1)%2==0:
                num=reader.compareSub(l,mid,mid+1,r)
                if num==1:
                    r=mid
                else:
                    l=mid+1
            else:
                num=reader.compareSub(l,mid-1,mid+1,r)
                if num==0:
                    return mid
                elif num==1:
                    r=mid-1
                else:
                    l=mid+1
            if l==r:
                return l
----------------------------------------------------------------------
                                  
Explanation
We start with the whole list
If the length is odd, say middle point is mid
Then we compare (left, mid-1) to (mid+1, right)
If return 1: right = mid-1
If return -1: left = mid+1
If return 0: return mid
If the length is even
Take whichever side is larger, meaning change left or right accordingly
If left == right: return left (or right)
Implementation
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        l, r = 0, n-1
        for _ in range(20):
            mid = (r+l+1) // 2
            if (r-l+1) % 2:
                cmp = reader.compareSub(l, mid-1, mid+1, r)
                if not cmp: return mid
                elif cmp > 0: r = mid-1
                else: l = mid+1
            else:        
                cmp = reader.compareSub(l, mid-1, mid, r)
                if cmp > 0: r = mid-1
                else: l = mid
            if r == l: return l
        return -1
                                  
                                  
                                  
                                  
      
      
