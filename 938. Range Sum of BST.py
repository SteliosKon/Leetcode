# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.sum=0
        
        def BST(root):
            if root!=None:
                if root.val<=R and root.val>=L:
                    self.sum+=root.val
                BST(root.right)
                BST(root.left)
        
        BST(root)
        return self.sum
                
                    
        
        