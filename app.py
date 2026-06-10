from flask import Flask, render_template, request, redirect, url_for, flash
import json
from pathlib import Path
from datetime import datetime


app = Flask(__name__)
app.secret_key = "dev-secret-key"

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


@app.route("/")
def index():
    tasks = load_tasks()
    status = request.args.get("status", "all")

    if status == "active":
        tasks = [task for task in tasks if not task["done"]]
    elif status == "done":
        tasks = [task for task in tasks if task["done"]]

    return render_template("index.html", tasks=tasks, status=status)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()

    if not title:
        flash("Task title cannot be empty.", "error")
        return redirect(url_for("index"))

    tasks = load_tasks()

    new_task = {
        "id": get_next_id(tasks),
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    tasks.append(new_task)
    save_tasks(tasks)

    flash("Task added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/done/<int:task_id>")
def mark_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            flash("Task marked as completed.", "success")
            return redirect(url_for("index"))

    flash("Task not found.", "error")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        flash("Task not found.", "error")
    else:
        save_tasks(new_tasks)
        flash("Task deleted.", "success")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
