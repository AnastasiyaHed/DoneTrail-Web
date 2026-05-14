from flask import Flask, render_template, request, redirect, url_for
import json
from pathlib import Path
from datetime import datetime


app = Flask(__name__)

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
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if not title or title.strip() == "":
        return redirect(url_for("index"))
    tasks = load_tasks()

    new_id = get_next_id(tasks)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_task = {
        "id": new_id,
        "title": title.strip(),
        "done": False,
        "created_at": now
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return redirect(url_for("index"))


@app.route("/done/<int:task_id>")
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
