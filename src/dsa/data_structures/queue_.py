class Queue():
    '''
    Self-defined queue class to support appending to tail in O(1) time and 
    popping from head in O(1) time. Queue structure is modeled after a linked 
    list with prev and next pointers
    '''
    class QueueNode():
        def __init__(self, val, prev=None, next=None) -> None:
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, *vals) -> None:
        '''Add each val to end of queue in order it appears in iterable'''
        for val in vals:
            if self.head is None:
                self.head = self.tail = self.QueueNode(val)
                self.size = 1

            else:
                node = self.QueueNode(val, self.tail)
                self.tail.next = node
                self.tail = node
                self.size += 1

    def dequeue(self) -> int:
        '''Pop item from front of queue'''
        assert self.size > 0, 'Cannot pop from empty queue'
            
        if self.head is self.tail:
            value = self.head.val
            self.head = self.tail = None
            self.size = 0
            return value

        value = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return value

    def get_elems(self) -> list:
        '''Return a list representing elements in queue from head to tail'''
        elems = []
        curr = self.head
        while curr != None:
            elems.append(curr.val)
            curr = curr.next
        return elems

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return self.size > 0

    def __iter__(self):
        curr = self.head
        while curr != None:
            yield curr.val
            curr = curr.next

    def __repr__(self) -> str:
        return ' '.join([f'{elem} ->' for elem in self] + ['None'])