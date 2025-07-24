# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements from ROOT now (not app/)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY app/ .

# Run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
