from flask import Flask, render_template, request, jsonify
from linklist import Linklist
from conversion import infix_to_postfix
from queue_util import Queue
from binary_tree import BinaryTree
from graph import create_train_graph, find_shortest_path
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from quick import quick_sort
from merge import merge_sort

app = Flask(__name__)

# Instantiate the linked list
linked_list = Linklist()
cart = Queue()
G = create_train_graph()

# Categorize stations by train line
stations = {
    'MRT': ['North Avenue', 'Quezon Avenue', 'GMA Kamuning', 'Araneta Center-Cubao', 'Santolan-Annapolis', 'Ortigas',
            'Shaw Boulevard', 'Boni', 'Guadalupe', 'Buendia', 'Ayala', 'Magallanes', 'Taft Avenue'],
    'LRT1': ['Roosevelt', 'Balintawak', 'Monumento', '5th Avenue', 'R. Papa', 'Abad Santos', 'Blumentritt', 'Tayuman',
             'Bambang', 'Doroteo Jose', 'Carriedo', 'Central Terminal', 'UN Avenue', 'Pedro Gil', 'Quirino',
             'Vito Cruz', 'Gil Puyat', 'Libertad', 'EDSA', 'Baclaran','Redemptorist','MIA', 'Asiaworld','Ninoy Aquino', 'Dr.Santos','Las Piñas', 'Zapote','Niog'],
    'LRT2': ['Recto', 'Legarda', 'Pureza', 'V. Mapa', 'J. Ruiz', 'Gilmore', 'Betty Go-Belmonte', 'Anonas', 'Katipunan',
             'Santolan']
}

binary_tree = BinaryTree()

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
@app.route("/cuyos")
def cuyos():
    return render_template("cuyos.html")

@app.route("/ronda")
def ronda():
    return render_template("ronda.html")

@app.route("/uy")
def uy():
    return render_template("uy.html")

@app.route("/varron")
def varron():
    return render_template("varron.html")

@app.route("/mangulabnan")
def mangulabnan():
    return render_template("mangulabnan.html")

@app.route("/diong")
def diong():
    return render_template("diong.html")
@app.route("/garcia")
def garcia():
    return render_template("garcia.html")
@app.route('/linklist', methods=["GET", "POST"])  # Combined route for stack operations
def linklist():
    stack_contents = ""
    message = ""  # Add a separate message variable

    if request.method == "POST":
        # Perform linked list-related operations
        if "push" in request.form:
            data = request.form["data"]
            linked_list.push(data)
        elif "pop" in request.form:
            popped_item = linked_list.pop()
            message = f"Popped: {popped_item}" if popped_item else "The list is empty, nothing to pop."
        elif "peek" in request.form:
            if linked_list.is_empty():
                message = "List is empty - nothing to peek at"
            else:
                top_item = linked_list.peek()
                message = f"Peeked at first item: {top_item}"
        elif "remove_beginning" in request.form:
            removed_item = linked_list.remove_beginning()
            message = f"Removed from the beginning: {removed_item}" if removed_item else "No data to remove."
        elif "remove_at_end" in request.form:
            removed_item = linked_list.remove_at_end()
            message = f"Removed from the end: {removed_item}" if removed_item else "No data to remove."
        elif "remove_at" in request.form:
            data = request.form["data"]
            removed_item = linked_list.remove_at(data)
            message = f"Removed item: {removed_item}" if removed_item else f"Item {data} not found."


    # Format linked list contents for display
    if not linked_list.is_empty():
        stack_items = []
        current_node = linked_list.top
        while current_node:
            stack_items.append(current_node.data)
            current_node = current_node.next
        stack_contents = " -> ".join(stack_items)
    else:
        stack_contents = "The list is empty."

    return render_template('linklist.html', stack_contents=stack_contents, message=message)  # Add message to template

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
def binary():
    global binary_tree
    message = ""
    success = True

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create_root":
            try:
                new_value = int(request.form.get("new_value"))
                success, message = binary_tree.insert_at_node(None, new_value, None)
            except ValueError:
                success = False
                message = "Please enter a valid number"

        elif action == "insert":
            try:
                parent_value = int(request.form.get("parent_value"))
                new_value = int(request.form.get("new_value"))
                direction = request.form.get("direction")
                success, message = binary_tree.insert_at_node(parent_value, new_value, direction)
            except ValueError:
                success = False
                message = "Please enter valid numbers"

    # Get tree data for visualization
    tree_data = binary_tree.get_tree_data()

    return render_template(
        "binary_tree.html",
        tree=binary_tree,
        tree_data=tree_data,
        message=message,
        success=success
    )
@app.route("/stations")
def stations():
    return render_template("stations.html", stations=stations)


@app.route("/find_path", methods=["POST"])
def find_path():
    origin = request.form.get("origin")
    destination = request.form.get("destination")

    if origin and destination:
        path, distance = find_shortest_path(G, origin, destination)
        if path:
            return render_template("stations.html", stations=stations, path=path, distance=distance, origin=origin,
                                   destination=destination)
        else:
            error = "No path found between the selected stations."
            return render_template("stations.html", stations=stations, error=error)

    error = "Please select both origin and destination stations."
    return render_template("stations.html", stations=stations, error=error)

@app.route("/sorting", methods=["GET", "POST"])
def sorting():
    if request.method == "POST":
        array_str = request.form.get("array")
        algo = request.form.get("algo")
        try:
            arr = [int(x) for x in array_str.split(",")]
        except ValueError:
            return "Invalid input array", 400

        if algo == "bubble":
            sorting_steps = bubble_sort(arr.copy())
        elif algo == "selection":
            sorting_steps = selection_sort(arr.copy())
        elif algo == "insertion":
            sorting_steps = insertion_sort(arr.copy())
        elif algo == "merge":
            sorting_steps = list(merge_sort(arr.copy()))
        elif algo == "quick":
            sorting_steps = quick_sort(arr.copy())
        else:
            return "Invalid sorting algorithm", 400

        return jsonify(list(sorting_steps))
    return render_template("sorting.html")

if __name__ == "__main__":
    app.run(debug=True)
