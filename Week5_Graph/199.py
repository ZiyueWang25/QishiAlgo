# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        l = deque([root])
        while l:
            res.append(l[-1].val)
            l2 = deque([])
            while l:
                node = l.popleft()
                l2.append(node.left) if node.left else None
                l2.append(node.right) if node.right else None
            l = l2
        return res

    # DFS
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside