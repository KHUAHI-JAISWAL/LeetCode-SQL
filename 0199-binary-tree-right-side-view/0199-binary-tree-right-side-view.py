# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        #Brute Force Approach: BFS — har level ka last node store karna; TC: O(N), SC: O(N).
        #Best Approach: DFS (Right → Left) — har level ka pehla node store karna; TC: O(N), SC: O(H)

        ans = []

        def dfs(node, level):
            if not node:
                return

            if level == len(ans):
                ans.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return ans
        