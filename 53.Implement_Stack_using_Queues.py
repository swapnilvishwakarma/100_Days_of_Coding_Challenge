# Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.


class Queue(object):
    def __init__(self):
        self.elements = []
        self.size = 0

    def add(self, x: int) -> None:
        """
        Add element x into queue.
        """
        self.elements.append(x)
        self.size += 1

    def remove(self) -> int:
        """
        Removes the element from the beginning of queue and returns that element.
        """
        if not self.empty():
            top = self.elements[0]
            self.elements.remove(top)
            self.size -= 1
            return top

    def peek(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.elements[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0

    def __str__(self):
        return self.elements.__str__()

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Queue()
        self.buffer = Queue()
        self.tops = {}

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.add(x)
        self.tops[self.stack.size] = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(self.stack.size - 1):
            self.buffer.add(self.stack.remove())
        top = self.stack.remove()

        while not self.buffer.empty():
            self.stack.add(self.buffer.remove())

        return top

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.tops[self.stack.size]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()

    def __str__(self):
        return self.stack.__str__()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()