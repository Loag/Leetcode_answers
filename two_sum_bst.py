# 1214

from types import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:        
        def rec2(node, s):
            if node:
                s.add(node.val)
                rec2(node.left, s)
                rec2(node.right, s)
            return s
        
        t2 = rec2(root2, set())
        
        def rec1(node):
            if node:
                t = rec1(node.left)
                if target - node.val in t2:
                    return True
                if not t:
                    t = rec1(node.right)
                return t
        
        return(rec1(root1))