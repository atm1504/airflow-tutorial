from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'atm1504',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v1',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2023, 5, 20),
    schedule_interval='@daily',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo hello world, this is gadhera hain tu!!'
    )
    task1
