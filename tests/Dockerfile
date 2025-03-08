# tests/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Install testing requirements (pytest, coverage, etc.)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project for testing
# (Alternatively, copy only what's needed: the main code + test files)
COPY . /app

# Default command runs the tests
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v"]