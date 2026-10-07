# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:


        #Brute Force: Har node ko starting point maan kar DFS karo → O(n²) Time, O(h) Space
        #Best Approach: Prefix Sum + HashMap use karke required previous sum check karo → O(n) Time, O(h) Space



        prefix = {0: 1}

        def dfs(node, curr_sum):
            if node is None:
                return 0

            curr_sum += node.val

            count = prefix.get(curr_sum - targetSum, 0)

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix[curr_sum] -= 1

            return count

        return dfs(root, 0)
        