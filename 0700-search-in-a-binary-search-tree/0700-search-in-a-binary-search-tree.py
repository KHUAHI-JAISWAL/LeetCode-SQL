# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        #Brute Force: DFS/BFS se poore tree mein target search karo — Time: O(N), Space: O(N) worst case.
        #Best Approach: BST property use karke target chhota ho to left aur bada ho to right jao — Time: O(H), Space: O(1) iterative approach, where H is tree height.


        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None

        
