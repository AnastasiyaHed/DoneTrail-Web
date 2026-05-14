# DoneTrail Web

DoneTrail Web is a small Flask web application for creating, tracking and completing personal tasks.

The project is a web version of the DoneTrail command-line application. Tasks are stored in a JSON file and can be managed through a browser interface.

---

# DoneTrail Web

DoneTrail Web — это небольшое веб-приложение на Flask для создания, отслеживания и завершения личных задач.

Проект является веб-версией консольного приложения DoneTrail. Задачи сохраняются в JSON-файл и управляются через браузерный интерфейс.

---

## Features

- View all tasks on the main page
- Add new tasks through an HTML form
- Mark tasks as completed
- Delete tasks
- Store tasks in a JSON file
- Automatically generate task IDs
- Save task creation date and time
- Use Flask routes and Jinja2 templates

## Возможности

- Просмотр всех задач на главной странице
- Добавление новых задач через HTML-форму
- Отметка задач как выполненных
- Удаление задач
- Хранение задач в JSON-файле
- Автоматическая генерация ID задачи
- Сохранение даты и времени создания задачи
- Использование маршрутов Flask и шаблонов Jinja2

---

## Technologies

- Python
- Flask
- Jinja2
- HTML
- JSON
- pathlib
- datetime

## Технологии

- Python
- Flask
- Jinja2
- HTML
- JSON
- pathlib
- datetime

---

## Project Structure

```text
donetrail-web/
│
├── app.py
├── tasks.json
├── requirements.txt
├── README.md
│
└── templates/
    ├── base.html
    └── index.html
```

## Структура проекта

```text
donetrail-web/
│
├── app.py
├── tasks.json
├── requirements.txt
├── README.md
│
└── templates/
    ├── base.html
    └── index.html
```

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask
```

Or install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Установка

Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
```

Активация на Windows:

```bash
venv\Scripts\activate
```

Установите зависимости:

```bash
pip install flask
```

Или установите зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## Использование

Запустите приложение:

```bash
python app.py
```

Откройте приложение в браузере:

```text
http://127.0.0.1:5000/
```

---

## Routes

| Route | Method | Description |
|---|---:|---|
| `/` | GET | Shows the task list |
| `/add` | POST | Adds a new task |
| `/done/<task_id>` | GET | Marks a task as completed |
| `/delete/<task_id>` | GET | Deletes a task |

## Маршруты

| Маршрут | Метод | Описание |
|---|---:|---|
| `/` | GET | Показывает список задач |
| `/add` | POST | Добавляет новую задачу |
| `/done/<task_id>` | GET | Отмечает задачу как выполненную |
| `/delete/<task_id>` | GET | Удаляет задачу |

---

## Data Storage

Tasks are stored in the `tasks.json` file.

Example:

```json
[
  {
    "id": 1,
    "title": "Learn Flask",
    "done": false,
    "created_at": "2026-05-14 15:30:00"
  }
]
```

If the file is empty or corrupted, the application returns an empty task list.

## Хранение данных

Задачи сохраняются в файл `tasks.json`.

Пример:

```json
[
  {
    "id": 1,
    "title": "Learn Flask",
    "done": false,
    "created_at": "2026-05-14 15:30:00"
  }
]
```

Если файл пустой или повреждён, приложение возвращает пустой список задач.

---

## Example Interface

The main page allows the user to:

- enter a task title;
- add the task;
- view all saved tasks;
- mark a task as completed;
- delete a task.

## Пример интерфейса

Главная страница позволяет пользователю:

- ввести название задачи;
- добавить задачу;
- посмотреть все сохранённые задачи;
- отметить задачу как выполненную;
- удалить задачу.

---

## What This Project Demonstrates

This project demonstrates the basics of Flask web development:

- creating a Flask application;
- working with routes;
- handling form data with `request.form`;
- redirecting users after actions;
- using `url_for`;
- rendering HTML templates with Jinja2;
- storing simple data in a JSON file.

## Что показывает этот проект

Этот проект демонстрирует основы веб-разработки на Flask:

- создание Flask-приложения;
- работу с маршрутами;
- обработку данных формы через `request.form`;
- перенаправление пользователя после действий;
- использование `url_for`;
- рендеринг HTML-шаблонов через Jinja2;
- хранение простых данных в JSON-файле.