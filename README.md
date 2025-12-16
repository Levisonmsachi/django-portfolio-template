# 🎯 Portfolio Website

A modern, responsive portfolio website built with **Django** to showcase your professional projects, skills, and achievements in an elegant and professional manner.

---

## ✨ Features

- **🏠 Home Page** – Create a captivating landing page to welcome visitors
- **👤 About Me** – Share your background, skills, and professional journey
- **💼 Projects Showcase** – Display your portfolio projects with descriptions
- **📬 Contact Section** – Enable visitors to get in touch with you
- **🎨 Responsive Design** – Beautiful UI that adapts to all devices
- **⚡ Custom Error Pages** – Professional 404 error handling
- **🚀 Production Ready** – Optimized settings and security configurations

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3** | Core programming language |
| **Django 6.0** | Web framework |
| **HTML5** | Markup structure |
| **CSS3** | Styling and responsive design |
| **SQLite** | Database (default) |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** – [Download here](https://www.python.org/downloads/)
- **pip** – Python package manager (included with Python)
- **Git** – Version control (optional)

---

## 🚀 Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
2. Create a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install django
4. Apply Migrations
python manage.py migrate
5. Run the Development Server
Run in terminal
python manage.py runserver
Visit your portfolio at: http://127.0.0.1:8000/

📁 Project Structure
portfolio/
├── portfolio/               # Project settings and configuration
│   ├── settings.py         # Django configuration
│   ├── urls.py             # Main URL routing
│   ├── wsgi.py             # WSGI application
│   └── asgi.py             # ASGI application
├── main/                   # Main application
│   ├── templates/          # HTML templates
│   │   ├── main/
│   │   │   ├── base.html   # Base template
│   │   │   ├── home.html   # Home page
│   │   │   ├── about.html  # About page
│   │   │   ├── projects.html # Projects page
│   │   │   ├── contact.html # Contact page
│   │   │   └── 404.html    # 404 error page
│   │   └── ...
│   ├── static/             # Static files (CSS, JS, images)
│   ├── views.py            # View functions
│   ├── urls.py             # App URL routing
│   ├── models.py           # Database models
│   └── ...
├── manage.py               # Django management script
└── db.sqlite3              # SQLite database
🎯 Available Routes
| Route | Page | Description | |-------|------|-------------| | / | Home | Welcome page with introduction | | /about/ | About | Your background and skills | | /projects/ | Projects | Showcase of your work | | /contact/ | Contact | Contact form or information | | /404/ | 404 Error | Custom error page (for testing) |

🎨 Customization
Update Your Information
Edit main/templates/main/home.html:

<!-- Customize your name and headline -->
<h1>Your Name</h1>
<p>Your Professional Title</p>
Edit main/templates/main/about.html:

<!-- Update your bio and skills -->
<h1>About Me</h1>
<p>Your biography here...</p>
Edit main/views.py:

# Add your projects to the projects view
my_projects = [
    {'name': 'Your Project', 'description': 'Description here'},
    # Add more projects...
]
⚙️ Configuration
Development vs. Production
The settings.py file is configured for development. For production deployment:

# settings.py

# Set to False in production
DEBUG = False

# Add your domain
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Configure static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
🌐 Deployment
Deploy to Heroku
Create a Procfile:
web: gunicorn portfolio.wsgi
Install production requirements:
pip install gunicorn psycopg2-binary python-decouple
Push to Heroku:
heroku create your-app-name
git push heroku main
Deploy to PythonAnywhere
Visit PythonAnywhere.com
Upload your project
Configure a Web app with Django
Set static files mapping
🔒 Security Best Practices
Keep your SECRET_KEY confidential
Use environment variables for sensitive data
Set DEBUG = False in production
Use HTTPS in production
Keep Django and dependencies updated
📦 Adding More Features
Create a New App
python manage.py startapp blog
Create Models
# blog/models.py
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
Register in Admin
# blog/admin.py
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
🧪 Testing
Run tests with:

python manage.py test
Create test files in main/tests.py and follow Django testing best practices.

📚 Learning Resources
Django Documentation – Official Django docs
Python.org – Python resources
MDN Web Docs – HTML/CSS reference
Real Python – In-depth tutorials
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

💬 Support
Have questions or need help?

Open an Issue
Check existing documentation
Review Django official docs
🌟 Acknowledgments
Built with Django – A powerful web framework
Inspired by modern portfolio design principles
Thanks to the open-source community
Made with ❤️ by LEVVIE-LIVVIE
