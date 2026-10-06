# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:


        #Brute Force: Har node se deepest leaf tak baar-baar depth calculate karo → O(n²) Time, O(h) Space.
        #Best Approach: DFS recursion se 1 + max(left_depth, right_depth) calculate karo → O(n) Time, O(h) Space.

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)