# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        q = []
        q.append(root)
        while q:
            ans = 0
            length_q = len(q)
            for _ in range(length_q):
                node = q.pop(0)
                ans += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return ans
        