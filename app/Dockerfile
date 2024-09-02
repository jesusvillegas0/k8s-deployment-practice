FROM python:3.9-slim
WORKDIR /app
COPY app/app.py /app
RUN pip install flask
ENV APP_VERSION=1.0.0
CMD ["python", "app.py"]
