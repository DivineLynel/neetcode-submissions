# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(current_node):
            if not current_node:
                return 0

            lef_height = dfs(current_node.left)
            right_height = dfs(current_node.right)

            self.res = max(self.res, lef_height + right_height)

            return max(lef_height, right_height) + 1

        dfs(root)

        return self.res