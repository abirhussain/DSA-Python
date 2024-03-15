# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = []
        queue.append(root)
        ans = 0
        while queue:
            ln = len(queue)
            ans += 1
            for _ in range(ln):
                node = queue.pop(0)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
        return ans
        