#FROM python:3-alpine
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY . .
#EXPOSE 3000
#CMD ["ash", "-c", "python main.py"]



FROM python:3.9.13-bullseye
WORKDIR /app

COPY requirements.txt .

RUN apt-get update -y
#RUN apt-get install libatlas-base-dev -y
#RUN pip install --index-url=https://www.piwheels.org/simple --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python main.py"]
