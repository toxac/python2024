class Queue:
    """implementation of queue data structure using python list"""
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def enqueue(self, item) -> None:
        """This operation inserts an element t the end of the queue. 
        Given its straightforward nature, without any need for iterating or traversing, 
        the enqueue operation bears a time complexity of O(1), a constant time.
        """
        self.items.insert(0, item)
    
    def dequeue(self):
        """Dequeueing means removing the front element from the queue. 
        As the operation only involves the first element without any checks or iterations through the queue, 
        its time complexity remains constant at O(1
        """
        return self.items.pop()
    
    def size(self) -> int:
        return len(self.items)
