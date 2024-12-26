

def print_fancy_tree(root, level=0, space="    "):
    """
    Print the binary tree in a fancy format.

    Args:
        root (Node): The root of the tree.
        level (int): The current level in the tree.
        space (str): The spacing for indentation.

    Returns:
        str: A string representation of the tree.
    """
    if root is None:
        return ""
    result = ""
    # Print right child first (reverse in-order)
    if root.right:
        result += print_fancy_tree(root.right, level + 1, space)
    # Add current node
    result += space * level + str(root.value) + "\n"
    # Print left child
    if root.left:
        result += print_fancy_tree(root.left, level + 1, space)
    return result
