# MiniBlog Pro (React + Flask Full Stack Project)

## Description
MiniBlog Pro is a full-stack web application that allows users to register, login, create blog posts, edit, delete, and like posts. It uses JWT authentication to secure private routes and Flask as a RESTful backend with a React frontend.

---

## Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Protected Routes

### Blog System
- Create Posts
- Edit Posts
- Delete Posts
- View All Posts
- View Single Post

### Interaction
- Like Posts (Many-to-Many)
- View Likes Count

### User Features
- Profile Management
- Dashboard Analytics
- View Own Posts
- View Own Likes

---

## Tech Stack

### Frontend
- React (Vite)
- React Router DOM
- Axios
- Context API

### Backend
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Flask CORS
- SQLite

---

## Database Relationships

### One-to-Many
- One User → Many Posts

### Many-to-Many
- Many Users ↔ Many Posts (Likes)

---

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
python seed.py
python app.py
