# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #Brute Force: Har node ke root-to-node path ko check karke maximum value nikaalo → O(n²) Time, O(h) Space
        #Best Approach: DFS mein root se current node tak ka max_value maintain karo → O(n) Time, O(h) Space




        def dfs(node, max_val):
            if node is None:
                return 0

            count = 0

            if node.val >= max_val:
                count = 1
                max_val = node.val

            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        return dfs(root, root.val)