/*

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
*/




class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        //1st  value of pair denotes how many he trusts
        //2nd value of pair denotes how many trusts him
        vector<pair<int,int>> arr(N+1,{0,0});
        for(int i=0;i<trust.size();++i)
        {
            arr[trust[i][0]].first +=1;
            arr[trust[i][1]].second +=1;
        }
        
        //Now find who is trusted by N-1 others and he/she do not trusts others
        for(int i=1;i<=N;++i)
            if(arr[i].first==0 && arr[i].second==N-1)
                return i;
        
        return -1;
    }
};
