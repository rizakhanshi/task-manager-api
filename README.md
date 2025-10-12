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
