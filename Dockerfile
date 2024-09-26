FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy the Flask app
COPY . .

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=hello.py

# Expose the port Flask runs on
EXPOSE 5000

# Run Flask
CMD ["flask", "run", "--host=0.0.0.0"]
