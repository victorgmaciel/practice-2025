"""
Queue stores ordered items but its design is more restrictive.
It allows items to be added to the tail of queue and remove from head of queue
FIFO, first person to get in "line" is also the first person to be served
"""

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) >= 0:
            self.items.insert(0, item)
    def pop(self):
        if len(self.items) > 0:
            deleted_item = self.items[-1]
            del self.items[-1]
            return deleted_item
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)



