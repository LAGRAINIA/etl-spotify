from datetime import timedelta, datetime
import sys
import os

sys.path.append("/opt")

from airflow import DAG #type:ignore
from airflow.operators.python import PythonOperator #type:ignore
import sys
import os
from dotenv import load_dotenv

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


# Add the base directory to sys.path
# sys.path.insert(0, os.path.abspath('.'))
from plugins.utils.etl.extract_spotify_data import extract_data


def print_hello():
    print("Hello, Airflow !")
    print("I finally sucess my first dag !!!!")
    print(extract_data())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 11),  # Correction de 'star_date' en 'start_date'
    'email': ['anass.lagraini94@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)  # Correction de 'retry_dely' en 'retry_delay'
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='Un DAG simple pour imprimer un message',
    schedule_interval='*/10 * * * *'  # Exécuter toutes les 10 minutes
)

hello_task = PythonOperator(
    task_id='hello_task',  # Correction de 'Hello _task' en 'hello_task'
    python_callable=print_hello,
    dag=dag,
)

hello_task
