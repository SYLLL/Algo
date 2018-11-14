#DFS
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #find p or q or None
        if root in (None, p, q): return root
        
        left = self.lowestCommonAncestor( root.left, p, q) 
        right = self.lowestCommonAncestor(root.right, p, q)
        
        #found one of p, q in left, and another in right
        if left and right:
            return root
        #otherwise, it must be the one that is NOT NONE.
        else:
            return left or right
            
