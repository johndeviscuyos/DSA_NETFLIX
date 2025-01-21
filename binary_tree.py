class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.positions = {}  # Store x-positions for each node

    def insert_at_node(self, parent_value, new_value, direction):
        if self.size >= 15:
            return False, "Tree is at maximum capacity (15 nodes)"

        if self.root is None:
            self.root = Node(new_value)
            self.positions[new_value] = {'x': 0, 'level': 0}  # Root at center (x=0)
            self.size += 1
            return True, "Root node created"

        # Find the parent node
        parent = self._find_node(self.root, parent_value)
        if parent is None:
            return False, f"Parent node with value {parent_value} not found"

        # Check if new value is same as parent value
        if parent_value == new_value:
            return False, f"Child node cannot have the same value as its parent ({new_value})"

        # Get parent's position
        parent_pos = self.positions[parent_value]
        parent_x = parent_pos['x']
        parent_level = parent_pos['level']

        # Calculate new node position
        offset = 2 ** (3 - parent_level) / 2  # Adjust spacing based on level
        if direction == "left":
            if parent.left is not None:
                return False, f"Left child of {parent_value} already exists"
            parent.left = Node(new_value)
            self.positions[new_value] = {
                'x': parent_x - offset,
                'level': parent_level + 1
            }
            self.size += 1
            return True, f"Added {new_value} to the left of {parent_value}"
        elif direction == "right":
            if parent.right is not None:
                return False, f"Right child of {parent_value} already exists"
            parent.right = Node(new_value)
            self.positions[new_value] = {
                'x': parent_x + offset,
                'level': parent_level + 1
            }
            self.size += 1
            return True, f"Added {new_value} to the right of {parent_value}"

        return False, "Invalid direction specified"

    def _find_node(self, node, value):
        if node is None or node.value == value:
            return node

        left_result = self._find_node(node.left, value)
        if left_result:
            return left_result

        return self._find_node(node.right, value)

    def get_tree_data(self):
        """Convert the tree into a format suitable for visualization"""
        if not self.root:
            return []

        result = []
        queue = [(self.root, None)]  # (node, parent_value)

        while queue:
            node, parent = queue.pop(0)
            pos = self.positions[node.value]

            result.append({
                'value': node.value,
                'level': pos['level'],
                'x': pos['x'],
                'parent': parent
            })

            if node.left:
                queue.append((node.left, node.value))
            if node.right:
                queue.append((node.right, node.value))

        return result