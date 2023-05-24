from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args={
    'owner':'atm1504',
    'retries':5,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2023, 5,24 ),
    schedule_interval='@daily'
) as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is gadhera hain tu!!'
    )
    task1