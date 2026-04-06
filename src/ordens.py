from models.avl_tree import TreeNode

class PosOrdem():

    def post_order(self, node: TreeNode) -> None:
        
        if node is None:
            return
        
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.key, end=", ")

class PreOrdem():

    def pre_ordem(self, node: TreeNode) -> None:
        if node is None:
            return
        
        print(node.key, end=", ")
        self.pre_ordem(node.left)
        self.pre_ordem(node.right)

class InOrden():

    def in_orden(self, node: TreeNode) -> None:
        if node is None:
            return
        
        self.in_orden(node.left)
        print(node.key, end=", ")
        self.in_orden(node.right)