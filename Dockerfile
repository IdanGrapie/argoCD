FROM python:3.9-slim

WORKDIR /home/idan/new/gitt/idan.anav/devops/Docker/webapp

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application when the container launches
CMD ["python", "./weather.py"]


