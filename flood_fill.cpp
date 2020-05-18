/*

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
*/





class Solution {
    void dfs(vector<vector<int>>& image, int sr, int sc,int newColor,int rows,int cols,int source)
    {
        if(sr<0 || sr>=rows || sc<0 || sc>=cols)
            return;
        else if(image[sr][sc]!=source)
            return;
        
        image[sr][sc] = newColor;
        
        dfs(image,sr-1,sc,newColor,rows,cols,source);   //TOP
        dfs(image,sr+1,sc,newColor,rows,cols,source);   //DOWN
        dfs(image,sr,sc-1,newColor,rows,cols,source);   //LEFT
        dfs(image,sr,sc+1,newColor,rows,cols,source);   //RIGHT
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        
        if(newColor==image[sr][sc])
            return image;
        int rows = image.size();
        int cols = image[0].size();
        int source = image[sr][sc]; 
        dfs(image,sr,sc,newColor,rows,cols,source);
        return image;
    }
};
