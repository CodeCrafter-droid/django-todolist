📝 Django Todo List Application
A full-stack Todo List web application built using Django that allows users to manage their daily tasks efficiently with authentication, priority-based task management, and deployment-ready configuration.
The project is deployed on Render and supports both web UI and REST APIs for future integrations.

🚀 Features
👤 User Management
User registration and login
Secure authentication using Django sessions
Logout functionality
Account deletion with password confirmation
Separate views for logged-in and non-logged-in users

✅ Task Management
Create, update, and delete tasks
Priority-based tasks (High / Medium / Low)
Tasks ordered by:
Priority (High → Low)
Last updated time
Each user can access only their own tasks

🔐 Security
CSRF protection enabled
Login-required views for protected pages
Secure password verification before account deletion
Environment variables used for sensitive data (SECRET_KEY, database credentials)

🌐 REST API (Django REST Framework)
RESTful API endpoints for task management
API returns JSON responses
Token-based authentication support (ready for mobile / frontend apps)
API layer enables:
Mobile app integration
React / frontend frameworks
Automation and external services

☁️ Deployment
Deployed on Render
PostgreSQL database used in production
Static files handled with WhiteNoise
Environment-based configuration (production-ready)

🛠️ Tech Stack
Backend: Django, Django REST Framework
Database: PostgreSQL (Production), SQLite (Development)
Frontend: HTML, Bootstrap (via CDN)
Authentication: Django Auth (Sessions & Tokens)
Deployment: Render
Server: Gunicorn

📂 Project Structure

project/
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
├── static/
├── requirements.txt
└── manage.py

🔌 REST API Overview
Example Endpoints
Method  Endpoint          Description 
GET     /api/tasks/       List user tasks
POST    /api/tasks/       Create new task
PUT     /api/tasks/<id>/  Update task
DELETE  /api/tasks/<id>/  Delete task

APIs return JSON and are protected using authentication.

⚙️ Environment Variables
The project uses environment variables for security:

SECRET_KEY=
DEBUG=
DATABASE_URL=

These are configured in Render for production.

▶️ Run Locally

git clone <repo-url>
cd project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

📌 Resume Highlight
"Built and deployed a Django-based Todo application with user authentication, priority-based task management, and REST API support, using PostgreSQL and cloud deployment on Render."

👨‍💻 Author
CodeCrafter_droid
Backend Developer (Python / Django)
