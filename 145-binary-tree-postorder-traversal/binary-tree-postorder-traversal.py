# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(TreeNode):
            if TreeNode is None:
                return

            postorder(TreeNode.left)
            postorder(TreeNode.right)
            result.append(TreeNode.val)

        postorder(root)
        return result