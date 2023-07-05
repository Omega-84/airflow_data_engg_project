from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

from etl_script import car_etl

default_args = {
    'start_date': datetime(2023, 7, 5),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG('airflow_dag', schedule_interval='@daily', default_args=default_args) as dag:
    task = PythonOperator(
        task_id='etl_car',
        python_callable=car_etl
    )