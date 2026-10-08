# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:

        #Brute Force: Har node se ZigZag path separately calculate karo → O(n²) Time, O(h) Space

        #Best Approach: DFS mein left/right direction aur current ZigZag length maintain karo → O(n) Time, O(h) Space


        ans = 0

        def dfs(node, left, right):
            nonlocal ans

            if node is None:
                return

            ans = max(ans, left, right)

            dfs(node.left, right + 1, 0)
            dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return ans
        