# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        #Brute Force: Har node se p aur q tak ka path find karke paths compare karo → O(n) Time, O(n) Space

        #Best Approach: DFS mein agar left aur right subtree se p aur q milte hain, current node LCA hai → O(n) Time, O(h) Space


        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right