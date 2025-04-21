class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
                return self
        if self.val < val:
            if self.right:
                self.right = self.right.delete(val)
                return self
        if val == self.val:
            if not self.right:
                return self.left
            if not self.left:
                return self.right

            # two children exist,
            # find the smallest node in right subtree
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left

            self.val = min_larger_node.val

            self.right = self.right.delete(min_larger_node.val)

            return self

            # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
