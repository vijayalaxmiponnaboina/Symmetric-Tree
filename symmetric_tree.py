# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(left,right):

            # both are empty
            if left is None and right is None:
                return True

            # If one is empty
            if left is None or right is None:
                return False

            # check value
            return (
                left.val==right.val
                and isMirror(left.left,right.right)
                and isMirror(left.right,right.left)
            )
            
        # base case
        if root is None:
            return True
        return isMirror(root.left,root.right)