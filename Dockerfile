FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy Django project code
COPY . .

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]