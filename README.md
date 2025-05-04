# 📝 Django Task Management API (By AarDG10)

This project is a RESTful **Task Management System** built using **Django** and **Django REST Framework**. It supports full **CRUD operations** (Create, Read, Update, Delete) for TODO tasks. Each task consists of a `title`, `description`, `date`, and `completed` status.

---

## 🚀 Features

- Create a new task
- View all tasks
- Filter tasks by:
  - Title
  - Date
  - Sort by Date
- Edit a task
- Delete a task

---

## 📦 Technologies Used

- Python
- Django
- Django REST Framework
- Docker & Docker Compose
- Postman (For Testing)

---

## 🛠️ Setup & Build Instructions
- ### Docker Build
    - docker-compose up --build
- The Api will then be available at http://localhost:8000/tasks/

## Api Endpoints
- **POST** http://localhost:8000/tasks/ [To create a new task with a title, optional description, and date.]
- **GET**  http://localhost:8000/tasks/ [To get the Tasks List]
    - ### *For Filter*
        - http://localhost:8000/tasks/?search=%title% [To filter the Tasks based on Title]
        - http://localhost:8000/tasks/?search_date=%date% [To filter the Tasks based on the Date]
        - http://localhost:8000/tasks/?sort_by_date=true [To sort the dates (increasing/serial order) based on a boolean value]
- **PATCH** http://localhost:8000/tasks/<id>/ [To Partial Edit a task that has been listed]
- **DELETE** http://localhost:8000/tasks/<id>/ [To Delete a Task from the List]


## JSON DATA (Raw) Example
-   {
        "title": "Buy groceries",
        "description": "Bread and Butter",
        "date": "2025-05-04"
    }