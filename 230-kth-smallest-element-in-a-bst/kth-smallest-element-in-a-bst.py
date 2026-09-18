# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, result):
        if root is None:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        result = []

        self.inorder(root, result)
        return result[k-1]