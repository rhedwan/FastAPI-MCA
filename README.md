# FastAPI Bootcamp: Installation & Your First Route

This guide covers everything needed to get started with FastAPI using Astral's `uv` package manager and build your first API endpoint.

---

# Prerequisites

Before starting, ensure you have:

- A code editor (VS Code recommended)
- Terminal access
- Internet connection

No prior FastAPI experience is required.

---

# Installing Astral uv

Instead of using `pip`, this course uses `uv`, a fast Python package and project manager from Astral.

## macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

Example output:

```text
uv 0.x.x
```

---

# Creating a New FastAPI Project

Create a new project:

```bash
uv init fastapi-class
```

Move into the project directory:

```bash
cd fastapi-class
```

---

# Installing Python

Install Python 3.12:

```bash
uv python install 3.12
```

Pin the project to Python 3.12:

```bash
uv python pin 3.12
```

Verify:

```bash
uv run python --version
```

Expected output:

```text
Python 3.12.x
```

---

# Installing FastAPI

Install FastAPI and the Uvicorn server:

```bash
uv add fastapi uvicorn
```

This command:

- Creates a virtual environment
- Installs FastAPI
- Installs Uvicorn
- Updates project dependencies

## Activating the Virtual Environment

`uv` automatically uses the project's virtual environment when you run commands with `uv run`.

If you want to activate the virtual environment manually, use the command for your system:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

To deactivate the virtual environment:

```bash
deactivate
```

---

# Project Structure

Create a file called:

```text
main.py
```

Your project should look like:

```text
fastapi-class/
│
├── .venv/
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Creating Your First FastAPI Application

Open `main.py` and add:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

---

# Understanding the Code

## Import FastAPI

```python
from fastapi import FastAPI
```

This imports the FastAPI framework.

---

## Create the Application

```python
app = FastAPI()
```

This creates the FastAPI application instance.

Think of it as the main application object that manages all routes.

---

## Create a Route

```python
@app.get("/")
```

This tells FastAPI:

> When someone sends a GET request to "/", run the function below.

---

## Route Function

```python
def home():
    return {"message": "Hello FastAPI"}
```

When the route is visited, FastAPI returns JSON:

```json
{
  "message": "Hello FastAPI"
}
```

---

# Running the Application

Start the development server:

```bash
uv run uvicorn main:app --reload
```

Explanation:

- `main` → filename (`main.py`)
- `app` → FastAPI instance (`app = FastAPI()`)
- `--reload` → automatically restart when code changes

---

# Opening the Application

Once running, visit:

```text
http://127.0.0.1:8000
```

You should see:

```json
{
  "message": "Hello FastAPI"
}
```

---

# Automatic API Documentation

FastAPI automatically generates API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You will see an interactive Swagger UI where you can test your endpoints without Postman.

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# Creating Another Route

Add another endpoint:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/about")
def about():
    return {"course": "FastAPI Bootcamp"}
```

Now you have two endpoints:

```text
GET /
GET /about
```

Visit:

```text
http://127.0.0.1:8000/about
```

Response:

```json
{
  "course": "FastAPI Bootcamp"
}
```

---

# Practice Exercise

Create the following routes:

```text
GET /
GET /about
GET /health
```

Expected response for `/health`:

```json
{
  "status": "running"
}
```

