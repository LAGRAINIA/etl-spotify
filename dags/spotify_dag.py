from datetime import timedelta
from aiflow  import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago 
import datetime

def print_hello() : 
    print("Hello, Airflow !")


default_args = {
    'owner': 'airflow', 
    'depends_on_past': False,
    'star_date': datetime(2024,8, 8),
    'email': ['anass.lagraini94@gmail.com'], 
    'email_on_failure': False,
    'email_on_retry': False, 
    'retries': 1,
    'retry_dely': timedelta(minutes=1)
}

dag= DAG(
    'simple_dag',
    default_args=default_args,
    description='Un DAG simple pour imprimer un message',
    schedule_interval='*/10 * * * *' # Exécuter tous les jours à 15h30
)

hello_task= PythonOperator(
    task_id='Hello _task',
    python_callable=print_hello,
    dag=dag,
)

hello_task