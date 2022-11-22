
FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY test_task/ .

CMD ["python3", "manage.py", "runserver", "0:8000"]
