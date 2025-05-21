# FastAPI Tasks Application

A task management application built with FastAPI, Redis, and Docker.

## Features

- User authentication and authorization
- Task management
- Redis integration for caching
- Docker containerization

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Redis

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd FASTAPI-tasks
```

2. Using Docker (Recommended):
```bash
docker-compose up --build
```

3. Manual Installation:
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
FASTAPI-tasks/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   ├── core/
│   ├── db/
│   ├── models/
│   └── schemas/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./fastapi-tasks.db
REDIS_HOST=localhost
REDIS_PORT=6379
```

## License

MIT 