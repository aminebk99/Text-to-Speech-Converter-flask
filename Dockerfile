# Use an official Python runtime as a parent image
FROM python:latest

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install any needed packages specified in requirements.txt without caching
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# RUN flask db init

# Create the initial migration
# RUN flask db migrate -m "initial migration"

# # Apply the initial migration
# RUN flask db upgrade

# Expose the port that the app will run on
EXPOSE 5000

# Run Flask when the container launches
CMD ["flask", "run"]