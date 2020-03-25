#An array is monotonic if it is either monotone increasing or monotone decreasing.

#An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

#Return true if and only if the given array A is monotonic.


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        
        inc = False
        dec = False
        for i in range(len(A)-1):
            if inc:
                if A[i] > A[i+1]:
                    #print('found decreasing! wrong!')
                    return False
            if dec:
                if A[i] < A[i+1]:
                    #print('found increasing! wrong!')
                    return False
            if A[i] == A[i+1]:
                continue
            elif A[i] > A[i+1]:

                dec=True
            elif A[i] < A[i+1]:
                inc = True
        if inc == False and dec == False:
            #print('same values')
            return True
        if inc:
            #print('increasing arr - ok')
            return True
        if dec:
            #print('decreasing arr - ok')
            return True
