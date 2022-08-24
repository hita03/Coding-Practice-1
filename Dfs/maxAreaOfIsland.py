# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
class Solution(object):
    
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
          
        m= len(grid)
        n= len(grid[0])
        i=0
        j=0
        areas={}
        x=0
        
        def dfs(i, j, m,n,grid ):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                grid[i][j]=0
                return 1+ dfs(i+1, j,m,n,grid) + dfs(i-1, j,m,n,grid) + dfs(i,j+1,m,n,grid) + dfs(i,j-1,m,n,grid)
            return 0  
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    areas[x]=dfs(i,j,m,n,grid)
                    x+=1
        
        if areas:
            print(areas.items())
            return max(areas.values())
        else:
            return 0    
       
        