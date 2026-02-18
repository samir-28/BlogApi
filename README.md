#  Role-Based Blog API

A **Django REST Framework (DRF)** backend API with **JWT authentication** and **role-based access**.  
Supports **ADMIN, AUTHOR, and READER** roles with permissions for creating, editing, publishing, and viewing blogs.

---

##  Features

- **Custom User Model** with roles: `ADMIN`, `AUTHOR`, `READER`  
- **JWT Authentication**  
- **Blog CRUD**:
  - `ADMIN`: Full access  
  - `AUTHOR`: Create blogs, update/delete own  
  - `READER`: View published blogs only  
- **Custom Actions**:
  - `/blogs/{id}/publish/` → Only ADMIN can publish  
  - `/blogs/my_blogs/` → Lists blogs of the logged-in user  
- **PostgreSQL** database  
- **Custom management command**: `python manage.py create_user`  

---

## Tech Stack

- Python 3.11+  
- Django 5+  
- Django REST Framework  
- PostgreSQL  
- JWT Authentication (SimpleJWT)  

---

## Installation

1. **Clone the repo**

```bash
git clone <repo_url>
cd <repo_folder>
```
## Create virtual environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
---

## Install dependencies
```
pip install -r requirements.txt
```

## Configure PostgreSQL
```
Update config/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Create the database:
```
CREATE DATABASE blog_db;

Run migrations

python manage.py makemigrations
python manage.py migrate


Create users

python manage.py create_user


Start server

python manage.py runserver

```
API base URL: http://127.0.0.1:8000/api/

Authentication
```
POST /api/token/ → Get JWT access token

POST /api/token/refresh/ → Refresh token
```
Include token in headers for protected endpoints:

Authorization: Bearer <access_token>
```
/api/blogs/	GET	List blogs	ADMIN (all), AUTHOR (own), READER (published)
/api/blogs/	POST	Create blog	ADMIN, AUTHOR
/api/blogs/{id}/	GET	Retrieve blog	All (role-restricted)
/api/blogs/{id}/	PUT/PATCH	Update blog	ADMIN (all), AUTHOR (own)
/api/blogs/{id}/	DELETE	Delete blog	ADMIN (all), AUTHOR (own)
/api/blogs/{id}/publish/	POST	Publish blog	ADMIN only
/api/blogs/my_blogs/	GET	List user’s blogs	AUTHOR, ADMIN
```
---
## Project Structure
```
config/          # Django project settings
accounts/        # Custom user model, user management
blogs/           # Blog model, serializers, viewsets, permissions
manage.py        # Django management commands
requirements.txt # Project dependencies
```
