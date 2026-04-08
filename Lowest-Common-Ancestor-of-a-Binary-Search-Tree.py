1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        current = root
11        if not root:
12            return False
13        while current:
14            if p.val < current.val and q.val < current.val:
15                current = current.left
16            elif p.val > current.val and q.val > current.val:
17                current = current.right
18            else:
19                return current
20        