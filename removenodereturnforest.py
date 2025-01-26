from collections import deque
from types import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        if not root:
            return []
        forest=[]
        nodes_queue = deque([root])
        while nodes_queue:
            current_node=nodes_queue.popleft()
            if current_node.left:
                nodes_queue.append(current_node.left)
                if current_node.left.val in to_delete_set:
                    current_node.left.val=None
            if current_node.right:
                nodes_queue.append(current_node.right)
                if current_node.right.val in to_delete_set:
                    current_node.right.val=None
            if current_node.val in to_delete_set:
                if current_node.left:
                    forest.append(current_node.left)
                if current_node.right:
                    forest.append(current_node.right)
        if root not in to_delete_set:
            forest.append(root)
        return forest