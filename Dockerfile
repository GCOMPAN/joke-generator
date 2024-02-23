FROM python:3.8.7

# Set the working directory in the container
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install --upgrade pip

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy the rest of the application source
COPY . .

# Expose the port the app runs on
EXPOSE 5000 

# Command to run the application with config.yml
CMD ["python", "app.py", "--config", "config.yml"]