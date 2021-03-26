# Design your implementation of the circular double-ended queue (deque).

# Your implementation should support following operations:

# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return -1.
# isEmpty(): Checks whether Deque is empty or not. 
# isFull(): Checks whether Deque is full or not.

class MyCircularDeque:

    def __init__(self, k: int):
        
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cq = []*k        
        self.size = 0
        self.max_len = k
    
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if(self.size == self.max_len):
            print(False)
            return False
        self.cq.insert(0, value)
        self.size+=1
        print(True)
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if(self.size == self.max_len):
            print(False)
            return False
        self.cq.append(value)
        self.size+=1
        print(True)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if(not self.size):
            print(False)
            return False
        self.cq.pop(0)
        self.size-=1
        print(True)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if(not self.size):
            print(False)
            return False
        self.cq.pop()
        self.size-=1
        print(True)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        print(-1 if not self.size else self.cq[0])
        return -1 if not self.size else self.cq[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        print(-1 if not self.size else self.cq[-1])
        return -1 if not self.size else self.cq[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        print(not self.size)
        return not self.size

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        print(self.size == self.max_len)
        return self.size == self.max_len


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(7)
param_1 = obj.insertFront(4)
param_2 = obj.insertLast(5)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()