FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to root of container
COPY . .

# Set PYTHONPATH to include the root directory
ENV PYTHONPATH=/app

# Change to the pokedex directory where the app is located
WORKDIR /app/pokedex

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]