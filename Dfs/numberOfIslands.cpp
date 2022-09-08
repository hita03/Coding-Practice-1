// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]



class Solution {
public:
    void dfs(vector<vector<char>>& grid, int i, int j, int r, int c){
        if(i>=r || j>=c || i<0 || j<0 || grid[i][j]!='1' || grid[i][j]=='2') return;
        grid[i][j]='2'; //2 means its visited
        dfs(grid,i+1,j,r,c);
        dfs(grid,i-1,j,r,c);
        dfs(grid,i,j-1,r,c);
        dfs(grid,i,j+1,r,c);

    
    }
    int numIslands(vector<vector<char>>& grid) {
        
        int r = grid.size();
        if (r==0) return 0;
        int c = grid[0].size();
        
        int islands=0;
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(grid[i][j]=='1'){
                    
                    islands++;
                    dfs(grid,i,j,r,c);
                }
            }
        }
        return islands;
    }
};