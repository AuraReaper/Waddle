# Waddle API

A high-performance RESTful API for book management and review systems, built with modern Python technologies and designed for scalability.

## 🚀 Features

- **User Authentication & Authorization**: JWT-based auth with role-based access control (admin/user roles)
- **Book Management**: CRUD operations for books with user ownership tracking
- **Review System**: Users can create, read, update, and delete reviews for books
- **Tag System**: Categorize books with custom tags using many-to-many relationships
- **Email Verification**: Asynchronous email verification system using Celery
- **Password Reset**: Secure password reset functionality with time-limited tokens
- **Caching**: Redis-based caching for improved performance
- **Database Migrations**: Alembic for database schema versioning
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation
- **CORS & Security**: Built-in CORS handling and trusted host middleware
- **Request Logging**: Custom middleware for request/response logging with timing

## 🛠 Tech Stack

### Backend Framework
- **FastAPI**: High-performance async web framework
- **Uvicorn**: ASGI server for production deployment

### Database & ORM
- **PostgreSQL**: Primary database with asyncpg driver
- **SQLModel**: Type-safe ORM with Pydantic integration
- **SQLAlchemy**: Advanced ORM features with async support
- **Alembic**: Database migration management

### Authentication & Security
- **JWT (PyJWT)**: JSON Web Tokens with crypto support
- **Passlib**: Password hashing with bcrypt
- **Pydantic**: Data validation and settings management
- **Itsdangerous**: Secure token generation

### Caching & Task Queue
- **Redis**: In-memory caching and session storage
- **Celery**: Distributed task queue for async operations
- **Flower**: Celery monitoring tool

### Email System
- **FastAPI-Mail**: Async email sending capabilities
- **Background Tasks**: Non-blocking email operations

## 📋 Prerequisites

- Python 3.13+
- PostgreSQL
- Redis Server

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/waddle.git
cd waddle
```

2. **Install dependencies using uv**
```bash
uv sync
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Run database migrations**
```bash
alembic upgrade head
```

5. **Start Redis server**
```bash
redis-server
```

6. **Start Celery worker (in a separate terminal)**
```bash
celery -A src.celery_task.c_app worker --loglevel=info
```

7. **Start the API server**
```bash
python main.py
```

## 🌐 API Endpoints

### Authentication
- `POST /api/v1/auth/signup` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/verify/{token}` - Email verification
- `GET /api/v1/auth/refresh_token` - Refresh access token
- `GET /api/v1/auth/logout` - Logout user
- `GET /api/v1/auth/me` - Get current user profile
- `POST /api/v1/auth/password-reset-request` - Request password reset

### Books
- `GET /api/v1/books/` - List all books
- `POST /api/v1/books/` - Create new book
- `GET /api/v1/books/{book_uid}` - Get book details
- `PATCH /api/v1/books/{book_uid}` - Update book
- `DELETE /api/v1/books/{book_uid}` - Delete book
- `GET /api/v1/books/user/{user_uid}` - Get user's books

### Reviews
- Review CRUD operations for books

### Tags
- Tag management and book categorization

## 📊 Database Schema

The application uses the following main entities:
- **Users**: User accounts with roles and verification status
- **Books**: Book information with user ownership
- **Reviews**: Book reviews with ratings
- **Tags**: Book categorization system
- **BookTag**: Many-to-many relationship between books and tags

## 🔒 Security Features

- JWT-based authentication with refresh tokens
- Role-based access control (RBAC)
- Password hashing with bcrypt
- Email verification for new accounts
- Secure token generation for password resets
- Token blacklisting for logout
- CORS protection
- Trusted host middleware

## 📈 Performance & Monitoring

- Async/await throughout the application for high concurrency
- Redis caching for frequently accessed data
- Custom logging middleware with request timing
- Connection pooling with asyncpg
- Background task processing with Celery

## 📖 API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧪 Development

The project uses modern Python development practices:
- Type hints throughout the codebase
- Pydantic models for data validation
- Async/await for I/O operations
- Modular architecture with clear separation of concerns

## 📝 Environment Variables

Required environment variables (see `.env.example`):
- `DATABASE_URL`: PostgreSQL connection string
- `JWT_SECRET`: Secret key for JWT tokens
- `JWT_ALGORITHM`: JWT signing algorithm
- `REDIS_HOST`: Redis server host
- `REDIS_PORT`: Redis server port
- `MAIL_*`: Email configuration for notifications
- `DOMAIN`: Application domain for email links

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For issues and questions, please open a GitHub issue or contact the development team.
