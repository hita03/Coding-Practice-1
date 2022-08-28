# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # using BFS
        r = len(grid)
        c = len(grid[0])
        fresh = 0
        if r==0:
            return -1
        
        # defining double ended queue
        queue = deque()
        
        # first push all 2 valued elements into queue
        # because they are always gonna be rotten
        # queue elements are a pair form of the cell position => (x,y)
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append((i,j))
                
                if grid[i][j]==1:
                    fresh+=1
        


        # stores level number in traversal
        # it also means the minutes that passes by with with some good oranges get rotten (unvisited cells become visited cells)
        count =0
        
        # bfs traversal        
        while queue and fresh>0:
            count+=1
            
            for _ in range(len(queue)):
                
                # popping 1st coordinate element
                (x,y) = queue.popleft()
                                
                    
                # finding neighbour in i+1,j / i-1,j / i,j+1 / i,j-1
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx, yy = x+dx, y+dy

                    # skip edge and visited coordinates (means those who are already rotten)
                    if xx == r or yy == c or xx<0 or yy<0 or grid[xx][yy]==0 or grid[xx][yy]==2:
                        continue

                    # if the nighbour is fresh     
                    # append and visit this neighbour coordinate
                    queue.append((xx,yy))
                    grid[xx][yy] = 2
                    fresh -=1


        if fresh ==0:
            return count
        else: return -1
                
        