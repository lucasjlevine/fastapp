# 🚀 FastApp

**FastApp** is a lightweight, file-based fullstack framework built on top of FastAPI. It combines automatic routing, Jinja templates, and simple project structure — inspired by SvelteKit’s file-based routing but fully Pythonic.

---

## 📦 Features

✅ **File-based routing**: Every folder in `/app` becomes a route.  
✅ **Dynamic parameters**: Use `{}` in folder names for FastAPI-style dynamic routes.  
✅ **Jinja templating**: Built-in Jinja2 with a global `/templates` directory for layouts & components.  
✅ **Static pages**: Drop in a `+page.jinja` without Python code and get an automatic route.  
✅ **FastAPI power**: Use the full FastAPI ecosystem (dependencies, middleware, etc.).  
✅ **Hot reload**: Works with `uvicorn` reload/workers out of the box.  

---

## 📂 Project Structure
```
project/
│ .env
| fastapp.py
│ main.py
│ /app
│   +page.py          # → "/"
│   +page.jinja       # Template for "/"
│   /hello
|     +page.jinja     # -> /hello
│     /{name}
│       +page.py      # → "/hello/{name}"
│       +page.jinja
│ /templates
│   base.jinja        # Global templates/layouts
| /static
|   
```

---

## 🚀 Getting Started

### 1️⃣ Install dependencies

```bash
pip install fastapi uvicorn jinja2 python-dotenv
```

### 2️⃣ Create main.py

```python
from fastapp import FastApp

app = FastApp()

if __name__ == "__main__":
    app.run()
```

- FastApp() scans /app and builds routes automatically.
- .run() uses an import string internally so hot reload and workers work.

### 3️⃣ Environment variables (.env)
```bash
HOST=127.0.0.1
PORT=8000
RELOAD=True
```

## 🛠️ Routes

### 📄 Static Page

/app/+page.jinja:
```jinja
{% extends "base.jinja" %}

{% block content %}
<h1>Welcome to FastApp!</h1>
<p>This is a simple FastAPI application using FastApp.</p>
<p>FastApp is a framework that simplifies FastAPI development.</p>
{% endblock %}
```
Visit /static → rendered automatically.
No Python code required.

### 🌀 Dynamic Route

/app/hello/{name}/+page.py:
```python
from fastapp import FastAppRouter, Request

router = FastAppRouter()


@router.get("/")
async def dynamic_page(request: Request, name: str):
    return router.render({"name": name})
```

/app/dynamic/{id}/+page.jinja:
```jinja
{% extends "base.jinja" %}

{% block content %}
<p>Hello, {{ name }}!</p>
{% endblock %}
```
Visit /hello/lucas → Hello, lucas!.

## 🎨 Templates
- /templates stores shared layouts and components:
```
/templates
  base.jinja
  /components
    header.jinja
```

- Accessible from any page via standard Jinja:
```jinja
{% extends "base.jinja" %}
{% include "components/header.jinja" %}
```