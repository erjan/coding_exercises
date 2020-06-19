'''
Given an array of citations sorted in ascending order 
(each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: 
"A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
'''


//NON-OPTIMAL METHOD
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int low=0,high=n,mid;
        int res;
        
        while(low<=high)
        {
            mid = low+(high-low)/2;
            int ub = lower_bound(citations.begin(),citations.end(),mid) - citations.begin();
            
            if(n-ub >= mid)
            {
                res = mid;
                low = mid+1;
            }
            else
                high = mid-1;
        }
        return res;
    }
};
