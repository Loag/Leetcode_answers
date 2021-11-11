# 1214

from types import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:        
        # traverse root 2 and gat all of its values.
        def rec2(node, s):
            if node:
                s.add(node.val)
                rec2(node.left, s)
                rec2(node.right, s)
            return s
        
        t2 = rec2(root2, set())
        
        # traverse root1
        def rec1(node):
            if node:

                # get val from left tree
                t = rec1(node.left)

                # if target minus the value is in the second tree, then it is true
                if target - node.val in t2:
                    return True

                # if its not in the left tree, try the right
                if not t:
                    t = rec1(node.right)
                return t
        
        return(rec1(root1))