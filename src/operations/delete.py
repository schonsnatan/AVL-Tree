from models.node import TreeNode
from operations.balancer import TreeBalancer

class TreeDeleter:

    def __init__(self):
        self.balancer = TreeBalancer()

    def delete(self, node: TreeNode, value: int) -> TreeNode:
        if node is None:
            return node

        if value < node.key:
            node.left = self.delete(node.left, value)
        elif value > node.key:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        if node is None:
            return node

        node = self.balancer.handle_balance(node)
        return node

    # search for min value node in right subtree
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
