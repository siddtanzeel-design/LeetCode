# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def isBST(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (isBST(node.left, low, node.val) and isBST(node.right, node.val, high))

        return isBST(root, float('-inf'), float('inf'))