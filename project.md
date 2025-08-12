# Waddle API - Book Management System

## Short Description
A scalable, high-performance RESTful API for book management and review systems, featuring JWT authentication, async processing, and distributed task queues.

## Detailed Description

**Waddle API** is a production-ready book management platform built with modern Python technologies, designed to handle high-throughput operations while maintaining security and scalability. The system enables users to manage personal book collections, write reviews, categorize books with tags, and interact through a comprehensive authentication system.

The application demonstrates advanced backend development patterns including asynchronous programming, distributed task processing, and enterprise-grade security implementations. It features a complete user management system with email verification, password reset functionality, and role-based access control.

### Key Features & Capabilities

**🔐 Advanced Authentication System**
- JWT-based authentication with refresh token rotation
- Role-based access control (RBAC) supporting admin and user roles
- Secure password hashing using bcrypt
- Email verification workflow with time-limited tokens
- Password reset functionality with secure token generation
- Token blacklisting for secure logout

**📚 Comprehensive Book Management**
- Full CRUD operations for book entities
- User ownership tracking and authorization
- Advanced querying capabilities
- Book categorization through flexible tagging system
- Many-to-many relationships between books and tags

**⭐ Review & Rating System**
- User review creation and management
- Rating system with validation constraints
- Review-book-user relationship management
- Review history and user activity tracking

**🚀 High-Performance Architecture**
- Async/await throughout the application for optimal concurrency
- Redis caching layer for frequently accessed data
- Connection pooling with asyncpg for database efficiency
- Custom middleware for request/response logging and timing
- Background task processing with Celery for email operations

**📧 Email Integration**
- Asynchronous email sending using Celery task queues
- SMTP integration with FastAPI-Mail
- Email templates for verification and password reset
- Background processing to prevent blocking operations

**🛡️ Security & Middleware**
- CORS protection with configurable origins
- Trusted host middleware for additional security
- Request/response logging with performance metrics
- Type-safe data validation using Pydantic models

## Technologies Used

### **Core Framework & Runtime**
- **FastAPI** - Modern, fast web framework for building APIs with Python 3.7+
- **Uvicorn** - ASGI web server implementation for Python
- **Python 3.13** - Latest Python runtime with enhanced performance

### **Database Stack**
- **PostgreSQL** - Advanced open-source relational database
- **SQLModel** - Modern Python library for interacting with SQL databases
- **SQLAlchemy** - Python SQL toolkit and Object-Relational Mapping (ORM)
- **asyncpg** - Fast PostgreSQL Database Client Library for Python/asyncio
- **Alembic** - Database migration tool for SQLAlchemy

### **Caching & Task Processing**
- **Redis** - In-memory data structure store for caching and task queues
- **Celery** - Distributed task queue system
- **Flower** - Real-time monitor and web admin for Celery

### **Authentication & Security**
- **PyJWT** - JSON Web Token implementation in Python
- **Passlib** - Password hashing library supporting multiple algorithms
- **bcrypt** - Modern password hashing for secure applications
- **itsdangerous** - Safe data serialization for Python

### **Data Validation & Configuration**
- **Pydantic** - Data validation and parsing using Python type hints
- **Pydantic Settings** - Settings management using Pydantic

### **Email & Communication**
- **FastAPI-Mail** - Simple lightweight mail system for FastAPI
- **SMTP** - Email protocol integration

### **Development & Deployment**
- **uv** - Fast Python package installer and resolver
- **Type Hints** - Static type checking throughout codebase
- **Async/Await** - Asynchronous programming patterns
- **RESTful API Design** - Following REST architectural principles

### **Documentation & Monitoring**
- **OpenAPI/Swagger** - Automatic API documentation generation
- **Custom Logging** - Request/response timing and monitoring
- **CORS Middleware** - Cross-origin resource sharing configuration

## Architecture Highlights

- **Modular Design**: Clean separation of concerns with dedicated modules for authentication, books, reviews, and tags
- **Async-First**: Leveraging Python's asyncio for high-concurrency operations
- **Type Safety**: Comprehensive use of type hints and Pydantic models
- **Database Optimization**: Connection pooling and async database operations
- **Security-First**: Multiple layers of security including JWT, password hashing, and middleware protection
- **Scalability**: Redis caching and Celery task queues for horizontal scaling
- **Maintainability**: Clear project structure with database migrations and comprehensive error handling
