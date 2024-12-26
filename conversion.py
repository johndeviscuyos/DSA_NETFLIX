class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):  # Add a new node to the top of the stack
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):  # Remove the node at the top of the stack
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):  # Return the data at the top of the stack
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):  # Determine if the stack has elements
        return self.top is None


def precedence(operator):  # Set precedence of the operators
    if operator in "+-":
        return 1
    elif operator in "*/":
        return 2
    elif operator == "^":
        return 3
    else:
        return 0


def left_associative(operator):  # Determine if operator is left-associative
    return operator in "+-*/"


def infix_to_postfix(expression):  # Convert infix expression to postfix
    stack = Stack()
    output = []
    steps = []  # Track each step of the conversion process

    for term in expression:
        if term.isalnum():  # Operand
            output.append(term)
            steps.append(f"Added operand {term} to output: {' '.join(output)}")
        elif term == '(':
            stack.push(term)
            steps.append(f"Pushed '(' onto stack")
        elif term == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
                steps.append(f"Popped operator from stack to output: {' '.join(output)}")
            stack.pop()  # Remove '(' from the stack
            steps.append("Popped '(' from stack")
        elif term in "+-*/^":  # Operator
            while (not stack.is_empty() and
                   (precedence(stack.peek()) > precedence(term) or
                    (precedence(stack.peek()) == precedence(term) and left_associative(term)))):
                output.append(stack.pop())
                steps.append(f"Popped operator from stack to output: {' '.join(output)}")
            stack.push(term)
            steps.append(f"Pushed operator {term} onto stack")
        else:
            raise ValueError("Invalid character in expression")

    # Pop remaining operators
    while not stack.is_empty():
        output.append(stack.pop())
        steps.append(f"Popped remaining operator to output: {' '.join(output)}")

    return " ".join(output), steps
