from fancy_tree_printer import print_fancy_tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        """
        Inserts a value into the binary tree while maintaining BST properties.
        """

        def _insert_recursive(current_node, value):
            if current_node is None:
                return Node(value)
            if value < current_node.value:
                current_node.left = _insert_recursive(current_node.left, value)
            elif value > current_node.value:
                current_node.right = _insert_recursive(current_node.right, value)
            return current_node

        self.root = _insert_recursive(self.root, value)

    def delete_node(self, root, key):
        """
        Deletes a node with the specified key from the binary tree.
        """
        if root is None:
            return root

        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            min_larger_node = self._find_min(root.right)
            root.value = min_larger_node.value
            root.right = self.delete_node(root.right, min_larger_node.value)

        return root

    def _find_min(self, node):
        """
        Finds the node with the minimum value in the given subtree.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, root, key):
        """
        Searches for a node with the specified key in the binary tree.
        """
        if root is None or root.value == key:
            return root

        if key < root.value:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def display(self):
        """
        Displays the binary tree visually (optional utility function).
        """
        return print_fancy_tree(self.root)

