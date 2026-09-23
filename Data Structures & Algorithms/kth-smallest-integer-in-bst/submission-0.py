# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []


        def kthSmallestAux (node: Optional[TreeNode]):
            if not node:
                return

            kthSmallestAux(node.left)
            l.append(node.val)
            kthSmallestAux(node.right)

        kthSmallestAux(root)
        return l[k-1]