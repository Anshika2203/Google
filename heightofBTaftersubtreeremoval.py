from collections import deque, defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n+q) double traversal
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        maxHeightAfterRemoval=[0]*100001
        self.currentMaxHeight=0
        def TraverseLeftToRight(node, currentHeight):
            if not node:
                return
            maxHeightAfterRemoval[node.val]=self.currentMaxHeight
            self.currentMaxHeight=max(self.currentMaxHeight, currentHeight)
            TraverseLeftToRight(node.left, currentHeight+1)
            TraverseLeftToRight(node.right, currentHeight+1)
        def TraverseRightToLeft(node, currentHeight):
            if not node:
                return
            maxHeightAfterRemoval[node.val]=max(maxHeightAfterRemoval[node.val], self.currentMaxHeight)
            self.currentMaxHeight=max(self.currentMaxHeight, currentHeight)
            TraverseRightToLeft(node.right, currentHeight+1)
            TraverseRightToLeft(node.left, currentHeight+1)
        TraverseLeftToRight(root, 0)
        self.currentMaxHeight=0
        TraverseRightToLeft(root, 0)

        return [maxHeightAfterRemoval[q] for q in queries]



