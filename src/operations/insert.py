from models.node import TreeNode
from operations.balancer import TreeBalancer

class TreeInserter:

    def __init__(self):
        self.balancer = TreeBalancer()

    def insert_recursively(self, node: TreeNode, value: int) -> TreeNode:
        if node == None:
            return TreeNode(value)

        if value < node.key:
            node.left = self.insert_recursively(node.left, value)
        elif value > node.key:
            node.right = self.insert_recursively(node.right, value)

        node = self.balancer.handle_balance(node)
        return node