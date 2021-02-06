# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, MIN, MAX):
            if node is None:
                return True
            if MIN < node.val < MAX:
                return valid(node.left,MIN,min(MAX,node.val)) & valid(node.right,max(MIN,node.val),MAX)
            else:
                return False
        return valid(root,float("-inf"),float("inf"))