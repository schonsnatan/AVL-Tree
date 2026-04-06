from models.node import TreeNode

class TreeSearcher:
    def search(self, node: TreeNode, value: int) -> TreeNode:
        if node == None or node.key == value:
            return node

        if value < node.key:
            return self.search(node.left, value)
        
        return self.search(node.right, value)
