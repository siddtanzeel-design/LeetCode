# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(TreeNode):
            if TreeNode is None:
                return

            result.append(TreeNode.val)
            preorder(TreeNode.left)
            preorder(TreeNode.right)

        preorder(root)
        return result