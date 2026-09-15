# Student Management System - Django

A simple sample Django project for the AWS Phase 2 assignment.

## Features
- Add students
- View students
- Delete students
- SQLite database
- Simple responsive HTML interface

## Run locally

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create the database:
```bash
python manage.py migrate
```

Start the server:
```bash
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

## AWS deployment

See `docs/AWS_STEPS.md` and `docs/AWS_CHECKLIST.md`.
