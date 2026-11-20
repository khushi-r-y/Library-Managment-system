# Library Management System

Intermediate Django project with authentication, dashboard, books, physical book copies, members, issuing/returning, reservations/fines models, Django admin and REST APIs.

## Windows setup
Open this folder in VS Code. Open Terminal in the folder containing manage.py:

```bash
python -m venv env
env\\Scripts\\activate
pip install -r requirements.txt
python manage.py makemigrations accounts books circulation
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and sign in with the superuser credentials.
Admin: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/api/

Staff users can manage books, members and circulation. Create categories and books in Django admin, then add book copies. Add members from the Members page.

## API endpoints
GET/POST /api/categories/
GET/POST /api/books/
GET/POST /api/copies/
GET/POST /api/members/
GET/POST /api/borrow-records/
POST /api/borrow-records/{id}/return_book/
GET/POST /api/reservations/
GET/POST /api/fines/

APIs require authentication (session or Basic Auth). Example book JSON:
```json
{"title":"Python Programming","isbn":"9781234567890","author":"John Smith","publisher":"Example Press","category":1,"published_date":"2024-01-15","description":"Python guide"}
```

Educational starter only. Change SECRET_KEY and DEBUG settings before deployment.
