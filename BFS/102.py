# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        queue = []
        queue.append(root)
        while queue:
            len_q = len(queue)
            tmp = []
            for _ in range(len_q):
                node = queue.pop(0)
                if node != None:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(tmp):
                ans.append(tmp)
        return ans
        