FROM python:3.8-slim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Run the worker
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]