# 📝 Django Blog Application

A clean and modular **Django-based Blog Application** featuring user authentication, blog creation, personal blog management, and secure logout.
This project follows standard Django conventions and is structured for scalability, readability, and future GSOC-level enhancements.

---

## 🚀 Features

### ✅ User Authentication

* User Registration
* User Login
* User Logout
* Form validation & secure session handling

### 📰 Blog Functionality

* Create blog posts
* View your own posts
* View posts by other users (optional to add later)
* Clean separation of templates, static files, and Django apps

### ⚙️ Tech Stack

* **Backend:** Django
* **Database:** SQLite3 (default, can be swapped for PostgreSQL/MySQL)
* **Frontend:** Django Templates + Static files
* **Environment:** Python virtual environment (venv)

---

## 📂 Project Structure

```
django_blog/
├── blog/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── django_blog/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── db.sqlite3
├── manage.py
```

---

## 🛠️ Installation & Setup

Follow the steps to run the project locally:

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/django-blog.git
cd django-blog
```

### 2️⃣ Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```
python manage.py migrate
```

### 5️⃣ Run the development server

```
python manage.py runserver
```

App will be available at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧩 How It Works

### 🔐 Authentication

* Django’s built-in `User` model is used.
* Session-based login & logout.

### 📝 Blog Model

A simple model (title, content, date, author) that stores user-associated blog entries.

### 📑 Templates

* Clean template structure inside `/blog/templates/`
* Base template for consistent UI

---

## 📌 Commands for Development

### Create a superuser

```
python manage.py createsuperuser
```

### Collect static files (for production)

```
python manage.py collectstatic
```

---

## 📘 Future Enhancements

* Rich Text Editor (Quill/CKEditor)
* Comment System
* Tag-based filtering
* REST API (Django REST Framework)
* Docker support
* JWT-based authentication
* CI/CD Pipeline

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues and submit pull requests.

---

## 📄 License

This project is licensed under the **MIT License**.
