FROM python:3.11-slim 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN apt-get update && apt-get install -y \
    netcat gcc postgresql \
    && apt-get clean
    
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/code/entrypoint.sh"]
