# 🧾 Employee Management System (Django + DRF)

A simple Django-based REST API for managing employees, departments, attendance, and performance records.

---

## 🔧 Features

- CRUD for Employees, Departments, Attendance
- PostgreSQL support
- DRF + Swagger UI (`/swagger/`)
- Data Seeder for fake employees
- Docker + docker-compose setup
- Environment configuration via `.env`

---

## 🗂️ Project Structure

```
employee-project/
├── employees/                  # App for employee logic
├── attendance/                 # App for attendance records
├── employee_project/           # Main project settings
├── .env                        # Environment variables (not committed)
├── .env.example                # Sample env
├── Dockerfile                  # Docker build config
├── docker-compose.yml          # Service config
├── entrypoint.sh               # Auto migrations + seed
└── manage.py
```

---

## 🚀 Running Locally (without Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

---

## 🐳 Running with Docker

```bash
docker-compose up --build
```

Visit: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## 🔐 Environment Variables (.env)

```
DEBUG=True
SECRET_KEY=django-insecure-key
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

## ✅ Endpoints

- `/api/employees/`
- `/api/attendance/`
- `/swagger/`

---

## 📦 Seeder Command

```bash
python manage.py seed_data
```

Generates fake employees and departments using `Faker`.

---

## 🧪 Coming Soon

- JWT Auth
- Chart.js visualizations
