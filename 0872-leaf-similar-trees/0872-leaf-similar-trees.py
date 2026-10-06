# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:


        #Brute Force: Dono trees ke leaves ko baar-baar traverse karke compare karo → O(n²) Time, O(h) Space.
        #Best Approach: DFS se dono trees ke leaf values ka sequence nikalo aur compare karo → O(n + m) Time, O(n + m) Space.

        def get_leaves(root):
            leaves = []

            def dfs(node):
                if node is None:
                    return

                if node.left is None and node.right is None:
                    leaves.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        return get_leaves(root1) == get_leaves(root2)
        