# Django Blog API with Swagger UI Documentation

This repository contains a Django REST Framework-based Blog API with interactive documentation powered by Swagger UI. The API allows users to create, read, update, and delete blog posts, comments, and categories, with comprehensive API documentation available through an interactive interface.

## Features

* RESTful API for managing blog posts, comments, and categories
* Interactive API documentation with Swagger UI
* User authentication and permissions
* Nested routing for post comments
* Automatic OpenAPI schema generation

## Prerequisites

* Python 3.10+
* Django 4.2+
* Django REST Framework
* drf-spectacular
* drf-nested-routers

## Installation

**Clone the repository:**

```bash
git clone https://github.com/yourusername/blogapi.git
cd blogapi
```

**Create and activate a virtual environment:**

```bash
conda create -n blogapi_env python=3.10
conda activate blogapi_env
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Create a superuser:**

```bash
python manage.py createsuperuser
```

**Start the development server:**

```bash
python manage.py runserver
```

## API Endpoints

The API provides the following endpoints:

### Posts

```
GET /api/posts/ - List all posts
POST /api/posts/ - Create a new post
GET /api/posts/{id}/ - Retrieve a post
PUT /api/posts/{id}/ - Update a post
DELETE /api/posts/{id}/ - Delete a post
```

### Comments

```
GET /api/posts/{post_id}/comments/ - List comments for a post
POST /api/posts/{post_id}/comments/ - Create a comment on a post
GET /api/posts/{post_id}/comments/{id}/ - Retrieve a comment
PUT /api/posts/{post_id}/comments/{id}/ - Update a comment
DELETE /api/posts/{post_id}/comments/{id}/ - Delete a comment
```

### Categories

```
GET /api/categories/ - List all categories
POST /api/categories/ - Create a new category
GET /api/categories/{id}/ - Retrieve a category
PUT /api/categories/{id}/ - Update a category
DELETE /api/categories/{id}/ - Delete a category
```

### Documentation

```
/api/docs/ - Swagger UI documentation interface
/api/schema/ - OpenAPI schema
```

## API Documentation

After starting the server, visit `http://127.0.0.1:8000/api/docs/` to access the interactive API documentation powered by Swagger UI.