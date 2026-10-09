# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:

        #Brute Force Approach: BFS — har level ke nodes ka sum calculate karna; TC: O(N), SC: O(N).
        #Best Approach: BFS — level-wise sum calculate karke minimum level with maximum sum return karna; TC: O(N), SC: O(N).


        q = deque([root])
        level = 1
        best_level = 1
        max_sum = float('-inf')

        while q:
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                best_level = level

            level += 1

        return best_level
        