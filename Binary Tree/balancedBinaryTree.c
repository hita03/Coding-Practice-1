#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

 // Definition for a binary tree node.
 struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 };
 

bool recursive(struct TreeNode* node);
int getHeight(struct TreeNode* node);
bool isBalanced(struct TreeNode* root){

    if(root == NULL) return true;
    return recursive(root);
}
bool recursive(struct TreeNode* node){
    
    if(node==NULL){
        return true;
    }
    int res = getHeight(node->left) - getHeight(node->right);
        printf("\nres: %d",res);
        if(res > 1 || res < -1){
            printf("ret false ");
            return false;
        } 
        if(!recursive(node->left)) return false;
        if(!recursive(node->right))return false;
        return true;

    
}

int getHeight(struct TreeNode* node){
    
    if(node==NULL) return -1;
    
    int l = getHeight(node->left);
    int r = getHeight(node->right);
    if(l>r) return l+1;
    else return r+1;

}