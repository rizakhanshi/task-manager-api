# Task Manager API

This repository contains the Task Manager API — a Django + Django REST Framework application that allows users to manage personal tasks. The API supports creating, reading, updating, deleting, and marking tasks as complete or incomplete. Tasks are owned by users and are only visible to their owners.

## Quickstart

1. Clone the repository:

   git clone https://github.com/rizakhanshi/task-manager-api.git
   cd task-manager-api

2. Create a virtual environment and install dependencies:

   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\Activate.ps1 on Windows
   pip install -r requirements.txt

3. Apply migrations and create a superuser:

   python manage.py migrate
   python manage.py createsuperuser

4. Run the development server:

   python manage.py runserver

5. Visit the API at `http://127.0.0.1:8000/api/` and the admin at `/admin/`.

## API Endpoints

- `GET /api/tasks/` — list authenticated user's tasks with optional filters and ordering
- `POST /api/tasks/` — create a new task
- `GET /api/tasks/{id}/` — retrieve a task (must be owner)
- `PUT /api/tasks/{id}/` — update a task (cannot edit a completed task)
- `DELETE /api/tasks/{id}/` — delete a task
- `POST /api/tasks/{id}/mark_complete/` — mark task as complete (sets `completed_at`)
- `POST /api/tasks/{id}/mark_incomplete/` — mark task as incomplete

Filtering: use query params `status`, `priority`, and `due_date`.
Ordering: use `?ordering=due_date` or `?ordering=priority`.

## Authentication

The API uses Django's session authentication and token authentication by default. Obtain a token via DRF's token endpoints (if enabled) or use the admin interface to manage users.

## Model behavior and validations

- Tasks have `title`, `description`, `due_date`, `priority` (low/medium/high), `status` (pending/completed), `owner`, and `completed_at` timestamp.
- `due_date` must be a future date. Attempts to save a task with a past due date will raise a validation error.
- Completed tasks cannot be edited. To change a completed task, mark it incomplete first.

## Tests

Run tests with:

   pytest -q

## Deployment

You can deploy this app to platforms like Heroku or PythonAnywhere. Add a `Procfile`, configure environment variables for `SECRET_KEY` and `DEBUG=False`, and use a production-ready database like PostgreSQL for deployed environments.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT
# Task Management API

A Django + Django REST Framework API for managing tasks.  
Built as the ALX Backend Engineering capstone. Features: JWT auth, CRUD tasks, mark complete/incomplete, filters, ordering, and deployment notes.

## Features
- User registration & JWT authentication
- Create / Read / Update / Delete tasks
- Mark tasks complete / incomplete with timestamp
- Task ownership (users only see their tasks)
- Filters (status, priority, due date) and ordering (due date, priority)
- Pagination
- Docker-ready and deployment notes for Render

## Tech stack
- Python 3.11+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (JWT)
- PostgreSQL (recommended in production)
- Docker (optional)

## Repository layout (recommended)
