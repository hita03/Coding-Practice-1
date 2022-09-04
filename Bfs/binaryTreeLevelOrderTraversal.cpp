// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


// Example 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]
// Example 2:

// Input: root = [1]
// Output: [[1]]

// Example 3:
// Input: root = []
// Output: []

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
            
class Solution {
public:
    int height(TreeNode*root){
        int l,r;
        if(root==NULL) return -1;
        else{
            l=height(root->left);
            r=height(root->right);
        }
        if(l>r) return l+1;
        return r+1;
        
    }
    
    void funcn(TreeNode* root, int level, int currentLevel, vector<int> *li){
        if(root!=NULL){
            if(level==currentLevel) li->push_back(root->val);
            
            funcn(root->left,level,currentLevel+1,li);
            funcn(root->right,level,currentLevel+1,li);

        }
    }
        
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        int h = height(root);
        vector<vector<int>>res;
        vector<int>li;
        for(int i=0; i<=h; i++){
            funcn(root,i,0,&li);
            res.push_back(li);
            li.clear();
        }
        
        
        return res;
    }
};


//PYTHON

// # Definition for a binary tree node.
// # class TreeNode(object):
// #     def __init__(self, val=0, left=None, right=None):
// #         self.val = val
// #         self.left = left
// #         self.right = right


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        li=[]
        res=[]
        
        
        def height(root):
           
            if root is None:
                return -1
            else:
                l=height(root.left)
                r=height(root.right)
            
            if l>r:
                return l+1
            else:
                return r+1
            
        h=height(root)   
        
        
        def func(root,level,currentlevel,li):
            if not root:
                return
            if level == currentlevel:
                li.append(root.val)
            
            func(root.left,level,currentlevel+1,li)
            func(root.right,level,currentlevel+1,li)
        
        
        for i in range(h+1):
            func(root,i,0,li)
            print(li)
            res.append(li)
            li=[]
        
        return res 
        


