# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            length = len(queue)
            levelArr = []
            for _ in range(length):
                curr = queue.popleft()
                if (curr):
                    queue.append(curr.left)
                    queue.append(curr.right)
                    levelArr.append(curr.val)
            if (levelArr != []):
                res.append(levelArr)
        return res
        

        



        