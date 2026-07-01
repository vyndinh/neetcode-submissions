# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cnt):
            if not node:
                return 0
            left_depth = dfs(node.left, cnt+1)
            right_depth = dfs(node.right, cnt+1)
            
            return 1 + max(left_depth, right_depth)

        return dfs(root, 0)