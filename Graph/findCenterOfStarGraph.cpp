// There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

// You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

// Input: edges = [[1,2],[2,3],[4,2]]
// Output: 2
// Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
// Example 2:

// Input: edges = [[1,2],[5,1],[1,3],[1,4]]
// Output: 1


// C++

class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        map<int,int> vertex;
        int n = edges.size();
        int i;
        for(i = 1; i<= n+1; i++){
            vertex[i] = 0; 
        } 
        
        for(i = 0; i< n; i++){
            vertex[edges[i][0]] +=1;
            vertex[edges[i][1]] +=1;
        }
        
        for(i = 1; i< n+2; i++){
            cout<<vertex[i]<<endl;
            if(vertex[i]==n){
                return i;
            }
        }
        return -1;
    }
};


// PY

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        vertex ={}
        n = len(edges)
        
        for i in range(1,n+2):
            vertex[i] = 0;
        
        
        for i in range(n):
            vertex[edges[i][0]] +=1;
            vertex[edges[i][1]] +=1;
         
        
        for key in vertex:
            if vertex[key] == n:
                return key
        
        return -1