1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        if not root:
10            return False
11        def isSameTree(Raiz1,Raiz2):
12            if not Raiz1 and not Raiz2:
13                return True
14            if not Raiz1 or not Raiz2:
15                return False
16            if Raiz1.val != Raiz2.val:
17                return False
18            return isSameTree(Raiz1.left,Raiz2.left) and isSameTree(Raiz1.right, Raiz2.right)
19            
20
21        if isSameTree(root,subRoot):
22            return True
23        else:
24            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
25