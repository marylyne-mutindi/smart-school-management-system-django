# 🏫 School Management System - Django Project

This is a Django-based school management system with role-based modules for **Students**, **Parents**, **Teachers**, and **Admins**. It also includes an **Account** app to manage user registration, login, and authentication.

## 🚀 Features

- Role-based authentication system (Student, Teacher, Parent, Admin)
- Separate dashboards and permissions for each role
- Admin panel for managing users and system data
- CRUD operations for student and teacher data
- Parent access to view student performance
- Teacher access to manage class records
- Profile management
- Secure login/logout system

## 🏗️ Project Structure

```bash
school_management/
├── account/            # Handles authentication and user roles
├── student/            # Student-specific views and models
├── teacher/            # Teacher-specific functionalities
├── parent/             # Parent view access
├── admin_panel/        # Admin functionality
├── templates/          # Shared and role-based templates
├── static/             # Static files (CSS, JS, images)
├── school_management/  # Project settings
├── manage.py
└── README.md
