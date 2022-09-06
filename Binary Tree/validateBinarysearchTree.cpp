

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
//      bool funcn(TreeNode* curNode) {
//         if(curNode!=NULL){
//             // cout<<curNode->val<<endl;
//             if(curNode->left){
//                 cout<<curNode->val <<" "<<curNode->left->val<<endl;
//                 if(curNode->val <= curNode->left->val) return false;
//             }
            
//             if(curNode->right){
//                 cout<<"r: ";
//                 cout<<curNode->val <<" "<<curNode->right->val<<endl;

//                 if(curNode->val >= curNode->right->val) return false;
//             }
            
//         }
//         if(curNode->left)funcn(curNode->left);
//         if(curNode->right)funcn(curNode->right);
//         return true;
//     }
// };
class Solution {
public:    
    void traverse(TreeNode* root,vector<int>*tree){
        if(root==NULL) return;
        traverse(root->left,tree);
        tree->push_back(root->val);
        traverse(root->right,tree);
    }
    bool isValidBST(TreeNode* root) {
        
        vector<int> tree;
        traverse(root, &tree);
        for(int i=0; i< tree.size()-1;i++){
            if(tree[i]>=tree[i+1]) return false;
        }
        return true;
    }   
};
    
   
