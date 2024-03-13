# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        q = []
        q.append(cloned)
        while q:
            n = q.pop(0)
            if n.val == target.val:
                return n
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return None
