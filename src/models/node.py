class TreeNode:

    def __init__ (self, key: int):
        self.key = key
        self.right = None
        self.left = None
        self.height = 1
        self.balance_factor = 0