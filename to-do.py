from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory storage for tasks
todo_list = []

# HTML template as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1 {
            color: #333;
        }
        .task {
            padding: 10px;
            border-bottom: 1px solid #ccc;
        }
        .completed {
            text-decoration: line-through;
            color: gray;
        }
        .actions {
            margin-left: 10px;
        }
    </style>
</head>
<body>

    <h1>To-Do List</h1>

    <!-- Task Input Form -->
    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="Enter a new task" required>
        <button type="submit">Add Task</button>
    </form>

    <!-- Task List -->
    <ul>
        {% for task in todo_list %}
        <li class="task {% if task.completed %}completed{% endif %}">
            {{ loop.index }}. {{ task.description }}
            <span class="actions">
                {% if not task.completed %}
                <a href="/complete/{{ loop.index0 }}">Mark as completed</a>
                {% endif %}
                <a href="/delete/{{ loop.index0 }}">Delete</a>
            </span>
        </li>
        {% else %}
        <p>No tasks yet. Add one above!</p>
        {% endfor %}
    </ul>

</body>
</html>
"""

# Route for the homepage
@app.route("/")
def index():
    return render_template_string(html_template, todo_list=todo_list)

# Route to add a task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        todo_list.append({"description": task, "completed": False})
    return redirect(url_for("index"))

# Route to mark a task as completed
@app.route("/complete/<int:task_index>")
def complete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
    return redirect(url_for("index"))

# Route to delete a task
@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list.pop(task_index)
    return redirect(url_for("index"))

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
