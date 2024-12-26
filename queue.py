class Node:
    """Node class to represent an element in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Queue implementation using a linked list."""

    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None  # Points to the rear of the queue

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front is None

    def enqueue(self, data):
        """Adds an element to the rear of the queue."""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty, update rear
            self.rear = None
        return data

    def peek(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data


class Deque(Queue):
    """Deque implementation extending the Queue."""

    def add_front(self, data):
        """Adds an element to the front of the deque."""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def remove_rear(self):
        """Removes and returns the rear element of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")

        # If there is only one element
        if self.front == self.rear:
            data = self.rear.data
            self.front = self.rear = None
            return data

        # Traverse to find the second last node
        current = self.front
        while current.next != self.rear:
            current = current.next

        data = self.rear.data
        self.rear = current
        self.rear.next = None
        return data