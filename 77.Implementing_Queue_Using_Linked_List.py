# Node for a singly linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# A Linked List class with single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the tail of the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # Remove an element from the head of linked list
    def remove(self):
        temp = self.head
        if (temp is not None):
            element = temp.data
            self.head = temp.next
            temp = None
            return element

    # Display an element from the tail of the linked list
    def peek(self):
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            return current.data

    # Print method for linked list
    def printLL(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
    
    
# Queue implememted using a linked list
Queue = LinkedList()
# Enqueue 3
Queue.insert(3)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 4
Queue.insert(4)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 5
Queue.insert(5)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Dequeue elements
print("Element dequeued:", Queue.remove())
print("Element dequeued:", Queue.remove())
print("Element dequeued:", Queue.remove())