FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8000

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py loaddata fixtures.json && python3 manage.py runserver 0.0.0.0:8000"]