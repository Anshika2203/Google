# Our team uses a large distributed binary tree for storing data. We have noticed a concerning pattern 
# in our binary tree where there can be multiple long "chains" of nodes, each link with only one child.

# Please return the count of chains of certain lengths.

# A chain is defined as a run of nodes each containing one child, where each such node is defined as a "chain link node". 
# A chain ends when it reaches either a "normal node" (containing two children) or a "leaf node" (containing zero children).

# Nodes are of the following type:

# class Node:
#   """Base Node class. Nodes are either local or remote"""

# class LocalNode(Node):
#   """Node stored locally."""
#   left: Node
#   right: Node

# class RemoteNode(Node):
#   """Node which exists on another server.

#   Explain what the methods of this class would do.
#   You do not need to implement them but you do need to use them.
#   """

# # Hint: it can be helpful to first implement the algorithm using LocalNode
# # only, then extend it.

# Example:

# Key:
# - n: "normal" node:       2 children
# - c: "chain link" node:   1 child
# - cN: chain link node that is also bottom of chain (N=chain count)
# - l: leaf node:           0 children
# - ^: lack of a node, i.e. a stub


#    Depth 1                  n
#                          /     \
#    Depth 2             c1       c
#                       /  ^     / ^
#    Depth 3          n         c
#                    / \       ^ \
#    Depth 4        c    c       c3
#                  / ^  / ^      / ^
#    Depth 5      c2   c2       n
#                / ^  ^ \      / \
#    Depth 6    l        n    l   n
#                       / \      / \
#    Depth 7           l   l    l   l


# # Result:
# chains:
#   length 1: 1
#   length 2: 2
#   length 3: 1
  
#   class LocalNode(Node):
#   """Node stored locally."""
#   left: LocalNode
#   right: LocalNode
  
  
#   class LocalNode(Node):
#     length=0
    
#     def get_child_node(self):
#       return(self.left is not None, self.right is not None)
 
#     def get_chain_length(self,node,length):
#       results={}
#     
#       current=self
      
#       left_exists, right_exists = self.get_child_node()
#       if not left_exists and not right_exists:
#         return length
#       if left_exists and right_exists:
#         get_chain_length(node.left, length)
#         get_chain_length(node.right, length)
#         return length
#       current=current.left if left_exists else current.right
#       length=get_chain_length(current, lengths)+1
        
     
#       if length>0:
#         results[length]=results.get(length, 0)+1
#       return length
    
#     get_chain_length(root, length)
#     return results
   
  
  
  
  