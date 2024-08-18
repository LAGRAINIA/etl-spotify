FROM apache/airflow:2.7.3-python3.9

# Set working direcotry
WORKDIR /opt/airflow

# Set the PYTHONPATH to include the required directories
ENV PYTHONPATH "/opt/plugins"


# Copy DAGs and other necessary files
COPY plugins/ /opt/plugins
COPY .env /opt/.env
COPY requirements.txt /opt/requirements.txt

# Change ownership of .spotify_cache to airflow user
USER root
RUN chown -R airflow:root /opt/.env

# Grant read and write permissions to the airflow group
RUN chmod -R 775 /opt/.env

# Switch back to the airflow user for further operations
USER airflow

# Install requirements
RUN pip install --no-cache-dir -r /opt/requirements.txt


# Set the default command
#CMD ["airflow", "webserver"]
