class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lm=-float("inf"), rm=float("inf")):
            if not node:
                return True
            if lm < node.val < rm:
                return helper(node.left, lm, min(rm, node.val)) and helper(node.right, max(lm,node.val), rm)
            else:
                return False
        return helper(root)