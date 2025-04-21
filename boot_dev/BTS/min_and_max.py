"""traversing through nodes"""



def get_min(self):
    if self.val is None:
        return
    current = self # get a temp variable going
    while self.left is not None:
        current = current.left
    return current.val

def get_max(self):
    if self.val is None:
        return
    current = self
    while self.right is not None:
        current = current.right
    return current.val

