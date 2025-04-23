"""Exists function checking if a value is in A BST"""


def exists(self, val):
    """Based off boot.dev so will only work with those classes
    returns: True or False, yes it exists"""

    if val == self.val:
        return True

    # We first check the root of the tree
    # If the val we're searching for is less than root, go left else go right

    if val < self.val:
        if self.left is not None:
            return self.left.exists(val)
        else:
            return False
    else:
        if self.right is not None:
            return self.right.exists(val)
        else:
            return False


