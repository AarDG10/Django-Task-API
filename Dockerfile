FROM python:3.12-slim-bookworm  

# Set work directory (Made some changes in this file to best fit the Django REST Api, was previously set for FastAPI)
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Expose Django default port
EXPOSE 8000

# Optional: Run Django's dev server by default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
