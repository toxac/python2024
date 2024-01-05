class Stack:
    """ Stack implementation using list
    parameters:
    none
    
    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        """Check if stack is empty"""
        return self.items == []
    
    def push(self, item):
        """Push item to stack"""
        self.items.append(item)
    
    def pop(self):
        """Pop item from stack"""
        return self.items.pop()
    
    def peek(self):
        """Peek at top of stack"""
        return self.items[len(self.items)-1]
    
    def size(self):
        """Return size of stack"""
        return len(self.items)