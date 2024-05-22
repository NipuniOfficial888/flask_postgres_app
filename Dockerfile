FROM python:3.11-alpine
RUN apk add --no-cache postgresql-dev gcc musl-dev
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]

