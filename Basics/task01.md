# FastAPI Assignment: Daily Todo API

## Objective

Practice:

- Path Parameters
- Query Parameters
- Request Body
- Basic Validation (`str`, `int`)

---

## Create a Todo Model

```python
class Todo(BaseModel):
    title: str
    priority: int
```

---

## Task 1: Get a Todo

Create:

```text
GET /todos/{todo_id}
```

Example:

```text
GET /todos/1
```

Response:

```json
{
  "todo_id": 1
}
```

---

## Task 2: Filter Todos

Create:

```text
GET /todos
```

Accept query parameters:

- `status: str`
- `limit: int`

Example:

```text
GET /todos?status=completed&limit=5
```

Response:

```json
{
  "status": "completed",
  "limit": 5
}
```

---

## Task 3: Create a Todo

Create:

```text
POST /todos
```

Request Body:

```json
{
  "title": "Study FastAPI",
  "priority": 1
}
```

Response:

```json
{
  "message": "Todo created",
  "todo": {
    "title": "Study FastAPI",
    "priority": 1
  }
}
```

---

## Task 4: Update a Todo

Create:

```text
PUT /todos/{todo_id}
```

Example:

```text
PUT /todos/3
```

Request Body:

```json
{
  "title": "Complete Assignment",
  "priority": 2
}
```

Response:

```json
{
  "todo_id": 3,
  "todo": {
    "title": "Complete Assignment",
    "priority": 2
  }
}
```

---

## Requirements

- Use `int` for IDs and priority.
- Use `str` for title and status.
- Use a Pydantic model for the request body.
- Test all endpoints using `/docs`.
