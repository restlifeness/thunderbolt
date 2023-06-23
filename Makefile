# Makefile

# Alembic migrations
migrate:
    alembic upgrade head

# Pytest testing
test:
    pytest .tests

# Starting the application with Docker Compose
start:
    docker-compose up -d

# Stopping the application with Docker Compose
stop:
    docker-compose down
