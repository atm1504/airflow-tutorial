from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'atm1504',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='our_first_dag_v4',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2023, 5, 24),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is gadhera hain tu!!'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo u r looking very beautiful! April fool"
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo Hain thik hai makeup karle be..."
    )
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    task1 >> task2
    task1 >> task3
