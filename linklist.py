

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def remove_beginning(self):
        return self.pop()

    def remove_at_end(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            removed_data = self.top.data
            self.top = None
            return removed_data
        else:
            current_node = self.top
            while current_node.next.next is not None:
                current_node = current_node.next
            removed_data = current_node.next.data
            current_node.next = None
            return removed_data

    def remove_at(self, data):
        if self.top is None:
            return None

        if self.top.data == data:
            return self.pop()

        current_node = self.top
        while current_node.next is not None:
            if current_node.next.data == data:
                removed_data = current_node.next.data
                current_node.next = current_node.next.next
                return removed_data
            current_node = current_node.next

        return None