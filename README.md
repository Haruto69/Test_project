# Django Authentication System

A simple Django-based user authentication system with a custom login and registration interface, styled using TailwindCSS. Includes admin access and flash messaging support.

## 🚀 Features

- User registration and login  
- Floating labels and password visibility toggle  
- Responsive, modern UI with TailwindCSS  
- Django admin panel for managing users  
- Flash message support for errors and notifications  

## 📁 Project Structure

C:.
└───Test_project-main  
    │   .gitignore  
    │   manage.py  
    │  
    ├───accounts  
    │   │   admin.py  
    │   │   apps.py  
    │   │   forms.py  
    │   │   models.py  
    │   │   urls.py  
    │   │   views.py  
    │   │  
    │   ├───migrations  
    │   │       0001_initial.py  
    │   │       __init__.py  
    │   │  
    │   └───templates  
    │       ├───accounts  
    │       │       base.html  
    │       │       login.html  
    │       │       register.html  
    │       │       welcome.html  
    │       │  
    │       └───registration  
    │               logged_out.html  
    │  
    ├───auth_project  
    │       asgi.py  
    │       settings.py  
    │       urls.py  
    │       wsgi.py  
    │  
    └───static  
        ├───css  
        │       styles.css  
        │  
        └───js  
                app.js

## 🧩 Setup Instructions

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/django-auth-system.git  
   cd Test_project-main  
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```

4. Run migrations:  
   ```bash
   python manage.py migrate  
   ```

5. Create a superuser:  
   ```bash
   python manage.py createsuperuser  
   ```

6. Start the development server:  
   ```bash
   python manage.py runserver  
   ```

7. Access the app:  
   - Login/Register: http://127.0.0.1:8000/login/  
   - Admin Panel: http://127.0.0.1:8000/admin/  

## 📜 License

This project is licensed under the MIT License.
