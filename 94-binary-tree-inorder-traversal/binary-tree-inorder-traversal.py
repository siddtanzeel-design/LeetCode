# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(TreeNode):
            if TreeNode is None:
                return

            inorder(TreeNode.left)
            result.append(TreeNode.val)
            inorder(TreeNode.right)

        inorder(root)
        return result