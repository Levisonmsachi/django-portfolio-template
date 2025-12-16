<div align="center">

<h1>Portfolio Website</h1>

<p><strong>Modern • Responsive • Professional</strong></p>

<p>
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge" />
</p>

</div>

---

## Overview

A clean, scalable, and fully responsive **portfolio website built with Django**. Designed to showcase projects, skills, and experience with a professional layout that looks great on desktop, tablet, and mobile.

This project follows Django best practices and is structured for **easy customization**, **future expansion**, and **production deployment**.

---

## Key Features

<ul>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/homeassistant.svg" width="14"/> Home Page – Strong landing section with introduction</li>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/aboutdotme.svg" width="14"/> About Section – Personal background, skills, and journey</li>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/github.svg" width="14"/> Projects Showcase – Highlight featured work</li>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/minutemailer.svg" width="14"/> Contact Page – Easy communication channel</li>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/responsive.svg" width="14"/> Fully Responsive – Optimized for all screen sizes</li>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/bugcrowd.svg" width="14"/> Custom 404 Page – Clean error handling</li>
  <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/securityscorecard.svg" width="14"/> Secure & Scalable – Ready for production</li>
</ul>

---

## Tech Stack

| Technology                                                                                      | Role             |
| ----------------------------------------------------------------------------------------------- | ---------------- |
| <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/python.svg" width="14"/> Python 3 | Core language    |
| <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/django.svg" width="14"/> Django   | Web framework    |
| <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/html5.svg" width="14"/> HTML5     | Markup           |
| <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/css3.svg" width="14"/> CSS3       | Styling & layout |
| <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/sqlite.svg" width="14"/> SQLite   | Default database |

---

## Prerequisites

Ensure the following tools are installed:

* <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/python.svg" width="14"/> Python **3.8+**
* <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/pypi.svg" width="14"/> pip
* <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/git.svg" width="14"/> Git (optional)

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
portfolio/
│
├── portfolio/            # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── main/                 # Core application
│   ├── templates/
│   │   └── main/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── projects.html
│   │       ├── contact.html
│   │       └── 404.html
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── manage.py
└── db.sqlite3
```

---

## Routes

| URL          | Page     | Description         |
| ------------ | -------- | ------------------- |
| `/`          | Home     | Landing page        |
| `/about/`    | About    | Background & skills |
| `/projects/` | Projects | Portfolio showcase  |
| `/contact/`  | Contact  | Contact details     |
| `/404/`      | Error    | Custom error page   |

---

## Customization Guide

### Update Home Page

`main/templates/main/home.html`

```html
<h1>Your Name</h1>
<p>Your Professional Title</p>
```

### Update About Page

`main/templates/main/about.html`

```html
<h1>About Me</h1>
<p>Your biography here...</p>
```

### Add Projects

`main/views.py`

```python
my_projects = [
    {"name": "Project Name", "description": "Project description"},
]
```

---

## Production Configuration

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## Deployment Options

### Heroku

```bash
pip install gunicorn psycopg2-binary python-decouple
```

`Procfile`

```
web: gunicorn portfolio.wsgi
```

### PythonAnywhere

* Upload project
* Configure Django web app
* Map static files

---

## Security Best Practices

* Keep `SECRET_KEY` private
* Use environment variables
* Disable `DEBUG` in production
* Enable HTTPS
* Update dependencies regularly

---

## Testing

```bash
python manage.py test
```

---

## Learning Resources

* Django Documentation
* Python.org
* MDN Web Docs
* Real Python

---

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

## Author

<strong>LEVVIE-LIVVIE</strong>
Built with Django • Designed for growth

---

<div align="center">

<img src="https://img.shields.io/badge/Open_Source-Contributions_Welcome-blue?style=for-the-badge" />

</div>
