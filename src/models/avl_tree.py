from models.node import TreeNode
from operations.insert import TreeInserter
from operations.delete import TreeDeleter
from operations.balancer import TreeBalancer
from operations.search import TreeSearcher

class AVLTree:
    def __init__(self):
        self.inserter = TreeInserter()
        self.deleter = TreeDeleter()
        self.balancer = TreeBalancer()
        self.searcher = TreeSearcher()
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, value: int) -> TreeNode:
        self.root = self.inserter.insert_recursively(self.root, value)
    
    def search(self, value: int) -> TreeNode:
        return self.searcher.search(self.root, value)

    def delete(self, value: int) -> TreeNode:
        self.root = self.deleter.delete(self.root, value)
            
    def print_tree(self, node=None, level=0, prefix="Root: ") -> None:
        if node is None:
            node = self.root
        if node is not None:
            bf = self.balancer.get_balance(node)
            print("    " * level + prefix + f"{node.key} (BF: {bf})")
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print("    " * (level + 1) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print("    " * (level + 1) + "R--- None")