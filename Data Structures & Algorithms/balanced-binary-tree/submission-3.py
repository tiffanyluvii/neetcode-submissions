# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        leftValue = self.isBalancedAux(root.left)
        rightValue = self.isBalancedAux(root.right)

        maxValue = max(leftValue, rightValue)
        minValue = min(leftValue, rightValue)

        print(maxValue)
        print(minValue)

        print(maxValue - minValue)
        if (maxValue - minValue > 1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)



    def isBalancedAux(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.isBalancedAux(root.left),          self.isBalancedAux(root.right))

        
        