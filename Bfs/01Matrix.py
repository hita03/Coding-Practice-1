# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # using BFS
        r = len(mat)
        c = len(mat[0])
        
        # defining double ended queue
        queue = deque()
        
        # first push all 0 valued elements into queue
        # because their distance is 0 always
        # queue elements are a pair form of the cell position => (x,y)
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    queue.append((i,j))
                
        
        # visited will have set elements of visited pairs.
        # it will only store unique position (property of set)
        visited = set() 
        
        # all 0s coordinate position are into visited 
        visited.update(queue)
        
        # stores level number in traversal
        count =0
        
        # bfs traversal
        while queue:
            for _ in range(len(queue)):
                
                # popping 1st coordinate element
                (x,y) = queue.popleft()
                
                # finding neighbour in i+1,j / i-1,j / i,j+1 / i,j-1
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx, yy = x+dx, y+dy
                    
                    # skip edge and visited coordinates
                    if (xx,yy) in visited or xx == r or yy == c or xx<0 or yy<0:
                        continue
                
                    # append and visit this neighbour coordinate
                    queue.append((xx,yy))
                    visited.add((xx,yy))
                
                
                # now update value of nearest 0 distance in mat
                if mat[x][y]!=0:
                    print(mat[x][y],count)
                    mat[x][y] = count

            # increasing level (of traversal) by 1
            count+=1        
       
        return mat
                
