# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = []
        queue.append(root)
        ans = None
        while queue:
            ln = len(queue)
            node = queue.pop(0)
            ans = node.val
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
            for _ in range(ln-1):
                n = queue.pop(0)
                if n and n.left:
                    queue.append(n.left)
                if n and n.right:
                    queue.append(n.right)
        return ans