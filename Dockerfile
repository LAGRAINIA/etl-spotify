FROM python:3

WORKDIR /app

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Install Airflow and other dependencies from requirements.txt
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Create necessary directories and set permissions
RUN mkdir -p /opt/airflow/logs /opt/airflow/dags && \
    chmod -R 777 /opt/airflow/logs /opt/airflow/dags

# Copy DAGs and other necessary files
COPY dags /opt/airflow/dags
COPY . .

# Set the default command
CMD ["airflow", "webserver"]
