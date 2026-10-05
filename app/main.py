from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

app = FastAPI()

# Mount static files
static_dir = Path(__file__).parent.parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Sample data for demo
tasks = [
    {
        "id": 1,
        "title": "Prepare interview demo",
        "description": "Build a polished project for discussion",
        "status": "In Progress",
        "priority": "High",
        "assigned_to": "Candidate"
    }
]

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Render the main dashboard"""
    return render_template("index.html")

@app.get("/api/tasks")
async def get_tasks():
    """Get all tasks"""
    return tasks

@app.post("/api/tasks")
async def create_task(task: dict):
    """Create a new task"""
    new_task = {
        "id": max([t["id"] for t in tasks]) + 1 if tasks else 1,
        **task
    }
    tasks.append(new_task)
    return new_task

@app.put("/api/tasks/{task_id}")
async def update_task(task_id: int, task: dict):
    """Update an existing task"""
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i].update(task)
            return tasks[i]
    return {"error": "Task not found"}

@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task"""
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Task deleted"}

def render_template(template_name: str) -> str:
    """Simple template rendering"""
    template_path = Path(__file__).parent.parent / "templates" / template_name
    if template_path.exists():
        return template_path.read_text()
    return "<h1>Template not found</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
