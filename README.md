# Interview Demo: FastAPI + jQuery + Jinja2 Task Manager

This repository is a simple full-stack interview demo built with:
- Python + FastAPI
- JavaScript + jQuery
- HTML + Jinja2 templates
- SQLite for persistence

It showcases a clean, practical application that can be discussed during an interview: a task board with CRUD operations, validation, and a polished UI.

## Features
- Add new tasks
- Update task status and priority
- Delete tasks
- View tasks in a dashboard format
- REST API endpoints for backend interaction
- HTML rendered server-side using Jinja2
- AJAX requests using jQuery

## Tech stack
- FastAPI
- Jinja2
- jQuery
- SQLite

## Run locally

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Open the app:
   ```text
   http://127.0.0.1:8000
   ```

## API examples

- GET `/api/tasks`
- POST `/api/tasks`
- PUT `/api/tasks/{id}`
- DELETE `/api/tasks/{id}`

Example POST request:

```json
{
  "title": "Prepare interview demo",
  "description": "Build a polished project for discussion",
  "status": "In Progress",
  "priority": "High",
  "assigned_to": "Candidate"
}
```

## Project purpose
This app is intentionally small but realistic. It demonstrates:
- API design
- Server-side rendering
- Front-end interactivity
- Data persistence
- Error handling
- Clean code structure

## License
MIT
