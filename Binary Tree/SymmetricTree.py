# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Input: root = [1,2,2,3,4,4,3]
# Output: true


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def check(self,left, right):    
        if left == None and right == None: return True

        elif not left == None and not right == None:
            if left.val == right.val:
                return self.check(left.left,right.right) and self.check(left.right,right.left)
        
        return False
            
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, root)
        
    

        