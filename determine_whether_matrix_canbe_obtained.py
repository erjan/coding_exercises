'''
Given two n x n binary matrices 
mat and target, return true if it 
is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
'''

class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        vector<vector<int>>a=mat;
        
        if (mat==target)
        {
            return true;
        }
        
        
        // 1st rotation
        
        for (int i=0;i<mat.size();i++)
        {
            for (int j=0;j<mat[0].size();j++)
            {
                a[j][mat[0].size()-1-i]=mat[i][j];
            }
        }
        
        if (a==target)
        {
            return true;
        }
        
        mat=a;
        
        
        // 2nd rotation
        
         for (int i=0;i<mat.size();i++)
        {
            for (int j=0;j<mat[0].size();j++)
            {
                a[j][mat[0].size()-1-i]=mat[i][j];
            }
        }
        
        if (a==target)
        {
            return true;
        }
        
        mat=a;
       
        
        // 3rd rotation
        
         for (int i=0;i<mat.size();i++)
        {
            for (int j=0;j<mat[0].size();j++)
            {
                a[j][mat[0].size()-1-i]=mat[i][j];
            }
        }
        
        if (a==target)
        {
            return true;
        }
        
       
        return false;

    }
};
