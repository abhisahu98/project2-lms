FROM python:3.10-slim

WORKDIR /app

COPY feedback_system/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY feedback_system /app
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
