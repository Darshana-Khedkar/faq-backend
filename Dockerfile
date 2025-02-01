# Use Python 3.9 image from Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run Django's development server (or replace with the command you use for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
