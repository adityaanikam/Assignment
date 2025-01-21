# Django Application

## Overview
This project is a Django-based web application designed for real time chatting using web sockets . 

## Features
- User authentication and authorization
- Dynamic content rendering
- Integration with a database with SQLite
- REST API endpoints for external access

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adityaanikam/Assignment.git
   cd <django-app-directory>

2. create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4.Apply migrations:
```bash
python manage.py migrate
```
5.Run the development server
```bash 
daphne -p 8000 chat_project.asgi:application         
```
Usage
Access the app at http://127.0.0.1:8000/ in your browser.
Login or create an account to start using the application.               

Contributing
Feel free to fork this repository and submit pull requests for enhancements or bug fixes.

