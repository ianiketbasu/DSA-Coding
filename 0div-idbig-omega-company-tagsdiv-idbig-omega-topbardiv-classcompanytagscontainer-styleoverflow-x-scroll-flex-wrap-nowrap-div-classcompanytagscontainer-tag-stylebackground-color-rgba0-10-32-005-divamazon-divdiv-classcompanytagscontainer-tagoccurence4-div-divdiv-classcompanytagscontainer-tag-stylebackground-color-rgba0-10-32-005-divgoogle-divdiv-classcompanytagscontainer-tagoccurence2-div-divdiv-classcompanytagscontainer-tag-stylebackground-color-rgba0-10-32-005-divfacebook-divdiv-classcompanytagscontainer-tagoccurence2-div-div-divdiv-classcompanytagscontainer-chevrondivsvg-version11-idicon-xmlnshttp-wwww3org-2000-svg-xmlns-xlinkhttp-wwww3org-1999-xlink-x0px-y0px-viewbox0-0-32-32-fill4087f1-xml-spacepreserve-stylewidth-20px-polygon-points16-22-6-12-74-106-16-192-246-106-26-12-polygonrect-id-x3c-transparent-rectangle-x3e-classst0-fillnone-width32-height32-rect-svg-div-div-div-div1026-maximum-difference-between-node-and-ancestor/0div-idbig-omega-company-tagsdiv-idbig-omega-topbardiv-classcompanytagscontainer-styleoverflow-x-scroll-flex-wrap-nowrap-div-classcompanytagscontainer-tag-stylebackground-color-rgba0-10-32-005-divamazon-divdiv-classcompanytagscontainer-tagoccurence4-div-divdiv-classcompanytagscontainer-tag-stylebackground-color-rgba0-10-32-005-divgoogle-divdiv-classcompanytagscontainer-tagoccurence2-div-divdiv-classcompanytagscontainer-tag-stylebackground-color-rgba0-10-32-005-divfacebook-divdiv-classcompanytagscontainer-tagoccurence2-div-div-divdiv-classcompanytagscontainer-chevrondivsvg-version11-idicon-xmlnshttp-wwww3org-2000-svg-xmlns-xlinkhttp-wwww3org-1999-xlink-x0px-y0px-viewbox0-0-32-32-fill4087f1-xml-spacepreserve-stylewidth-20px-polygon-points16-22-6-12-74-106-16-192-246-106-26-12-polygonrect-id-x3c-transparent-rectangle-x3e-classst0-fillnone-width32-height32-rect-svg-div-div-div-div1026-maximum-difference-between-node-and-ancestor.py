# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mx = 0
        stack = [[root,root.val,root.val]]
        while len(stack) > 0:
            tmp, cur_mx, cur_mn = stack.pop()
            if tmp.val > cur_mx:
                cur_mx = tmp.val
            if tmp.val < cur_mn:
                cur_mn = tmp.val
            if cur_mx - cur_mn > mx:
                mx = cur_mx - cur_mn
                
            if tmp.left:
                stack.append([tmp.left, cur_mx, cur_mn])
            if tmp.right:
                stack.append([tmp.right, cur_mx, cur_mn])

        return mx