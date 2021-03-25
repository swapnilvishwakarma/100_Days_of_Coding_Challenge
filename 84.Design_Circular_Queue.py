# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implementation the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None]*k
        self.k = k
        self.front = self.rear = -1
        self.cur_size = 0
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            print(False)
            return False
        self.front = (self.front + 1) % self.k
        self.q[self.front] = value
        self.cur_size += 1
        print(True)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            print(False)
            return False
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = None
        self.cur_size -= 1
        print(True)
        return True
        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            print(-1)
            return -1
        idx = (self.rear + 1) % self.k
        print(self.q[idx])
        return self.q[idx]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            print(-1)
            return -1
        print(self.q[self.front])
        return self.q[self.front]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        print(self.cur_size == 0)
        return self.cur_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        print(self.cur_size == self.k)
        return self.cur_size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(4)
param_1 = obj.enQueue(3)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()