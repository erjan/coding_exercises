'''

We have an integer array nums, where all the integers in nums are 0 or 1. You will not be given direct access to the array, instead, you will have an API ArrayReader which have the following functions:

int query(int a, int b, int c, int d): where 0 <= a < b < c < d < ArrayReader.length(). The function returns the distribution of the value of the 4 elements and returns:
4 : if the values of the 4 elements are the same (0 or 1).
2 : if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
0 : if two element have a value equal to 0 and two elements have a value equal to 1.
int length(): Returns the size of the array.
You are allowed to call query() 2 * n times at most where n is equal to ArrayReader.length().

Return any index of the most frequent value in nums, in case of tie, return -1.
'''

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        """
        Sliding Window with 2 known
        
        Complexities:
            Time: O(N), N - length of the hidden array
            Space: O(1)
        """
        first, slide, corner = reader.query(0, 1, 2, 3), reader.query(1, 2, 3, 4), reader.query(0, 1, 3, 4)
        N = reader.length()
        
        if first == 4 or slide == 4 or corner == 4:
            if corner == 4:
                a, b = 0, 1
            else:
                a, b = 1, 2
            
        elif (first == 0 and slide == 0) or (first == 2 and slide == 2):
            a, b = 0, 4
        
        else:
            if (first == 2 and slide == 0):
                a, b = 0, 2 if corner == 0 else 1
            elif first == 0 and slide == 2 and corner == 2:
                a, b = 0, 2
            else:
                a, b = 2, 4
            
        one, another = 2, 0
        one_index, another_index = a, None
        x, y = 0, 0
        y_was = -1
        
        while x < N and y < N:
            if x in [a, b, y_was]:
                x += 1
                continue
                
            if y in [a, b]:
                y += 1
                continue
            
            if x == y:
                y += 1
                continue
                            
            call = reader.query(*sorted([a, b, x, y]))
            
            if call == 4:
                one += 2
            elif call == 2:
                one += 1
                another += 1
            else:
                another += 2
                another_index = x if another_index is None else another_index
            
            y_was = y
            x += 2
            y += 2
        
          
        if N % 2 and another_index is not None:
            call = reader.query(*sorted([a, b, another_index, x if x != y_was else y_was + 1]))
            
            if call == 2:
                one += 1
            else:
                another += 1
                                
        return -1 if one == another else (one_index if one > another else another_index)
      
--------------------------
class Solution {
    
    int replaceAndQuery(ArrayReader r, int[] a, int i, int v) {
        int t = a[i];
        for(int j = i; j < 3; j++) {
            a[j] = a[j+1];
        }
        a[3] = v;
        int q = r.query(a[0], a[1], a[2], a[3]);
        for(int j = 3; j > i; j--) {
            a[j] = a[j-1];
        }
        a[i] = t;
        return q;
    }
    
    // use the first 5 numbers to find three same numbers
    // record the counts
    // use the three same numbers to test all the remaining numbers and adjust the counts.
    public int guessMajority(ArrayReader reader) {
        int[] a = new int[] {0, 1, 2, 3};
        int n = reader.length();
        int idx1 = -1, cnt1 = 0, idx2 = -1, cnt2 = 0;
        int q = reader.query(a[0], a[1], a[2], a[3]);
        if (q == 4) {
            // all 4 numbers are the same
            idx1 = 3;
            cnt1 = 4;
            a[3] = 4;
        } else if (q == 2) {
            // there are 3 same numbers and one different
            // use the 5th number to tell them apart
            // replace each number with the 5th number and query
            // to find out if the number is the same as the 5th
            // find the majority from the same number count.
            boolean[] same = new boolean[4];
            int sameCount = 0;
            for(int i = 0; i < 4; i++) {
                if (replaceAndQuery(reader, a, i, 4) == 2) {
                    same[i] = true;
                    sameCount++;
                }
            }
            
            if (sameCount == 3) {
                cnt1 = 4; cnt2 = 1;
                for(int i = 0; i < 4; i++) {
                    if (!same[i]) {
                        idx2 = i;
                    } else {
                        idx1 = i;
                    }
                }
            } else { // sameCount == 1
                cnt1 = 3; cnt2 = 2;
                for(int i = 0; i < 4; i++) {
                    if (!same[i]) {
                        idx1 = i;
                    } else {
                        idx2 = i;
                    }
                }
            }
            for(int i = idx2; i < 3; i++) {
                a[i] = a[i+1];
            }
            a[3] = 5;            
        } else { // q == 0
            // evenly split
            // the 5th number plus the two same ones will form the 3-number group
            cnt1 = 3; cnt2 = 2;
            idx1 = 4;
            int[] same = new int[4];
            int j = 0;
            for(int i = 0; i < 4; i++) {
                if (replaceAndQuery(reader, a, i, 4) == 0) {
                    same[j++] = i;
                } else {
                    idx2 = i;
                }
            }
            a = same;
            a[2] = 4;
            a[3] = 5;
        }
                
        for(int i = a[3]; i < n; i++) {
            a[3] = i;
            if (reader.query(a[0], a[1], a[2], a[3]) == 4) {
                cnt1++;
            } else {
                if (idx2 == -1) idx2 = i;
                cnt2++;
            }
        }
        
        return cnt1 == cnt2 ? -1 : cnt1 > cnt2 ? idx1 : idx2;
    }
}
