# OrgFlow - Company Administration Portal

> A production-oriented Company Administration Portal built with Django Templates and PostgreSQL.

---
# Philosophy

This project is not built to learn Django.

It is built to learn Software Engineering.

The same business system will be implemented in three different technologies:

- Django Templates
- Django REST Framework
- FastAPI

The goal is to understand software architecture, system design, database design, and backend engineering rather than becoming dependent on a single framework.


## 📌 Project Overview

OrgFlow is a web-based Company Administration Portal designed to manage an organization's internal workflow.

The primary objective of this project is to build a scalable, maintainable, and production-oriented backend system by following real software engineering principles instead of tutorial-based development.

This repository contains the **Django Template Version (V1)** of OrgFlow.

Future implementations will be developed separately:

- OrgFlow DRF Edition
- OrgFlow FastAPI Edition

The business logic, database design, and system architecture remain the same across all versions while only the implementation technology changes.

---

# 🎯 Project Objectives

- Learn Software Engineering through project development
- Design scalable database architecture
- Implement enterprise-level RBAC
- Build reusable and maintainable Django applications
- Follow production-level coding standards
- Write documentation before implementation
- Understand business-first backend development

---

# 🚀 Technology Stack

- Python 3.11+
- Django 5.x
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Git & GitHub

---

# 🏗 Project Architecture

This project follows a **Modular Monolith Architecture**.

```
apps/
│
├── accounts/
├── core/
├── departments/
├── employees/
├── notifications/
├── projects/
├── tasks/
└── teams/
```

Each Django application represents a single business domain.

---

# 📂 Project Structure

```
OrgFlow/
│
├── apps/
├── config/
├── docs/
├── logs/
├── media/
├── scripts/
├── static/
├── templates/
│
├── manage.py
├── requirements.txt
├── README.md
└── .env
```

---

# 📚 Documentation

Project documentation is available inside the `docs/` directory.

Current documents include:

- Project Vision
- Software Requirement Specification (SRS)
- User Roles
- Business Rules
- Project Scope
- Glossary
- Database Design
- Software Architecture

---

# 🏢 Core Modules

- Authentication
- Employee Management
- Department Management
- Team Management
- Project Management
- Task Management
- Notification System

Additional modules such as Attendance, Leave Management, Payroll, and Asset Management are planned for future versions.

---

# 🎯 Development Philosophy

This project follows the principle:

```
Business Problem
        ↓
Requirement Analysis
        ↓
System Design
        ↓
Database Design
        ↓
Implementation
        ↓
Testing
```

The focus is on understanding **why** a feature exists before implementing **how** it is built.

---

# 📌 Current Version

Version: **V1**

Implementation:

- Django Template Based

Database:

- PostgreSQL

Architecture:

- Modular Monolith

---
# Project Status
- Under Development

# 🚧 Future Roadmap

### Version 1

- Django Templates

### Version 2

- Django REST Framework
- JWT Authentication
- Swagger Documentation

### Version 3

- FastAPI
- SQLAlchemy
- Async APIs
- Production Deployment

---

# 👨‍💻 Author

**Anoop Kushwaha**

Backend Engineering Learning Project

---

# 📄 License

This project is developed for educational purposes while following production-oriented software engineering practices.