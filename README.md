# 📚 Book Recommender API

A **Book Recommendation REST API** built with **Django** and **Django REST Framework**.
The project provides book search, recommendation, and analytics services based on a book dataset.

The API includes:

* Book CRUD API
* Book recommendation by author or title
* Rating distribution analytics
* Publisher statistics
* Pagination support
* Unified API response format
* API documentation

---

# 🧰 Tech Stack

* Python 3.10+
* Django
* Django REST Framework
* drf-spectacular (Swagger/OpenAPI)
* SQLite

---

# 📊 Dataset Source

This project uses the **Goodreads Books Dataset** available on Kaggle:

Dataset link:

https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks

## Dataset Description

The dataset was created to provide a **clean and structured collection of book information** suitable for data analysis and recommendation systems.

Many existing book datasets contain:

* Missing important attributes
* Poorly structured data
* Multiple fragmented files

To solve this problem, the dataset author used the **Goodreads API** to extract and clean book information into a single structured dataset containing useful numerical and categorical features.

The dataset includes information such as:

* Book title
* Authors
* Average rating
* Rating counts
* Publication year
* Publisher
* ISBN
* Language code
* Number of pages

These structured attributes make the dataset well-suited for:

* Data analysis
* Recommendation systems
* Rating analytics
* Book popularity insights

---

# 📦 Installation

## 1 Clone the repository

```bash
git clone https://github.com/Senxss19/book-recommender-api.git
cd book-recommender-api
```

---

## 2 Create virtual environment

```bash
python -m venv .venv
```

Activate environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

## 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5 Import dataset

```bash
python manage.py import_books
```

---

## 6 Run server

```bash
python manage.py runserver
```

Server will start at

```
http://127.0.0.1:8000
```

---

# 📄 API Documentation

Detailed API documentation is provided as a **PDF document**.

📄 **Download API Documentation**

https://github.com/Senxss19/book-recommender-api/blob/main/API.pdf

The API documentation includes:

* All available endpoints
* Request parameters
* Example requests
* Example responses
* Error codes
* Authentication description

Interactive API documentation is also available locally via Swagger UI:

```
http://127.0.0.1:8000/api/docs/
```

OpenAPI schema:

```
http://127.0.0.1:8000/api/schema/
```

---

# 📦 Unified Response Format

All APIs return a unified structure:

```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

Field description:

| Field   | Description               |
| ------- | ------------------------- |
| code    | status code (0 = success) |
| message | message text              |
| data    | returned data             |

---

# 📊 Features

* Book dataset import from CSV
* Author/title fuzzy search
* Top rated book recommendation
* Rating distribution analytics
* Publisher trend statistics
* Pagination support
* Swagger documentation
* Unified API response format

---

# 📁 Project Structure

```
book_recommender
│
├── config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── books
│   ├── management
│   │   └── commands
│   │       └── import_books.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│   ├── pagination.py
│   │
│   ├── services
│   │   ├── analytics.py
│   │   └── recommendation.py
│   │
│   └── utils
│       └── response.py
│
├── data
│   └── books.csv
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Future Improvements

* Machine learning recommendation algorithm
* User rating system
* Redis caching
* Elasticsearch full-text search
* Personalized recommendations

---

# 👨‍💻 Author

Developed for learning **Django REST API development** and **data-driven book recommendation systems**.
