FROM python:3

WORKDIR /app

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY dags /opt/airflow/dags

COPY . .

CMD ["tail", "-f", "/dev/null"]