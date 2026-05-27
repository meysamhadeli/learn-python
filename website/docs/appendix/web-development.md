# Web Development

## The Landscape

Python has mature web frameworks for every use case:

| Framework | Best For |
|-----------|---------|
| `FastAPI` | Modern async REST APIs with auto-generated docs |
| `Flask` | Simple web apps and APIs, minimal overhead |
| `Django` | Full-stack web apps — ORM, admin, auth, templates |
| `Starlette` | Lightweight async framework (FastAPI is built on it) |
| `aiohttp` | Async web server and client |

## FastAPI — Modern APIs

FastAPI is the recommended choice for new REST APIs. It uses Python type annotations to:
- Validate request/response data automatically (via Pydantic)
- Generate interactive API docs at `/docs` (Swagger UI) and `/redoc`
- Run async handlers natively

```bash
pip install fastapi uvicorn[standard]
uvicorn main:app --reload   # auto-reloads on file save
```

```python
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="My API", version="1.0.0")

# In-memory store (use a real database in production)
users: dict[int, dict] = {}
next_id = 1

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(UserCreate):
    id: int

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global next_id
    new_user = {"id": next_id, **user.model_dump()}
    users[next_id] = new_user
    next_id += 1
    return new_user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
```

Visit `http://localhost:8000/docs` for an interactive browser-based API explorer.

## Flask — Minimal Web

Flask is a micro-framework — it gives you routing and request/response handling, and leaves everything else (database, auth) up to you:

```bash
pip install flask
```

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = [{"id": 1, "title": "Buy groceries", "done": False}]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        abort(404)
    return jsonify(task)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(force=True)
    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(debug=True)
```

## Django — Full Stack

Django follows the "batteries included" philosophy — it ships with an ORM, admin panel, auth, form handling, and templating out of the box:

```bash
pip install django
django-admin startproject mysite
python manage.py startapp blog
python manage.py runserver
```

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

# blog/views.py
from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = list(Post.objects.values("id", "title", "published"))
    return JsonResponse(posts, safe=False)
```

Django's admin panel (`/admin/`) can give you a full CRUD-style interface for your models with very little extra setup.

## Choosing a Framework

- **New REST API** → FastAPI (async, type-safe, auto-docs)
- **Simple script/prototype** → Flask (minimal setup)
- **Complex web application** → Django (ORM, admin, auth, form validation all included)
