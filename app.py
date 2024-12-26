from flask import Flask, render_template, request, jsonify
from linklist import Linklist
from conversion import infix_to_postfix
from queue import Queue
from binary_tree import BinaryTree, print_fancy_tree
app = Flask(__name__)

# Instantiate the linked list
linked_list = Linklist()
cart = Queue()


@app.route("/")
def index():
    return render_template("index.html")  # Profile selection page

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")  # Homepage

@app.route("/profile")
def profile():
    return render_template("profile.html")  # Profile page

@app.route("/works")
def works():
    return render_template("works.html")  # Works page

@app.route('/linklist', methods=["GET", "POST"])  # Combined route for stack operations
def linklist():
    stack_contents = ""

    if request.method == "POST":
        # Perform linked list-related operations
        if "push" in request.form:
            data = request.form["data"]
            linked_list.push(data)  # Use linked_list instead of stack
            stack_contents = f"{data}"
        elif "pop" in request.form:
            popped_item = linked_list.pop()
            stack_contents = f"Popped: {popped_item}" if popped_item else "The list is empty, nothing to pop."
        elif "peek" in request.form:
            if linked_list.is_empty():
                stack_contents = "The list is empty."
            else:
                top_item = linked_list.peek()
                stack_contents = f"Top item: {top_item}"
        elif "remove_beginning" in request.form:
            removed_item = linked_list.remove_beginning()
            stack_contents = f"Removed from the beginning: {removed_item}" if removed_item else "No data to remove."
        elif "remove_end" in request.form:
            removed_item = linked_list.remove_at_end()
            stack_contents = f"Removed from the end: {removed_item}" if removed_item else "No data to remove."
        elif "remove_at" in request.form:
            data = request.form["data"]
            removed_item = linked_list.remove_at(data)
            stack_contents = f"Removed item: {removed_item}" if removed_item else f"Item {data} not found."

    # Format linked list contents for display
    if not linked_list.is_empty():
        stack_items = []
        current_node = linked_list.top  # Use linked_list instead of stack
        while current_node:
            stack_items.append(current_node.data)
            current_node = current_node.next
        stack_contents = " -> ".join(stack_items)  # Reset stack_contents to avoid duplication
    else:
        stack_contents = "The list is empty."

    return render_template('linklist.html', stack_contents=stack_contents)  # Render template with contents

@app.route("/convert", methods=["GET", "POST"])
def convert():
    result = ""
    steps = []  # New variable to hold steps
    if request.method == "POST":
        expression = request.form.get("expression")  # Get input from form
        try:
            # Perform conversion and get steps
            result, steps = infix_to_postfix(expression)
        except Exception as e:
            result = f"Error: {str(e)}"

    # Return the result and steps to the template
    return render_template("convert.html", result=result, steps=steps)

@app.route('/queue', methods=['GET', 'POST'])
def queue():
    message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        item = request.form.get('item')

        try:
            if action == 'enqueue' and item:
                cart.enqueue(item)
            elif action == 'dequeue':
                cart.dequeue()
        except Exception as e:
            message = f"Error: {str(e)}"

    # Prepare the queue items for rendering
    items = []
    current = cart.front
    while current:
        items.append(current.data)
        current = current.next

    return render_template("queue.html", items=items, message=message)

@app.route("/binary", methods=["GET", "POST"])
def binary_tree():
    tree = BinaryTree(10)  # Initialize or load your tree
    if request.method == "POST":
        action = request.form.get("action")
        if action == "insert":
            value = int(request.form.get("value"))
            tree.insert(value)  # Implement an insert method in your BinaryTree class
        elif action == "delete":
            value = int(request.form.get("value"))
            tree.delete_node(tree.root, value)

    tree_display = print_fancy_tree(tree.root)
    return render_template("binary.html", tree_display=tree_display)

if __name__ == "__main__":
    app.run(debug=True)
