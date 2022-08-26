// An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

// You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

// To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

// Return the modified image after performing the flood fill.

// Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
// Output: [[2,2,2],[2,2,0],[2,0,1]]
// Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
// Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
// Example 2:

// Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
// Output: [[0,0,0],[0,0,0]]
// Explanation: The starting pixel is already colored 0, so no changes are made to the image.




class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
//     if(image[sr][sc]== newColor) return image;
//     int rows = image.size();
//     int cols = image[0].size();
//     vector<int> visited;
//     for(int i=0; i<rows*cols; i++) visited.push_back(0);  
//     // for(auto j= visited.begin(); j!= visited.end(); j++) cout<<visited[*j]<<" ";    
    
//     dfs(image,cols,image[sr][sc],newColor, visited);
 
//     for(auto j= visited.begin(); j!= visited.end(); j++) cout<<visited[*j]<<" ";    
//     return image;
//     }
    
//    void dfs(vector<vector<int>>& image,int cols, int v, int newColor, vector<int> &visited){
//         visited[v]=1;
        
//         for(auto j= visited.begin(); j!= visited.end(); j++) cout<<visited[*j]<<" ";    
//         cout<<endl;
//         for (int i = 0; i < cols; ++i)
//             if (!visited[image[v][i]]){
                
//                 dfs(image, cols,image[v][i],newColor,visited);
//             }                   
//     }
        
      int val = image[sr][sc];        
      dfs(image, sr,sc, val, newColor);  
      return image;  
        
    }
    
    void dfs(vector<vector<int>>& image, int sr, int sc, int val, int newColor) {
    
        if(sr >= image.size() || sr<0 || sc>= image[0].size() || sc<0 || image[sr][sc]!=val || image[sr][sc]== newColor){
            return;
        }
         image[sr][sc]=newColor;
        
         dfs(image, sr+1, sc, val, newColor);
         dfs(image, sr-1, sc, val, newColor);
         dfs(image, sr, sc+1, val, newColor);
         dfs(image, sr, sc-1, val, newColor);
        
    }
};