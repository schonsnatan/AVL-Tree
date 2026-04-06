from models.node import TreeNode

class TreeBalancer:     

    def get_node_height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return node.height

    def get_balance(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            return self.get_node_height(node.left) - self.get_node_height(node.right)
    
    def handle_balance(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        
        node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))
        node.balance_factor = self.get_balance(node)

        # Rotacao Simples a Direita
        if node.balance_factor > 1 and self.get_balance(node.left) >= 0:
            print("Rotacao Simples a Direita (LL)")
            print("No desbalanceado]:", node.key)
            return self.right_rotate(node)
        
        # Rotacao Simples a Esquerda
        elif node.balance_factor < -1 and self.get_balance(node.right) <= 0:
            print("Rotacao Simples a Esquerda (RR)")
            print("No desbalanceado:", node.key)
            return self.left_rotate(node)
        
        # Rotacao Dupla a Direita
        elif node.balance_factor > 1 and self.get_balance(node.left) < 0:
            print("Rotacao Dupla a Direita (LR)")
            print("No desbalanceado:", node.key)
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Rotacao Dupla a Esquerda
        elif node.balance_factor < - 1 and self.get_balance(node.right) > 0:
            print("Rotacao Dupla a Esquerda (RL)")
            print("No desbalanceado:", node.key)
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
    
    def right_rotate(self, node: TreeNode):
        fe = node.left
        fe_r = fe.right
        fe.right = node
        node.left = fe_r
        node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))
        fe.height = 1 + max(self.get_node_height(fe.left), self.get_node_height(fe.right))
        return fe

    def left_rotate(self, node: TreeNode):
        fd = node.right
        fd_e = fd.left
        fd.left = node
        node.right = fd_e
        node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))
        fd.height = 1 + max(self.get_node_height(fd.left), self.get_node_height(fd.right))
        return fd