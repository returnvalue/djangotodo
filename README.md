# Django Todo App

This repository contains a small web-based Todo list built with **Django 5** and styled with **Bulma**. The app lets you create tasks, mark them as complete or incomplete, edit existing entries and delete them entirely.

## Features

- Add new tasks from the navigation bar
- List all todos with visual feedback when they are completed
- Mark tasks as complete or incomplete
- Edit task text
- Remove tasks

## Getting Started

### Installation

1. Install Python 3 and `pip` if they are not already on your system.
2. Install project dependencies:

```bash
pip install -r requirements.txt
```

### Running the Development Server

Run migrations and start the built-in Django server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://localhost:8000/` in your browser to access the app.

To edit a task, choose it from the list and click **Edit Task** in the navigation bar.

## Running Tests

A small test suite is included. Run it with:

```bash
python manage.py test
```

The `manage.py` script will fall back to Python's built-in `unittest` runner if Django is not installed.

## Notes

The database uses SQLite by default and comes with a few example tasks pre-populated in `db.sqlite3`. Feel free to delete the database file if you want to start fresh.

